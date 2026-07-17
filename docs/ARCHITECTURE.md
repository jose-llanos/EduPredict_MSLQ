"""
Documento de arquitectura de la API
"""

# ARQUITECTURA DE LA API - CLASIFICACIÓN MSLQ

## 🏗️ Diagrama General

```
┌─────────────────────────────────────────────────────────────┐
│                      CLIENTE (Frontend)                      │
│                   (Web, Mobile, Desktop)                     │
└────────────────────────────┬────────────────────────────────┘
                             │ HTTP/REST
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Application                       │
│  ┌───────────────────────────────────────────────────────┐  │
│  │            API Layer (app/api/v1.py)                 │  │
│  │  - GET /health                                       │  │
│  │  - POST /predict                                     │  │
│  │  - POST /predict-student                             │  │
│  │  - POST /predict-batch                               │  │
│  │  - GET /info                                         │  │
│  └──────────────────────┬────────────────────────────────┘  │
│                         │ Pydantic Validation
│  ┌──────────────────────▼────────────────────────────────┐  │
│  │         Service Layer (prediction_service.py)        │  │
│  │  - load_all_models()                                 │  │
│  │  - predict()                                         │  │
│  │  - predict_student()                                 │  │
│  │  - batch_predict()                                   │  │
│  │  - get_performance_info()                            │  │
│  └──────────────────────┬────────────────────────────────┘  │
│                         │
│  ┌──────────────────────▼────────────────────────────────┐  │
│  │      Model Layer (model_loader.py)                   │  │
│  │  - load_training_data()                              │  │
│  │  - preprocess_data()                                 │  │
│  │  - train_model()                                     │  │
│  │  - predict()                                         │  │
│  │  - save_model()                                      │  │
│  └──────────────────────┬────────────────────────────────┘  │
└─────────────────────────┼────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   ┌────────┐      ┌────────┐      ┌──────────┐
   │ Models │      │ Data   │      │ Logs     │
   │ (PKL)  │      │ (CSV)  │      │ (TXT)    │
   └────────┘      └────────┘      └──────────┘
```

## 📁 Estructura de Capas

### 1. **API Layer** (app/api/v1.py)
   - Define todos los endpoints REST
   - Validación con Pydantic
   - Documentación automática con OpenAPI
   - Manejo de errores y códigos de estado HTTP

### 2. **Schema Layer** (app/schemas/prediction.py)
   - Modelos Pydantic para validación
   - Documentación de entrada/salida
   - Ejemplos de requests/responses

### 3. **Service Layer** (app/services/prediction_service.py)
   - Lógica de negocio
   - Orquestación de predicciones
   - Gestión de modelos en memoria
   - Cálculos y transformaciones

### 4. **Model Layer** (app/models/model_loader.py)
   - Entrenamiento de modelos ML
   - Serialización/deserialización
   - Predicciones del modelo
   - Preprocesamiento de datos

### 5. **Config Layer** (app/config.py)
   - Configuración centralizada
   - Variables de entorno
   - Parámetros de modelos

## 🔄 Flujo de Solicitud

```
1. Cliente envía POST /api/v1/predict
   ↓
2. FastAPI valida con Pydantic (PredictionRequest)
   ↓
3. Enruta a función predict()
   ↓
4. prediction_service.predict() es llamado
   ↓
5. get_model_by_week() obtiene modelo correcto
   ↓
6. model_loader.predict() ejecuta predicción
   ↓
7. prediction_service.get_performance_info() obtiene descripción
   ↓
8. Se construye PredictionResponse
   ↓
9. FastAPI retorna JSON con status 200
   ↓
10. Cliente recibe respuesta con predicción
```

## 🤖 Modelos Disponibles

