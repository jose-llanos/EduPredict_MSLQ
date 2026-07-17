# 🎓 EduPredict MSLQ - FastAPI

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 📋 Descripción General

API REST profesional desarrollada con **FastAPI** para la predicción de desempeño académico de estudiantes basada en:

- 📊 **Cuestionario MSLQ** (Motivated Strategies for Learning Questionnaire)
- 📈 **Calificaciones de prácticas** (Cortes 1, 2 y 3)
- 🤖 **Modelo Random Forest** entrenado y optimizado

La API realiza predicciones en tres momentos del semestre:
- **Semana 4**: Con calificación de práctica 1 (15 características)
- **Semana 8**: Con calificaciones de prácticas 1 y 2 (16 características)
- **Semana 12**: Con calificaciones de prácticas 1, 2 y 3 (17 características)

## 🎯 Clasificación de Desempeño

El modelo clasifica el desempeño en tres niveles basados en el promedio académico:

| Código | Nivel | Rango de Calificación |
|--------|-------|----------------------|
| 0 | 🔴 Bajo desempeño | 0.0 - 2.9 |
| 1 | 🟡 Medio desempeño | 3.0 - 4.0 |
| 2 | 🟢 Alto desempeño | 4.1 - 5.0 |

---

## ⚡ Inicio Rápido (3 Pasos)

### Paso 1: Instalar Dependencias

```bash
cd EduPredict_MSLQ
pip install -r requirements.txt
```

### Paso 2: Copiar Datos de Entrenamiento

```bash
# Los archivos CSV deben estar en la carpeta 'data/'
cp ../data-model-mslq-pretest-207.csv data/
cp ../data-model-mslq-corhuila.csv data/
```

### Paso 3: Ejecutar la API

```bash
python main.py
```

¡Eso es! La API estará disponible en: **http://localhost:8000**

### Verificar que está funcionando

Abre en tu navegador:
- **Swagger UI** (interfaz interactiva): http://localhost:8000/docs
- **ReDoc** (documentación alternativa): http://localhost:8000/redoc

---

## 📦 Instalación Detallada

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional)

### Pasos de Instalación

#### 1. Crear entorno virtual

```bash
python -m venv venv

# Activar el entorno virtual
# En macOS/Linux:
source venv/bin/activate

# En Windows:
venv\Scripts\activate
```

#### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

#### 3. Copiar archivos de datos

Los archivos CSV de entrenamiento deben estar en la carpeta `data/`:

```bash
data/
├── data-model-mslq-pretest-207.csv    # Datos de entrenamiento
└── data-model-mslq-corhuila.csv       # Datos adicionales (opcional)
```

#### 4. Ejecutar la aplicación

```bash
python main.py
```

O usando uvicorn directamente:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🔌 Endpoints Disponibles

### 1. Health Check - Verificar que la API está activa

```http
GET /api/v1/health
```

**Respuesta (200):**
```json
{
  "status": "healthy",
  "app": "API Edu Predict MSLQ",
  "version": "1.0.0"
}
```

---

### 2. Información General - Obtener detalles de la API

```http
GET /api/v1/info
```

**Respuesta (200):**
```json
{
  "app_name": "API Edu Predict MSLQ",
  "version": "1.0.0",
  "description": "API para predicción de desempeño académico...",
  "available_weeks": [4, 8, 12],
  "performance_levels": {
    "0": {"name": "Bajo desempeño", "range": "0.0 - 2.9"},
    "1": {"name": "Medio desempeño", "range": "3.0 - 4.0"},
    "2": {"name": "Alto desempeño", "range": "4.1 - 5.0"}
  }
}
```

---

### 3. Predicción Individual - Realizar una predicción

```http
POST /api/v1/predict
Content-Type: application/json
```

#### Parámetros por Semana

**Semana 4** (15 características):
```json
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
```

**Semana 8** (16 características):
```json
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
```

**Semana 12** (17 características):
```json
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
```

**Respuesta (200):**
```json
{
  "prediction": 2,
  "performance_level": "Alto desempeño",
  "performance_range": "4.1 - 5.0",
  "week": 4,
  "confidence_score": 0.85
}
```

