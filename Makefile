.PHONY: help install dev prod train test clean docker-build docker-run

help:
	@echo "Comandos disponibles:"
	@echo "  make install      - Instalar dependencias"
	@echo "  make dev          - Ejecutar en modo desarrollo"
	@echo "  make prod         - Ejecutar en modo producción"
	@echo "  make train        - Entrenar modelos"
	@echo "  make test         - Ejecutar pruebas"
	@echo "  make clean        - Limpiar archivos temporales"
	@echo "  make docker-build - Construir imagen Docker"
	@echo "  make docker-run   - Ejecutar en Docker"

install:
	pip install -r requirements.txt

dev:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

prod:
	uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

train:
	python train_models.py

test:
	python example_usage.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

docker-build:
	docker build -t mslq-api .

docker-run:
	docker run -p 8000:8000 -v $(PWD)/data:/app/data -v $(PWD)/models:/app/models mslq-api

docker-compose-up:
	docker-compose up -d

docker-compose-down:
	docker-compose down