```
┌──────────────────────────────────────────────┐
│         RandomForestClassifier               │
│  - Semana 4: 15 características              │
│  - Semana 8: 16 características              │
│  - Semana 12: 17 características             │
│                                              │
│  Parámetros:                                 │
│  - bootstrap=False                           │
│  - max_depth=10                              │
│  - min_samples_split=5                       │
│  - random_state=42                           │
│                                              │
│  Salida:                                     │
│  - 0: Bajo desempeño (0.0-2.9)              │
│  - 1: Medio desempeño (3.0-4.0)             │
│  - 2: Alto desempeño (4.1-5.0)              │
└──────────────────────────────────────────────┘
```

## 🔑 Características por Semana

### Semana 4 (15 características)
```
practica_1, I18, I50, I33, I38, I40, I49,
I70, I61, I24, I11, I69, I63, I71, I75
```

### Semana 8 (16 características)
```
practica_1, practica_2, I18, I50, I33, I38, I40, I49,
I70, I61, I24, I11, I69, I63, I71, I75
```

### Semana 12 (17 características)
```
practica_1, practica_2, practica_3, I18, I50, I33, I38, I40, I49,
I70, I61, I24, I11, I69, I63, I71, I75
```

## 📊 Gestión de Modelos

```
┌─────────────────────────────────────┐
│     ModelManager                    │
├─────────────────────────────────────┤
│ Responsabilidades:                  │
│ • Cargar datos de entrenamiento    │
│ • Preprocesar y balancear datos    │
│ • Entrenar modelos                 │
│ • Guardar/Cargar modelos           │
│ • Hacer predicciones               │
└─────────────────────────────────────┘
        │
        ├─ load_training_data()
        ├─ preprocess_data()
        ├─ train_model()
        ├─ save_model()
        ├─ load_model()
        └─ predict()
```

## 🔐 Seguridad y Validación

```
Entrada → Pydantic Validation → Type Checking → Range Checking → Service
```

- Validación de tipos
- Rangos de valores
- Valores por defecto
- Documentación automática

## 🚀 Escalabilidad

### Mejoras posibles:
- Caché en memoria para predicciones frecuentes
- Base de datos para historial de predicciones
- Workers multiprocess con uvicorn
- Rate limiting y autenticación
- Versionado de modelos
- A/B testing de modelos

## 🧩 Integración con clientes

```
Client → HTTP/REST → FastAPI → JSON Response

Ejemplos:
- Web Dashboard (React, Vue, Angular)
- Mobile App (iOS, Android)
- Desktop Application
- Otros servicios backend
```

## 📝 Ejemplo de Arquitectura Completa

```
┌─────────────────────────────────────────────────────┐
│  request: POST /api/v1/predict                      │
│  {                                                   │
│    "week": 4,                                        │
│    "practica_1": 4.2,                               │
│    "I11": 3.5, ... (14 características más)         │
│  }                                                   │
└──────────────────┬──────────────────────────────────┘
                   │
        ┌──────────▼──────────┐
        │  Pydantic Validation │
        │  PredictionRequest   │
        └──────────┬───────────┘
                   │
        ┌──────────▼──────────────────┐
        │  prediction_service.predict  │
        │  • get_model_by_week(4)     │
        │  • model_manager.predict()  │
        │  • get_performance_info()   │
        └──────────┬──────────────────┘
                   │
        ┌──────────▼──────────────────┐
        │  RandomForestClassifier     │
        │  .predict([features])       │
        │  → prediction = 2           │
        │  → confidence = 0.92        │
        └──────────┬──────────────────┘
                   │
        ┌──────────▼──────────────────┐
        │  PredictionResponse         │
        │  {                          │
        │    "prediction": 2,         │
        │    "performance_level": ... │
        │    "confidence_score": 0.92 │
        │  }                          │
        └──────────┬──────────────────┘
                   │
                   ▼
        HTTP 200 → Client
```

## 🔧 Configuración Centralizada

```python
settings = Settings(
    app_name="API Edu Predict MSLQ",
    debug=True,
    port=8000,
    features_week_4=[...],
    features_week_8=[...],
    features_week_12=[...],
    performance_levels={...}
)
```

"""
