from fastapi import HTTPException, APIRouter
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession
from app.main import app

router_v1 = APIRouter(
    prefix="/health",
    tags=["health"],
)
@app.get("/check_data_base")
def health_check(db : AsyncSession):
    try:
        with db:
            db.execute(f'SELECT id from  public.table_speed_test_servers')
        return {"status": "ok"}
    except OperationalError:
        raise HTTPException(status_code=503, detail="Database not ready")