"""
Routers API v1
"""

from fastapi import APIRouter, HTTPException, status
from app.schemas import (
    PredictionRequest,
    PredictionResponse,
    StudentPredictionRequest,
    StudentPredictionResponse,
    BatchPredictionRequest,
    BatchPredictionResponse,
)
from app.services import PredictionService
from app.models.model_loader import ModelManager
from app.config import settings
import logging

logger = logging.getLogger(__name__)

# Instanciar servicios
model_manager = ModelManager(
    data_path=settings.data_path,
    models_path=settings.models_path
)
prediction_service = PredictionService(model_manager)

# Crear router
router = APIRouter(prefix="/api/v1", tags=["predictions"])


@router.get("/health", tags=["health"])
async def health_check():
    """Verifica el estado de la API"""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version
    }


@router.post(
    "/predict",
    response_model=PredictionResponse,
    status_code=status.HTTP_200_OK,
    summary="Realizar predicción individual",
    description="Realiza una predicción de desempeño académico para una semana específica"
)
async def predict(request: PredictionRequest) -> PredictionResponse:
    """
    Realiza predicción individual de desempeño académico
    
    - **week**: Semana de predicción (4, 8 o 12)
    - **practica_1, practica_2, practica_3**: Calificaciones de prácticas
    - **I11-I75**: Características del cuestionario MSLQ
    
    Retorna predicción, nivel de desempeño y confianza
    """
    try:
        # Obtener features requeridas para la semana
        required_features = prediction_service.get_features_by_week(request.week)
        
        # Preparar diccionario completo con todos los valores disponibles
        all_values = {
            "practica_1": request.practica_1,
            "practica_2": request.practica_2 or 0.0,
            "practica_3": request.practica_3 or 0.0,
            "I11": request.I11,
            "I18": request.I18,
            "I24": request.I24,
            "I33": request.I33,
            "I38": request.I38,
            "I40": request.I40,
            "I49": request.I49,
            "I50": request.I50,
            "I61": request.I61,
            "I63": request.I63,
            "I69": request.I69,
            "I70": request.I70,
            "I71": request.I71,
            "I75": request.I75,
        }
        
        # Crear diccionario solo con los features necesarios para esta semana
        features_dict = {feat: all_values[feat] for feat in required_features}
        
        # Realizar predicción
        prediction, confidence = prediction_service.predict(request.week, features_dict)
        performance_level, performance_range = prediction_service.get_performance_info(prediction)
        
        return PredictionResponse(
            prediction=int(prediction),
            performance_level=performance_level,
            performance_range=performance_range,
            week=request.week,
            confidence_score=round(confidence, 4)
        )
    
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Error en predicción: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )


@router.post(
    "/predict-student",
    response_model=StudentPredictionResponse,
    status_code=status.HTTP_200_OK,
    summary="Predicción para estudiante específico",
    description="Realiza predicción de desempeño para un estudiante identificado"
)
async def predict_student(request: StudentPredictionRequest) -> StudentPredictionResponse:
    """
    Realiza predicción para un estudiante específico
    
    Incluye nombre del estudiante y datos académicos/MSLQ
    """
    try:
        # Obtener features requeridas para la semana
        required_features = prediction_service.get_features_by_week(request.week)
        
        # Preparar diccionario completo
        all_values = {
            "corte_1": request.corte_1,
            "corte_2": request.corte_2 or 0.0,
            "corte_3": request.corte_3 or 0.0,
            "practica_1": request.corte_1,
            "practica_2": request.corte_2 or 0.0,
            "practica_3": request.corte_3 or 0.0,
            "I11": request.I11,
            "I18": request.I18,
            "I24": request.I24,
            "I33": request.I33,
            "I38": request.I38,
            "I40": request.I40,
            "I49": request.I49,
            "I50": request.I50,
            "I61": request.I61,
            "I63": request.I63,
            "I69": request.I69,
            "I70": request.I70,
            "I71": request.I71,
            "I75": request.I75,
        }
        
        # Crear diccionario solo con los features necesarios
        data_dict = {feat: all_values[feat] for feat in required_features}
        
        # Predicción
        result = prediction_service.predict_student(
            request.week,
            request.student_name,
            data_dict
        )
        
        return StudentPredictionResponse(**result)
    
    except Exception as e:
        logger.error(f"Error en predicción de estudiante: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )


@router.post(
    "/predict-batch",
    response_model=BatchPredictionResponse,
    status_code=status.HTTP_200_OK,
    summary="Predicción en lote",
    description="Realiza predicciones para múltiples estudiantes simultáneamente"
)
async def predict_batch(request: BatchPredictionRequest) -> BatchPredictionResponse:
    """
    Realiza predicciones en lote para múltiples estudiantes
    
    Retorna todas las predicciones y tiempo de procesamiento
    """
    try:
        # Obtener features requeridas para la semana
        required_features = prediction_service.get_features_by_week(request.week)
        
        # Preparar datos
        students_data = []
        for student in request.predictions:
            all_values = {
                "student_name": student.student_name,
                "corte_1": student.corte_1,
                "corte_2": student.corte_2 or 0.0,
                "corte_3": student.corte_3 or 0.0,
                "practica_1": student.corte_1,
                "practica_2": student.corte_2 or 0.0,
                "practica_3": student.corte_3 or 0.0,
                "I11": student.I11,
                "I18": student.I18,
                "I24": student.I24,
                "I33": student.I33,
                "I38": student.I38,
                "I40": student.I40,
                "I49": student.I49,
                "I50": student.I50,
                "I61": student.I61,
                "I63": student.I63,
                "I69": student.I69,
                "I70": student.I70,
                "I71": student.I71,
                "I75": student.I75,
            }
            
            # Crear diccionario solo con features necesarios
            data = {"student_name": student.student_name}
            data.update({feat: all_values[feat] for feat in required_features})
            students_data.append(data)
        
        # Predicciones en lote
        predictions, processing_time = prediction_service.batch_predict(
            request.week,
            students_data
        )
        
        return BatchPredictionResponse(
            total_predictions=len(predictions),
            predictions=[StudentPredictionResponse(**p) for p in predictions],
            processing_time=round(processing_time, 4)
        )
    
    except Exception as e:
        logger.error(f"Error en predicción en lote: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )


@router.get(
    "/info",
    status_code=status.HTTP_200_OK,
    summary="Información de la API",
    description="Obtiene información sobre los modelos y características disponibles"
)
async def api_info():
    """Obtiene información de la API"""
    return {
        "app_name": settings.app_name,
        "version": settings.app_version,
        "description": settings.description,
        "available_weeks": [4, 8, 12],
        "performance_levels": settings.performance_levels,
        "features": {
            "week_4": settings.features_week_4,
            "week_8": settings.features_week_8,
            "week_12": settings.features_week_12
        }
    }
