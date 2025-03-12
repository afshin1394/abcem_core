

"""seed database

Revision ID: a0cfefe5e051
Revises: d615c90a10ca
Create Date: 2025-02-24 06:50:08.082334

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

from app.domain.enums.complaint_type_enum import ComplaintTypeEnum
from app.domain.enums.problematic_service_enum import ProblematicServiceEnum
from app.domain.enums.service_type_enum import ServiceTypeEnum
from app.domain.enums.step_test_type_enum import StepTestTypeEnum
from app.domain.enums.technology_enum import TechnologyEnum
from app.domain.enums.walk_test_state_enum import WalkTestStatusEnum

# revision identifiers, used by Alembic.
revision: str = 'a0cfefe5e051'
down_revision: Union[str, None] = "d615c90a10ca"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# Define Tables
table_technology_type = sa.table(
    "table_technology_type",
    sa.column("id", sa.Integer),
    sa.column("name", sa.String)
)

table_walk_test_status = sa.table(
    "table_walk_test_status",
    sa.column("id", sa.Integer),
    sa.column("name", sa.String)
)

table_complaint_type = sa.table(
    "table_complaint_type",
    sa.column("id", sa.Integer),
    sa.column("name", sa.String)
)

table_problematic_service = sa.table(
    "table_problematic_service",
    sa.column("id", sa.Integer),
    sa.column("name", sa.String)
)

table_step_type = sa.table(
    "table_step_test_type",
    sa.column("id", sa.Integer),
    sa.column("name", sa.String)
)

table_service_type = sa.table(
    "table_service_type",
    sa.column("id", sa.Integer),
    sa.column("name", sa.String)
)

def upgrade() -> None:
    # Convert Enum to dictionary format
    technology_data = [{"id": tech.value, "name": tech.name} for tech in TechnologyEnum]
    walk_test_status_data = [{"id": state.value, "name": state.name} for state in WalkTestStatusEnum]
    complaint_type_data = [{"id": complaint_type.value, "name": complaint_type.name} for complaint_type in ComplaintTypeEnum]
    problematic_service_data = [{"id": service.value, "name": service.name} for service in ProblematicServiceEnum]
    step_type_data = [{"id": step.value, "name": step.name} for step in StepTestTypeEnum]
    service_type_data = [{"id": service_type.value, "name": service_type.name} for service_type in ServiceTypeEnum]

    # Insert data into tables
    op.bulk_insert(table_technology_type, technology_data)
    op.bulk_insert(table_walk_test_status, walk_test_status_data)
    op.bulk_insert(table_complaint_type, complaint_type_data)
    op.bulk_insert(table_problematic_service, problematic_service_data)
    op.bulk_insert(table_step_type, step_type_data)
    op.bulk_insert(table_service_type,service_type_data)

def downgrade() -> None:
    conn = op.get_bind()

    # Update table_walk_test to set the foreign key to NULL for technology_type_id references.
    # This prevents the foreign key violation when deleting from table_technology_type.
    tech_ids = tuple(tech.value for tech in TechnologyEnum)
    if tech_ids:
        # Construct a comma-separated list of ids for the SQL statement.
        tech_ids_str = ", ".join(str(t) for t in tech_ids)
        conn.execute(
            text(f"UPDATE table_walk_test SET technology_type_id = NULL WHERE technology_type_id IN ({tech_ids_str})")
        )
    # 2. Nullify foreign key references to table_walk_test_status in table_walk_test.
    walk_status_ids = tuple(state.value for state in WalkTestStatusEnum)
    if walk_status_ids:
        walk_ids_str = ", ".join(str(s) for s in walk_status_ids)
        conn.execute(
            text(f"UPDATE table_walk_test SET walk_test_status_id = NULL WHERE walk_test_status_id IN ({walk_ids_str})")
        )

        # 3. Nullify foreign key references to table_complaint_type.
    complaint_ids = tuple(ct.value for ct in ComplaintTypeEnum)
    if complaint_ids:
        complaint_ids_str = ", ".join(str(c) for c in complaint_ids)
        conn.execute(
            text(
                f"UPDATE table_walk_test SET complaint_type_id = NULL WHERE complaint_type_id IN ({complaint_ids_str})")
        )

    # 4. Nullify references to table_problematic_service.
    problematic_service_ids = tuple(ps.value for ps in ProblematicServiceEnum)
    if problematic_service_ids:
        problematic_service_ids_str = ", ".join(str(ps) for ps in problematic_service_ids)
        conn.execute(
            text(f"UPDATE table_walk_test SET problematic_service_id = NULL WHERE problematic_service_id IN ({problematic_service_ids_str})")
        )

    # 5. Nullify references to table_service_type.
    # service_type_ids = tuple(st.value for st in ServiceTypeEnum)
    # if service_type_ids:
    #     service_type_ids_str = ", ".join(str(s) for s in service_type_ids)
    #     conn.execute(
    #         text(f"UPDATE table_walk_test SET service_type_id = NULL WHERE service_type_id IN ({service_type_ids_str})")
    #     )
    # Delete from table_technology_type
    if tech_ids:
        conn.execute(text(f"DELETE FROM table_technology_type WHERE id IN {tech_ids}"))

    if walk_status_ids:
        conn.execute(text(f"DELETE FROM table_walk_test_status WHERE id IN {walk_status_ids}"))

    if complaint_ids:
        conn.execute(text(f"DELETE FROM table_complaint_type WHERE id IN {complaint_ids}"))

    if problematic_service_ids:
        conn.execute(text(f"DELETE FROM table_problematic_service WHERE id IN {problematic_service_ids}"))

    service_type_ids = tuple(st.value for st in ServiceTypeEnum)
    if service_type_ids:
        # 1. Temporarily allow NULL values by dropping the NOT NULL constraint.
        conn.execute(text("ALTER TABLE table_walk_test ALTER COLUMN service_type_id DROP NOT NULL"))

        # 2. Update rows in table_walk_test that reference these service types, setting the foreign key to NULL.
        service_type_ids_str = ", ".join(str(s) for s in service_type_ids)
        conn.execute(
            text(f"UPDATE table_walk_test SET service_type_id = NULL WHERE service_type_id IN ({service_type_ids_str})")
        )

    # if service_type_ids:
    #     conn.execute(text(f"DELETE FROM table_service_type WHERE id IN {service_type_ids}"))
    # Delete from table_walk_test_status
    walk_status_ids = tuple(state.value for state in WalkTestStatusEnum)
    if walk_status_ids:
        conn.execute(text(f"DELETE FROM table_walk_test_status WHERE id IN {walk_status_ids}"))

    # Delete from table_complaint_type
    complaint_ids = tuple(ct.value for ct in ComplaintTypeEnum)
    if complaint_ids:
        conn.execute(text(f"DELETE FROM table_complaint_type WHERE id IN {complaint_ids}"))

    # Delete from table_problematic_service
    problematic_service_ids = tuple(ps.value for ps in ProblematicServiceEnum)
    if problematic_service_ids:
        conn.execute(text(f"DELETE FROM table_problematic_service WHERE id IN {problematic_service_ids}"))

    # Delete from table_step_type
    step_ids = tuple(st.value for st in StepTestTypeEnum)
    if step_ids:
        conn.execute(text(f"DELETE FROM table_step_test_type WHERE id IN {step_ids}"))

    # Delete from table_service_type
    service_type_ids = tuple(st.value for st in ServiceTypeEnum)
    if service_type_ids:
        conn.execute(text(f"DELETE FROM table_service_type WHERE id IN {service_type_ids}"))