#!/bin/bash
# Script rápido para servir documentación ReDoc

echo "╔════════════════════════════════════════════════════════════╗"
echo "║          📚 Iniciando Servidor de Documentación             ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Verificar que estamos en la carpeta correcta
if [ ! -f "serve_docs.py" ]; then
    echo "❌ Error: Este script debe ejecutarse desde la carpeta EduPredict_MSLQ"
    exit 1
fi

echo "🚀 Iniciando servidor..."
python3 serve_docs.py
