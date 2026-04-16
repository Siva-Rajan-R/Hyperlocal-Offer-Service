from fastapi import FastAPI
from infra.primary_db.main import init_pg_db
from contextlib import asynccontextmanager
from icecream import ic
from dotenv import load_dotenv
import os,asyncio
from core.configs.settings_config import SETTINGS
from api.routers.v1 import offer_routes,coupon_routes
from hyperlocal_platform.core.enums.environment_enum import EnvironmentEnum
load_dotenv()


@asynccontextmanager
async def offer_service_lifespan(app:FastAPI):
    try:
        ic("Starting offer service...")
        await init_pg_db()
        # asyncio.create_task(worker())
        yield

    except Exception as e:
        ic(f"Error : Starting offer service => {e}")

    finally:
        ic("...Stoping offer Servcie...")

debug=False
openapi_url=None
docs_url=None
redoc_url=None

if SETTINGS.ENVIRONMENT.value==EnvironmentEnum.DEVELOPMENT.value:
    debug=True
    openapi_url="/openapi.json"
    docs_url="/docs"
    redoc_url="/redoc"

app=FastAPI(
    title="Offer Service",
    description="This service contains all the CRUD operations for offer service",
    debug=debug,
    openapi_url=openapi_url,
    docs_url=docs_url,
    redoc_url=redoc_url,
    lifespan=offer_service_lifespan
)



# Routes to include
app.include_router(offer_routes.router)
app.include_router(coupon_routes.router)