---

### 4. Predicción con Nombre de Estudiante

```http
POST /api/v1/predict-student
Content-Type: application/json
```

**Request:**
```json
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
```

**Respuesta (200):**
```json
{
  "student_name": "Juan Pérez García",
  "prediction": 2,
  "performance_level": "Alto desempeño",
  "performance_range": "4.1 - 5.0",
  "week": 4,
  "confidence_score": 0.85,
  "prediction_date": "2026-01-15T10:30:45.123456"
}
```

---

### 5. Predicción por Lotes

```http
POST /api/v1/predict-batch
Content-Type: application/json
```

**Request:**
```json
{
  "week": 4,
  "predictions": [
    {
      "student_name": "Juan Pérez",
      "practica_1": 4.2,
      "I11": 3.5,
      "I18": 4.0
    },
    {
      "student_name": "María López",
      "practica_1": 3.8,
      "I11": 3.2,
      "I18": 3.9
    }
  ]
}
```

**Respuesta (200):**
```json
{
  "total_predictions": 2,
  "results": [
    {
      "student_name": "Juan Pérez",
      "prediction": 2,
      "performance_level": "Alto desempeño",
      "confidence_score": 0.85
    },
    {
      "student_name": "María López",
      "prediction": 1,
      "performance_level": "Medio desempeño",
      "confidence_score": 0.78
    }
  ]
}
```

---

## 🏗️ Arquitectura

### Diagrama de Capas

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
│  │  - GET /health, /info                                │  │
│  │  - POST /predict, /predict-student, /predict-batch   │  │
│  └──────────────────────┬────────────────────────────────┘  │
│                         │ Pydantic Validation
│  ┌──────────────────────▼────────────────────────────────┐  │
│  │         Service Layer (prediction_service.py)        │  │
│  │  - load_all_models()                                 │  │
│  │  - predict() / predict_student() / batch_predict()  │  │
│  │  - get_performance_info()                            │  │
│  └──────────────────────┬────────────────────────────────┘  │
│                         │
│  ┌──────────────────────▼────────────────────────────────┐  │
│  │      Model Layer (model_loader.py)                   │  │
│  │  - load_training_data()                              │  │
│  │  - preprocess_data()                                 │  │
│  │  - train_model() / predict()                         │  │
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

### Estructura de Carpetas

```
EduPredict_MSLQ/
│
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1.py                    # Endpoints REST
│   ├── models/
│   │   ├── __init__.py
│   │   └── model_loader.py          # Carga y entrenamiento de modelos
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── prediction.py            # Validación con Pydantic
│   ├── services/
│   │   ├── __init__.py
│   │   └── prediction_service.py    # Lógica de negocio
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py                # Logging
│   └── config.py                    # Configuración centralizada
│
├── data/                            # Archivos CSV de entrenamiento
│   ├── data-model-mslq-pretest-207.csv
│   └── data-model-mslq-corhuila.csv
│
├── models/                          # Modelos entrenados (.pkl)
│
├── logs/                            # Archivos de log
│
├── docs/                            # Documentación
│   ├── ARCHITECTURE.md              # Arquitectura detallada
│   ├── INICIO_RAPIDO_API.md         # Guía rápida
│   ├── EJEMPLOS_REQUESTS.md         # Ejemplos de requests
│   └── RESUMEN_PROYECTO.md
│
├── main.py                          # Punto de entrada
├── requirements.txt                 # Dependencias
├── Dockerfile                       # Configuración Docker
├── docker-compose.yml               # Orquestación Docker
├── Makefile                         # Comandos útiles
├── .env                             # Variables de entorno
├── .gitignore
└── README.md                        # Este archivo
```

### Flujo de Solicitud

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

---

## 🤖 Modelo Machine Learning

### Algoritmo: Random Forest Classifier

**Parámetros de Configuración:**
- `bootstrap=False`
- `max_depth=10`
- `min_samples_split=5`
- `random_state=42`

### Características por Semana

#### Semana 4 (15 características)
```
practica_1, I18, I50, I33, I38, I40, I49,
I70, I61, I24, I11, I69, I63, I71, I75
```

