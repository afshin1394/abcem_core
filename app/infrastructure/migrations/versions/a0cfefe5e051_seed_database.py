

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
    conn = op.get_bind()  # Get database connection

    # Delete from `table_technology_type`
    ids = tuple(tech.value for tech in TechnologyEnum)
    if ids:  # Prevent SQL error for empty tuple
        conn.execute(text(f"DELETE FROM table_technology_type WHERE id IN {ids}"))

    # Delete from `table_walk_test_status`
    ids = tuple(state.value for state in WalkTestStatusEnum)
    if ids:
        conn.execute(text(f"DELETE FROM table_walk_test_status WHERE id IN {ids}"))

    # Delete from `table_complaint_type`
    ids = tuple(complaint_type.value for complaint_type in ComplaintTypeEnum)
    if ids:
        conn.execute(text(f"DELETE FROM table_complaint_type WHERE id IN {ids}"))

    # Delete from `table_problematic_service`
    ids = tuple(service.value for service in ProblematicServiceEnum)
    if ids:
        conn.execute(text(f"DELETE FROM table_problematic_service WHERE id IN {ids}"))

    # Delete from `table_step_type`
    ids = tuple(step.value for step in StepTestTypeEnum)
    if ids:
        conn.execute(text(f"DELETE FROM table_step_type WHERE id IN {ids}"))

    ids = tuple(service_type.value for service_type in ServiceTypeEnum)
    if ids:
        conn.execute(text(f"DELETE FROM table_service_type WHERE id IN {ids}"))