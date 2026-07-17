"""
Esquemas Pydantic para validación de datos de predicción
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class PredictionRequest(BaseModel):
    """Esquema para solicitud de predicción individual"""
    
    week: int = Field(
        ..., 
        ge=4, 
        le=12,
        description="Semana de predicción (4, 8 o 12)"
    )
    practica_1: float = Field(..., description="Calificación práctica 1")
    practica_2: Optional[float] = Field(None, description="Calificación práctica 2")
    practica_3: Optional[float] = Field(None, description="Calificación práctica 3")
    
    # Características MSLQ
    I11: float = Field(...)
    I18: float = Field(...)
    I24: float = Field(...)
    I33: float = Field(...)
    I38: float = Field(...)
    I40: float = Field(...)
    I49: float = Field(...)
    I50: float = Field(...)
    I61: float = Field(...)
    I63: float = Field(...)
    I69: float = Field(...)
    I70: float = Field(...)
    I71: float = Field(...)
    I75: float = Field(...)
    
    class Config:
        json_schema_extra = {
            "example": {
                "week": 4,
                "practica_1": 4.2,
                "practica_2": None,
                "practica_3": None,
                "I11": 3.5,
                "I18": 4.0,
                "I24": 3.8,
                "I33": 4.1,
                "I38": 3.9,
                "I40": 4.2,
                "I49": 3.7,
                "I50": 4.0,
                "I61": 3.6,
                "I63": 3.9,
                "I69": 4.1,
                "I70": 4.0,
                "I71": 3.8,
                "I75": 4.2
            }
        }


class PredictionResponse(BaseModel):
    """Esquema para respuesta de predicción"""
    
    prediction: int = Field(
        ..., 
        description="Predicción de desempeño (0: Bajo, 1: Medio, 2: Alto)"
    )
    performance_level: str = Field(..., description="Descripción del nivel de desempeño")
    performance_range: str = Field(..., description="Rango de calificación")
    week: int = Field(..., description="Semana de predicción")
    confidence_score: float = Field(
        ..., 
        ge=0, 
        le=1,
        description="Confianza de la predicción"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "prediction": 2,
                "performance_level": "Alto desempeño",
                "performance_range": "4.1 - 5.0",
                "week": 4,
                "confidence_score": 0.85
            }
        }


class StudentPredictionRequest(BaseModel):
    """Esquema para predicción de estudiante específico"""
    
    student_name: str = Field(..., description="Nombre del estudiante")
    week: int = Field(ge=4, le=12, description="Semana de predicción")
    corte_1: float = Field(..., description="Calificación corte 1")
    corte_2: Optional[float] = Field(None, description="Calificación corte 2")
    corte_3: Optional[float] = Field(None, description="Calificación corte 3")
    
    # MSLQ Features
    I11: float
    I18: float
    I24: float
    I33: float
    I38: float
    I40: float
    I49: float
    I50: float
    I61: float
    I63: float
    I69: float
    I70: float
    I71: float
    I75: float


class StudentPredictionResponse(BaseModel):
    """Esquema para respuesta de predicción de estudiante"""
    
    student_name: str
    prediction: int
    performance_level: str
    performance_range: str
    week: int
    confidence_score: float
    prediction_date: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "student_name": "Juan Pérez",
                "prediction": 2,
                "performance_level": "Alto desempeño",
                "performance_range": "4.1 - 5.0",
                "week": 4,
                "confidence_score": 0.92,
                "prediction_date": "2024-01-15T10:30:00"
            }
        }


class BatchPredictionRequest(BaseModel):
    """Esquema para predicción en lote"""
    
    week: int = Field(ge=4, le=12, description="Semana de predicción")
    predictions: List[StudentPredictionRequest] = Field(
        ..., 
        description="Lista de estudiantes para predicción"
    )


class BatchPredictionResponse(BaseModel):
    """Esquema para respuesta de predicción en lote"""
    
    total_predictions: int
    predictions: List[StudentPredictionResponse]
    processing_time: float = Field(..., description="Tiempo de procesamiento en segundos")
    
    class Config:
        json_schema_extra = {
            "example": {
                "total_predictions": 2,
                "predictions": [
                    {
                        "student_name": "Juan Pérez",
                        "prediction": 2,
                        "performance_level": "Alto desempeño",
                        "performance_range": "4.1 - 5.0",
                        "week": 4,
                        "confidence_score": 0.92,
                        "prediction_date": "2024-01-15T10:30:00"
                    }
                ],
                "processing_time": 0.234
            }
        }