#### Semana 8 (16 características)
```
practica_1, practica_2, I18, I50, I33, I38, I40, I49,
I70, I61, I24, I11, I69, I63, I71, I75
```

#### Semana 12 (17 características)
```
practica_1, practica_2, practica_3, I18, I50, I33, I38, I40, I49,
I70, I61, I24, I11, I69, I63, I71, I75
```

---

## 🛠️ Comandos Útiles

### Con Makefile

```bash
make install       # Instalar dependencias
make dev          # Ejecutar en modo desarrollo
make train        # Entrenar modelos
make test         # Ejecutar pruebas
make clean        # Limpiar archivos temporales
make format       # Formatear código con Black
make lint         # Verificar código con Pylint
```

### Sin Makefile

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python main.py

# Ejecutar con uvicorn (modo recarga)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Entrenar modelos
python train_models.py

# Ejecutar pruebas
pytest

# Generar documentación
python generate_pdf_docs.py
python generate_word_manual.py
```

---

## 🐳 Docker (Alternativa)

Si tienes Docker instalado, puedes ejecutar la API en un contenedor:

### Opción 1: Docker Compose (Recomendado)

```bash
docker-compose up -d
```

La API estará disponible en: **http://localhost:8000**

### Opción 2: Docker Build Manual

```bash
# Construir imagen
docker build -t api-mslq .

# Ejecutar contenedor
docker run -p 8000:8000 api-mslq
```

---

## ✅ Verificación de Instalación

Para verificar que está todo funcionando correctamente:

1. ✅ Instala dependencias: `pip install -r requirements.txt`
2. ✅ Copia los archivos CSV a `data/`
3. ✅ Ejecuta: `python main.py`
4. ✅ Abre: http://localhost:8000/docs
5. ✅ Prueba el endpoint: GET /api/v1/health

Si ves una respuesta exitosa, ¡la API está funcionando! 🎉

---

## 🔍 Solución de Problemas

### Error: "Módulo no encontrado"

```bash
pip install -r requirements.txt
```

Asegúrate de haber activado el entorno virtual.

### Error: "Puerto 8000 en uso"

Opción 1: Cambiar el puerto en `.env`:
```
PORT=8001
```

Opción 2: Matar el proceso que usa el puerto:
```bash
# macOS/Linux
lsof -i :8000
kill -9 <PID>

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Error: "Archivo CSV no encontrado"

- Verifica que los archivos CSV estén en `EduPredict_MSLQ/data/`
- Comprueba los nombres de archivo: 
  - `data-model-mslq-pretest-207.csv`
  - `data-model-mslq-corhuila.csv`

### Error: "Modelo no encontrado"

- Los modelos se generan automáticamente al ejecutar `python main.py`
- Revisa la carpeta `models/` para ver si hay archivos `.pkl`
- Verifica los logs en `logs/` para más detalles

### Error: "ModuleNotFoundError: No module named 'app'"

Asegúrate de ejecutar el comando desde la carpeta `EduPredict_MSLQ/`:

```bash
cd EduPredict_MSLQ
python main.py
```

---

## 📖 Documentación Adicional

La documentación adicional está disponible en la carpeta `docs/`:

1. **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Arquitectura detallada, diagramas y flujos
2. **[INICIO_RAPIDO_API.md](docs/INICIO_RAPIDO_API.md)** - Guía de inicio rápido paso a paso
3. **[EJEMPLOS_REQUESTS.md](docs/EJEMPLOS_REQUESTS.md)** - Ejemplos completos de requests y responses

## 📊 Características Principales

✅ **Arquitectura escalable** - Capas bien separadas (API, Service, Model)
✅ **Validación automática** - Con Pydantic y modelos bien tipados
✅ **Documentación interactiva** - Swagger UI y ReDoc integrados
✅ **Predicciones en múltiples semanas** - Semanas 4, 8 y 12
✅ **Batch predictions** - Procesar múltiples estudiantes
✅ **Modelos preentrenados** - Random Forest Classifier optimizado
✅ **Manejo de errores** - Respuestas de error consistentes
✅ **Logging completo** - Rastreo de operaciones
✅ **Docker support** - Despliegue fácil en contenedores
✅ **Tests listos** - Ejemplos de pruebas unitarias

