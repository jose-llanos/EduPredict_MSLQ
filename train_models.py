"""
Script para entrenar modelos inicialmente
Ejecutar: python train_models.py
"""

import sys
import os
from pathlib import Path

# Cambiar al directorio del script
os.chdir(Path(__file__).parent)

# Agregar la ruta del proyecto
sys.path.insert(0, str(Path(__file__).parent))

from app.models.model_loader import ModelManager
from app.config import settings
from app.utils import setup_logger

# Configurar logger
logger = setup_logger("train_models", log_file=f"{settings.logs_path}/training.log")


def main():
    """Función principal de entrenamiento"""
    logger.info("=" * 60)
    logger.info("Iniciando entrenamiento de modelos")
    logger.info("=" * 60)
    
    try:
        # Crear gestor de modelos
        model_manager = ModelManager(
            data_path=settings.data_path,
            models_path=settings.models_path
        )
        
        # Cargar datos
        logger.info("Cargando datos de entrenamiento...")
        data = model_manager.load_training_data("data-model-mslq-pretest-207.csv")
        
        # Preprocesar
        logger.info("Preprocesando datos...")
        data = model_manager.preprocess_data(data)
        
        # Entrenar modelos
        logger.info("\n" + "=" * 60)
        logger.info("ENTRENANDO MODELO SEMANA 4")
        logger.info("=" * 60)
        model_4 = model_manager.train_model(
            data, 
            settings.features_week_4, 
            week=4
        )
        model_manager.save_model(model_4, 'model_week_4.pkl')
        
        logger.info("\n" + "=" * 60)
        logger.info("ENTRENANDO MODELO SEMANA 8")
        logger.info("=" * 60)
        model_8 = model_manager.train_model(
            data, 
            settings.features_week_8, 
            week=8
        )
        model_manager.save_model(model_8, 'model_week_8.pkl')
        
        logger.info("\n" + "=" * 60)
        logger.info("ENTRENANDO MODELO SEMANA 12")
        logger.info("=" * 60)
        model_12 = model_manager.train_model(
            data, 
            settings.features_week_12, 
            week=12
        )
        model_manager.save_model(model_12, 'model_week_12.pkl')
        
        logger.info("\n" + "=" * 60)
        logger.info("✅ Entrenamiento completado exitosamente")
        logger.info("=" * 60)
        logger.info("Modelos guardados en:", settings.models_path)
        
    except Exception as e:
        logger.error(f"❌ Error durante el entrenamiento: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
