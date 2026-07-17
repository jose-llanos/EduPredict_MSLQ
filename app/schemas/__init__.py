"""Schemas y modelos Pydantic para validación"""

from .prediction import (
    PredictionRequest,
    PredictionResponse,
    StudentPredictionRequest,
    StudentPredictionResponse,
    BatchPredictionRequest,
    BatchPredictionResponse,
)

__all__ = [
    "PredictionRequest",
    "PredictionResponse",
    "StudentPredictionRequest",
    "StudentPredictionResponse",
    "BatchPredictionRequest",
    "BatchPredictionResponse",
]