---

## 🚀 Próximos Pasos

1. Ejecuta la API con `python main.py`
2. Explora la documentación en http://localhost:8000/docs
3. Prueba los endpoints con el botón "Try it out"
4. Integra la API en tu aplicación frontend
5. Lee la documentación adicional en la carpeta `docs/`

---

## 💡 Integración con Clientes

### Desde JavaScript/TypeScript

```javascript
const response = await fetch('http://localhost:8000/api/v1/predict', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    week: 4,
    practica_1: 4.2,
    I11: 3.5,
    I18: 4.0,
    // ... resto de características
  })
});

const prediction = await response.json();
console.log(prediction.performance_level);
```

### Desde Python

```python
import requests

response = requests.post('http://localhost:8000/api/v1/predict', json={
    'week': 4,
    'practica_1': 4.2,
    'I11': 3.5,
    'I18': 4.0,
    # ... resto de características
})

prediction = response.json()
print(prediction['performance_level'])
```

### Desde cURL

```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "week": 4,
    "practica_1": 4.2,
    "I11": 3.5,
    "I18": 4.0
  }'
```

---

## ⚙️ Configuración Avanzada

### Variables de Entorno (.env)

```bash
# Puerto de ejecución
PORT=8000

# Modo debug
DEBUG=True

# Rutas de datos
DATA_PATH=./data
MODELS_PATH=./models
LOGS_PATH=./logs

# Configuración de logging
LOG_LEVEL=INFO
```

### Cambiar Modelos o Datos

1. Coloca nuevos archivos CSV en `data/`
2. Ejecuta: `python train_models.py`
3. Los nuevos modelos se guardarán en `models/`

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 📞 Soporte

Para preguntas o problemas:
- Revisa la sección de "Solución de Problemas"
- Consulta la documentación en `docs/`
- Abre un issue en el repositorio

---

## 🎯 Resumen

Esta API REST profesional te permite:

- ✅ Obtener predicciones de desempeño académico
- ✅ Integrar predicciones en aplicaciones web o móviles
- ✅ Procesar predicciones en lotes
- ✅ Acceder a documentación interactiva
- ✅ Escalar según tus necesidades

¡Comienza ahora mismo con los 3 pasos de inicio rápido! 🚀

---

**Última actualización:** Julio 2026
**Versión:** 1.0.0
| I24    | Característica MSLQ 24 |
| I33    | Característica MSLQ 33 |
| I38    | Característica MSLQ 38 |
| I40    | Característica MSLQ 40 |
| I49    | Característica MSLQ 49 |
| I50    | Característica MSLQ 50 |
| I61    | Característica MSLQ 61 |
| I63    | Característica MSLQ 63 |
| I69    | Característica MSLQ 69 |
| I70    | Característica MSLQ 70 |
| I71    | Característica MSLQ 71 |
| I75    | Característica MSLQ 75 |
| Práctica 1/2/3 | Calificaciones de cortes |

## 🤖 Modelo Machine Learning

- **Algoritmo**: Random Forest Classifier
- **Parámetros**: 
  - bootstrap=False
  - max_depth=10
  - min_samples_split=5
- **División de datos**: 80% entrenamiento, 20% validación
- **Balanceo de clases**: Resample para equilibrar distribución

## 📝 Ejemplo de Uso con cURL

```bash
# Predicción individual
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
```

## 🧪 Testing

```bash
# Ejecutar tests
pytest tests/

# Con cobertura
pytest --cov=app tests/
```

## 📋 Requisitos del Sistema

- Python 3.8+
- pip o conda
- 200MB de espacio en disco (aproximadamente)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo `LICENSE` para más detalles.

## 📧 Contacto

Para reportar issues o sugerencias, contacta al equipo de desarrollo.

## 🎓 Créditos

- **CORHUILA**: Institución académica
- **Modelo MSLQ**: Motivated Strategies for Learning Questionnaire
- **Framework**: FastAPI

---

**Versión**: 1.0.0  
**Última actualización**: 2026
