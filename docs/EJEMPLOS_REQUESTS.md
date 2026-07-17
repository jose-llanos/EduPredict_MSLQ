"""
EJEMPLOS DE REQUESTS - API Classification MSLQ
Guía de referencia rápida para cada endpoint
"""

# ════════════════════════════════════════════════════════════════
# 1. HEALTH CHECK
# ════════════════════════════════════════════════════════════════

GET /api/v1/health

Response (200):
{
  "status": "healthy",
  "app": "API Edu Predict MSLQ",
  "version": "1.0.0"
}


# ════════════════════════════════════════════════════════════════
# 2. INFORMACIÓN DE LA API
# ════════════════════════════════════════════════════════════════

GET /api/v1/info

Response (200):
{
  "app_name": "API Edu Predict MSLQ",
  "version": "1.0.0",
  "description": "API para predicción de desempeño académico...",
  "available_weeks": [4, 8, 12],
  "performance_levels": {
    "0": {"name": "Bajo desempeño", "range": "0.0 - 2.9"},
    "1": {"name": "Medio desempeño", "range": "3.0 - 4.0"},
    "2": {"name": "Alto desempeño", "range": "4.1 - 5.0"}
  },
  "features": {
    "week_4": ["practica_1", "I18", ...],
    "week_8": ["practica_1", "practica_2", ...],
    "week_12": ["practica_1", "practica_2", "practica_3", ...]
  }
}


# ════════════════════════════════════════════════════════════════
# 3. PREDICCIÓN INDIVIDUAL - SEMANA 4
# ════════════════════════════════════════════════════════════════

POST /api/v1/predict
Content-Type: application/json

