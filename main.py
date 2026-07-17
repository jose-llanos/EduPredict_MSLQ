"""
Aplicación FastAPI principal - Clasificación MSLQ CORHUILA
"""

import os
from pathlib import Path
from contextlib import asynccontextmanager

# Asegurar que estamos en el directorio correcto
os.chdir(Path(__file__).parent)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.config import settings
from app.api import v1_router
from app.utils import setup_logger

# Configurar logger
logger = setup_logger(
    "mslq_api",
    log_file=f"{settings.logs_path}/api.log"
)


# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manejo del ciclo de vida de la aplicación"""
    # Startup
    logger.info(f"🚀 Iniciando {settings.app_name} v{settings.app_version}")
    logger.info(f"📝 Documentación disponible en: http://localhost:{settings.port}/docs")
    yield
    # Shutdown
    logger.info("👋 Cerrando aplicación")


# Crear aplicación
app = FastAPI(
    title=settings.app_name,
    description=settings.description,
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(v1_router)


@app.get("/", tags=["root"])
async def root():
    """Endpoint raíz"""
    return {
        "message": f"Bienvenido a {settings.app_name}",
        "version": settings.app_version,
        "docs": "http://localhost:8000/docs"
    }


# Personalizar OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title=settings.app_name,
        version=settings.app_version,
        description=settings.description,
        routes=app.routes,
    )
    
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="info"
    )
