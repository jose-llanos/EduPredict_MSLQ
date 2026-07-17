"""
Configuración de la aplicación
"""

from pydantic_settings import BaseSettings
from typing import Optional
from pathlib import Path


def get_base_dir():
    """Obtiene el directorio base de la aplicación"""
    return Path(__file__).parent.parent.resolve()


class Settings(BaseSettings):
    """Configuración de la aplicación FastAPI"""
    
    # Información de la API
    app_name: str = "API Edu Predict MSLQ"
    app_version: str = "1.0.0"
    description: str = "API para predicción de desempeño académico basada en MSLQ"
    
    # Configuración del servidor
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Rutas (resolver a rutas absolutas en tiempo de ejecución)
    def __init__(self, **data):
        super().__init__(**data)
        base_dir = get_base_dir()
        self.data_path = str(base_dir / "data")
        self.models_path = str(base_dir / "models")
        self.logs_path = str(base_dir / "logs")
    
    # Valores por defecto (se sobrescriben en __init__)
    data_path: str = ""
    models_path: str = ""
    logs_path: str = ""
    
    # Configuración de modelos
    test_size: float = 0.20
    random_state: int = 42
    
    # Features por época
    features_week_4: list = [
        "practica_1", "I18", "I50", "I33", "I38", "I40", "I49", 
        "I70", "I61", "I24", "I11", "I69", "I63", "I71", "I75"
    ]
    
    features_week_8: list = [
        "practica_1", "practica_2", "I18", "I50", "I33", "I38", "I40", 
        "I49", "I70", "I61", "I24", "I11", "I69", "I63", "I71", "I75"
    ]
    
    features_week_12: list = [
        "practica_1", "practica_2", "practica_3", "I18", "I50", "I33", "I38", 
        "I40", "I49", "I70", "I61", "I24", "I11", "I69", "I63", "I71", "I75"
    ]
    
    # Umbral de desempeño
    performance_levels: dict = {
        0: {"name": "Bajo desempeño", "range": "0.0 - 2.9"},
        1: {"name": "Medio desempeño", "range": "3.0 - 4.0"},
        2: {"name": "Alto desempeño", "range": "4.1 - 5.0"}
    }
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Instancia global de configuración
settings = Settings()
