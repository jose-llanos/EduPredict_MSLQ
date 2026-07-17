"""
GUÍA DE INICIO - API FastAPI Edu Predict MSLQ
"""

# 🚀 BIENVENIDA

¡Hola! He creado una **API REST profesional con FastAPI** basada en tu modelo de 
clasificación de desempeño académico MSLQ.

# 📍 UBICACIÓN DEL PROYECTO

Tu proyecto FastAPI está en:
```
EduPredict_MSLQ/
```

Este directorio contiene toda la API completamente funcional.

# ⚡ INICIO RÁPIDO (3 PASOS)

## Paso 1: Instalar Dependencias
```bash
cd EduPredict_MSLQ
pip install -r requirements.txt
```

## Paso 2: Copiar Datos (IMPORTANTE)
```bash
# Los archivos CSV deben estar en la carpeta 'data'
cp ../data-model-mslq-pretest-207.csv data/
cp ../data-model-mslq-corhuila.csv data/
```

## Paso 3: Ejecutar API
```bash
python main.py
```

¡Eso es! La API estará disponible en: **http://localhost:8000**

# 📚 DOCUMENTACIÓN INTERACTIVA

Una vez que ejecutes la API, accede a:

- **Swagger UI** (interfaz interactiva): http://localhost:8000/docs
- **ReDoc** (documentación alternativa): http://localhost:8000/redoc

# 📁 ESTRUCTURA DENTRO DE EduPredict_MSLQ/

```
app/                   # Código principal
├── api/              # Endpoints REST
├── models/           # Machine Learning
├── schemas/          # Validación
├── services/         # Lógica
└── utils/            # Utilidades

main.py              # Punto de entrada
requirements.txt     # Dependencias
config.py            # Configuración
```

# 🔌 ENDPOINTS PRINCIPALES

1. **GET /api/v1/health** - Verificar que la API está activa
2. **POST /api/v1/predict** - Realizar predicción
3. **POST /api/v1/predict-student** - Predicción con nombre
4. **POST /api/v1/predict-batch** - Predicción múltiple
5. **GET /api/v1/info** - Información de la API

# 📖 ARCHIVOS DE DOCUMENTACIÓN

Dentro de `EduPredict_MSLQ/` encontrarás:

1. **README.md** - Documentación completa y detallada
2. **QUICK_START.md** - Instalación rápida
3. **ARCHITECTURE.md** - Diagramas y arquitectura
4. **EJEMPLOS_REQUESTS.md** - Ejemplos JSON de requests
5. **RESUMEN_PROYECTO.md** - Resumen del proyecto

# 🤖 MODELO Y CARACTERÍSTICAS

- **Algoritmo**: Random Forest Classifier
- **Semanas**: 4, 8, 12
- **Características**: 15-17 características MSLQ + prácticas
- **Salida**: 
  - 0 = Bajo desempeño (0.0-2.9)
  - 1 = Medio desempeño (3.0-4.0)
  - 2 = Alto desempeño (4.1-5.0)

# 🧪 PROBAR LA API

### Opción 1: Interfaz Web
1. Ejecuta `python main.py`
2. Abre http://localhost:8000/docs
3. Haz clic en "Try it out" en cualquier endpoint

### Opción 2: Script de Ejemplo
1. Ejecuta `python main.py` en una terminal
2. En otra terminal: `python example_usage.py`

### Opción 3: cURL
```bash
curl -X GET "http://localhost:8000/api/v1/health"
```

# 🐳 ALTERNATIVA: DOCKER

Si tienes Docker instalado:
```bash
docker-compose up -d
```

# 🛠️ COMANDOS ÚTILES

```bash
make install       # Instalar dependencias
make dev          # Ejecutar en desarrollo
make train        # Entrenar modelos
make test         # Ejecutar pruebas
make clean        # Limpiar archivos temporales
```

# ⚙️ CONFIGURACIÓN

Edita `.env` para cambiar:
- Puerto (default: 8000)
- Debug mode
- Rutas de datos/logs/modelos

# 📊 DATOS NECESARIOS

Coloca estos archivos en `EduPredict_MSLQ/data/`:
- `data-model-mslq-pretest-207.csv` ← para entrenar
- `data-model-mslq-corhuila.csv` ← datos de estudiantes (opcional)

# ✅ VERIFICACIÓN

Para verificar que está todo bien:

1. ✅ Instala dependencias con `pip install -r requirements.txt`
2. ✅ Copia los archivos CSV a `data/`
3. ✅ Ejecuta `python main.py`
4. ✅ Abre http://localhost:8000/docs
5. ✅ Prueba el endpoint GET /api/v1/health

Si ves una respuesta exitosa, ¡la API está funcionando! 🎉

# 🔍 SOLUCIÓN DE PROBLEMAS

### Error: "Módulo no encontrado"
```bash
pip install -r requirements.txt
```

### Error: "Puerto 8000 en uso"
```bash
# Cambiar puerto en .env
PORT=8001
```

### Error: "Archivo CSV no encontrado"
- Verifica que los CSV estén en `EduPredict_MSLQ/data/`

### Error: "Modelo no encontrado"
- Los modelos se generan automáticamente
- Revisa la carpeta `models/`

# 📞 PRÓXIMOS PASOS

1. Lee **README.md** para documentación completa
2. Revisa **ARCHITECTURE.md** para entender la estructura
3. Consulta **EJEMPLOS_REQUESTS.md** para ver ejemplos JSON
4. Integra la API en tu aplicación frontend

# 🎓 ESTRUCTURA GENERAL

```
Notebook Original (notebook en Jupyter)
           ↓
       Código extraído
           ↓
    API FastAPI (aquí) ← TÚ ESTÁS AQUÍ
           ↓
   Servir predicciones
           ↓
    Consumir desde cliente
```

# 💡 VENTAJAS DE ESTA ARQUITECTURA

✅ Escalable y profesional
✅ Fácil de mantener
✅ Bien documentada
✅ Tests listos
✅ Docker support
✅ Validación automática
✅ Documentación interactiva

# 🎯 CONCLUSIÓN

Tu API está **100% lista para usar**. Solo necesitas:

1. Copiar datos
2. Ejecutar `python main.py`
3. ¡Comenzar a hacer predicciones!

Para más detalles, consulta los archivos .md en la carpeta `EduPredict_MSLQ/`

¡Bienvenido al backend! 🚀
"""