Request:
{
  "week": 4,
  "practica_1": 4.2,
  "practica_2": null,
  "practica_3": null,
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

Response (200):
{
  "prediction": 2,
  "performance_level": "Alto desempeño",
  "performance_range": "4.1 - 5.0",
  "week": 4,
  "confidence_score": 0.85
}


# ════════════════════════════════════════════════════════════════
# 4. PREDICCIÓN INDIVIDUAL - SEMANA 8
# ════════════════════════════════════════════════════════════════

POST /api/v1/predict
Content-Type: application/json

Request:
{
  "week": 8,
  "practica_1": 4.2,
  "practica_2": 3.9,
  "practica_3": null,
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

Response (200):
{
  "prediction": 2,
  "performance_level": "Alto desempeño",
  "performance_range": "4.1 - 5.0",
  "week": 8,
  "confidence_score": 0.89
}


# ════════════════════════════════════════════════════════════════
# 5. PREDICCIÓN INDIVIDUAL - SEMANA 12
# ════════════════════════════════════════════════════════════════

POST /api/v1/predict
Content-Type: application/json

Request:
{
  "week": 12,
  "practica_1": 4.2,
  "practica_2": 3.9,
  "practica_3": 4.1,
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

Response (200):
{
  "prediction": 2,
  "performance_level": "Alto desempeño",
  "performance_range": "4.1 - 5.0",
  "week": 12,
  "confidence_score": 0.92
}


# ════════════════════════════════════════════════════════════════
# 6. PREDICCIÓN CON NOMBRE DE ESTUDIANTE
# ════════════════════════════════════════════════════════════════

POST /api/v1/predict-student
Content-Type: application/json

Request:
{
  "student_name": "Juan Pérez García",
  "week": 4,
  "corte_1": 4.2,
  "corte_2": null,
  "corte_3": null,
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

Response (200):
{
  "student_name": "Juan Pérez García",
  "prediction": 2,
  "performance_level": "Alto desempeño",
  "performance_range": "4.1 - 5.0",
  "week": 4,
  "confidence_score": 0.85,
  "prediction_date": "2024-01-15T10:30:45.123456"
}


# ════════════════════════════════════════════════════════════════
# 7. PREDICCIÓN EN LOTE (MÚLTIPLES ESTUDIANTES)
# ════════════════════════════════════════════════════════════════

POST /api/v1/predict-batch
Content-Type: application/json

Request:
{
  "week": 4,
  "predictions": [
    {
      "student_name": "Juan Pérez",
      "corte_1": 4.2,
      "corte_2": null,
      "corte_3": null,
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
    },
    {
      "student_name": "María García",
      "corte_1": 3.2,
      "corte_2": null,
      "corte_3": null,
      "I11": 2.8,
      "I18": 3.0,
      "I24": 2.9,
      "I33": 3.1,
      "I38": 2.9,
      "I40": 3.2,
      "I49": 2.7,
      "I50": 3.0,
      "I61": 2.6,
      "I63": 2.9,
      "I69": 3.1,
      "I70": 3.0,
      "I71": 2.8,
      "I75": 3.2
    },
    {
      "student_name": "Carlos López",
      "corte_1": 2.5,
      "corte_2": null,
      "corte_3": null,
      "I11": 2.0,
      "I18": 2.2,
      "I24": 2.1,
      "I33": 2.3,
      "I38": 2.2,
      "I40": 2.4,
      "I49": 2.0,
      "I50": 2.2,
      "I61": 1.9,
      "I63": 2.2,
      "I69": 2.3,
      "I70": 2.2,
      "I71": 2.1,
      "I75": 2.4
    }
  ]
}

Response (200):
{
  "total_predictions": 3,
  "predictions": [
    {
      "student_name": "Juan Pérez",
      "prediction": 2,
      "performance_level": "Alto desempeño",
      "performance_range": "4.1 - 5.0",
      "week": 4,
      "confidence_score": 0.85,
      "prediction_date": "2024-01-15T10:30:45.123456"
    },
    {
      "student_name": "María García",
      "prediction": 1,
      "performance_level": "Medio desempeño",
      "performance_range": "3.0 - 4.0",
      "week": 4,
      "confidence_score": 0.78,
      "prediction_date": "2024-01-15T10:30:45.234567"
    },
    {
      "student_name": "Carlos López",
      "prediction": 0,
      "performance_level": "Bajo desempeño",
      "performance_range": "0.0 - 2.9",
      "week": 4,
      "confidence_score": 0.82,
      "prediction_date": "2024-01-15T10:30:45.345678"
    }
  ],
  "processing_time": 0.234
}


# ════════════════════════════════════════════════════════════════
# CÓDIGOS DE RESPUESTA
# ════════════════════════════════════════════════════════════════

200 OK
- Predicción exitosa

400 Bad Request
- Datos inválidos o semana fuera de rango

422 Unprocessable Entity
- Validación fallida de datos

500 Internal Server Error
- Error interno del servidor

# ════════════════════════════════════════════════════════════════
# EJEMPLOS CON CURL
# ════════════════════════════════════════════════════════════════

# Health check
curl -X GET "http://localhost:8000/api/v1/health"

# Obtener info
curl -X GET "http://localhost:8000/api/v1/info"

# Predicción
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "week": 4,
    "practica_1": 4.2,
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
  }'

# ════════════════════════════════════════════════════════════════
# EJEMPLOS CON PYTHON (requests)
# ════════════════════════════════════════════════════════════════

import requests

BASE_URL = "http://localhost:8000/api/v1"

# Health
response = requests.get(f"{BASE_URL}/health")
print(response.json())

# Predicción
data = {
    "week": 4,
    "practica_1": 4.2,
    "I11": 3.5,
    # ... resto de características
}
response = requests.post(f"{BASE_URL}/predict", json=data)
print(response.json())

# ════════════════════════════════════════════════════════════════
# NOTAS IMPORTANTES
# ════════════════════════════════════════════════════════════════

1. Las semanas válidas son: 4, 8, 12
   - Semana 4: Solo practica_1
   - Semana 8: practica_1 y practica_2
   - Semana 12: practica_1, practica_2 y practica_3

2. Las características MSLQ son obligatorias

3. Los valores pueden ser decimales (float)

4. null es válido para prácticas no disponibles

5. confidence_score oscila entre 0 y 1

6. La API es stateless (sin estado)

7. Todos los endpoints retornan JSON
"""
