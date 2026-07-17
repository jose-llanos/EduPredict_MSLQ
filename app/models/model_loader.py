"""
Cargador de modelos de Machine Learning
"""

import pickle
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

import logging

logger = logging.getLogger(__name__)


class ModelManager:
    """Gestor de modelos de Machine Learning"""
    
    def __init__(self, data_path: str, models_path: str = None):
        self.data_path = Path(data_path)
        self.models_path = Path(models_path) if models_path else Path("./models")
        self.models_path.mkdir(parents=True, exist_ok=True)
        
        self.data = None
        self.models = {}
        self.scalers = {}
        
    def load_training_data(self, csv_file: str) -> pd.DataFrame:
        """
        Carga los datos de entrenamiento desde CSV
        
        Args:
            csv_file: Nombre del archivo CSV
            
        Returns:
            DataFrame con los datos
        """
        try:
            csv_path = self.data_path / csv_file
            data = pd.read_csv(csv_path, sep=";")
            logger.info(f"Datos cargados: {data.shape}")
            return data
        except Exception as e:
            logger.error(f"Error al cargar datos: {e}")
            raise
    
    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocesa los datos (remuestreo para balancear clases)
        
        Args:
            data: DataFrame con datos originales
            
        Returns:
            DataFrame procesado
        """
        try:
            # Separar por clase
            df_bajo = data[data['final'] == 0]
            df_medio = data[data['final'] == 1]
            df_alto = data[data['final'] == 2]
            
            # Remuestreo
            data_resample_bajo = resample(
                df_bajo, 
                replace=True, 
                n_samples=87, 
                random_state=42
            )
            data_resample_alto = resample(
                df_alto, 
                replace=True, 
                n_samples=87, 
                random_state=42
            )
            
            # Concatenar
            data_balanced = pd.concat([
                data_resample_bajo, 
                df_medio, 
                data_resample_alto
            ])
            
            logger.info(f"Datos balanceados: {data_balanced['final'].value_counts().to_dict()}")
            return data_balanced
        except Exception as e:
            logger.error(f"Error en preprocesamiento: {e}")
            raise
    
    def train_model(
        self, 
        data: pd.DataFrame, 
        features: list, 
        week: int = 4
    ) -> RandomForestClassifier:
        """
        Entrena un modelo Random Forest
        
        Args:
            data: DataFrame con los datos
            features: Lista de características
            week: Número de semana (para identificar el modelo)
            
        Returns:
            Modelo entrenado
        """
        try:
            # Preparar datos
            X = data[features]
            y = data['final'].values
            
            # Split
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, 
                train_size=0.80, 
                random_state=42
            )
            
            # Crear y entrenar modelo
            model = RandomForestClassifier(
                bootstrap=False, 
                max_depth=10, 
                min_samples_split=5,
                random_state=42
            )
            model.fit(X_train, y_train)
            
            # Evaluar
            score = model.score(X_test, y_test)
            logger.info(f"Modelo Semana {week} - Accuracy: {score:.4f}")
            
            return model
        except Exception as e:
            logger.error(f"Error al entrenar modelo: {e}")
            raise
    
    def save_model(self, model, filename: str):
        """Guarda un modelo"""
        try:
            model_path = self.models_path / filename
            joblib.dump(model, model_path)
            logger.info(f"Modelo guardado: {model_path}")
        except Exception as e:
            logger.error(f"Error al guardar modelo: {e}")
            raise
    
    def load_model(self, filename: str):
        """Carga un modelo"""
        try:
            model_path = self.models_path / filename
            model = joblib.load(model_path)
            logger.info(f"Modelo cargado: {model_path}")
            return model
        except Exception as e:
            logger.error(f"Error al cargar modelo: {e}")
            raise
    
    def predict(
        self, 
        model: RandomForestClassifier, 
        features_dict: dict
    ) -> tuple:
        """
        Realiza predicción
        
        Args:
            model: Modelo entrenado
            features_dict: Diccionario con valores de características
            
        Returns:
            Tupla (predicción, probabilidades)
        """
        try:
            # Convertir a DataFrame
            X = pd.DataFrame([features_dict])
            
            # Predicción
            prediction = model.predict(X)[0]
            probabilities = model.predict_proba(X)[0]
            confidence = float(np.max(probabilities))
            
            return prediction, confidence
        except Exception as e:
            logger.error(f"Error en predicción: {e}")
            raise
