"""
Servicio de predicción
"""

from datetime import datetime
from typing import Dict, List, Tuple
from app.models.model_loader import ModelManager
from app.config import settings
import logging

logger = logging.getLogger(__name__)


class PredictionService:
    """Servicio encargado de realizar predicciones"""
    
    def __init__(self, model_manager: ModelManager):
        self.model_manager = model_manager
        self.models = {}
        self.load_all_models()
    
    def load_all_models(self):
        """Carga todos los modelos entrenados"""
        try:
            # Intentar cargar modelos existentes
            try:
                self.models['week_4'] = self.model_manager.load_model('model_week_4.pkl')
                self.models['week_8'] = self.model_manager.load_model('model_week_8.pkl')
                self.models['week_12'] = self.model_manager.load_model('model_week_12.pkl')
                logger.info("Modelos cargados desde almacenamiento")
            except FileNotFoundError:
                logger.warning("Modelos no encontrados, será necesario entrenarlos")
                self.train_all_models()
        except Exception as e:
            logger.error(f"Error al cargar modelos: {e}")
            raise
    
    def train_all_models(self):
        """Entrena todos los modelos"""
        try:
            # Cargar y preprocesar datos
            data = self.model_manager.load_training_data("data-model-mslq-pretest-207.csv")
            data = self.model_manager.preprocess_data(data)
            
            # Entrenar modelos
            model_4 = self.model_manager.train_model(
                data, 
                settings.features_week_4, 
                week=4
            )
            model_8 = self.model_manager.train_model(
                data, 
                settings.features_week_8, 
                week=8
            )
            model_12 = self.model_manager.train_model(
                data, 
                settings.features_week_12, 
                week=12
            )
            
            # Guardar modelos
            self.model_manager.save_model(model_4, 'model_week_4.pkl')
            self.model_manager.save_model(model_8, 'model_week_8.pkl')
            self.model_manager.save_model(model_12, 'model_week_12.pkl')
            
            # Almacenar en memoria
            self.models['week_4'] = model_4
            self.models['week_8'] = model_8
            self.models['week_12'] = model_12
            
            logger.info("Todos los modelos entrenados y guardados")
        except Exception as e:
            logger.error(f"Error al entrenar modelos: {e}")
            raise
    
    def get_model_by_week(self, week: int):
        """Obtiene el modelo correspondiente a la semana"""
        if week == 4:
            return self.models.get('week_4')
        elif week == 8:
            return self.models.get('week_8')
        elif week == 12:
            return self.models.get('week_12')
        else:
            raise ValueError(f"Semana no válida: {week}")
    
    def get_features_by_week(self, week: int) -> List[str]:
        """Obtiene las características según la semana"""
        if week == 4:
            return settings.features_week_4
        elif week == 8:
            return settings.features_week_8
        elif week == 12:
            return settings.features_week_12
        else:
            raise ValueError(f"Semana no válida: {week}")
    
    def predict(self, week: int, features_dict: Dict) -> Tuple[int, float]:
        """
        Realiza predicción
        
        Args:
            week: Semana de predicción
            features_dict: Diccionario con características
            
        Returns:
            Tupla (predicción, confianza)
        """
        try:
            model = self.get_model_by_week(week)
            if model is None:
                raise ValueError(f"Modelo para semana {week} no disponible")
            
            prediction, confidence = self.model_manager.predict(model, features_dict)
            return prediction, confidence
        except Exception as e:
            logger.error(f"Error en predicción: {e}")
            raise
    
    def get_performance_info(self, prediction: int) -> Tuple[str, str]:
        """
        Obtiene información del nivel de desempeño
        
        Args:
            prediction: Código de predicción (0, 1, 2)
            
        Returns:
            Tupla (nombre_nivel, rango)
        """
        performance_info = settings.performance_levels.get(prediction, {})
        return (
            performance_info.get("name", "Desconocido"),
            performance_info.get("range", "N/A")
        )
    
    def predict_student(
        self, 
        week: int, 
        student_name: str, 
        data_dict: Dict
    ) -> Dict:
        """
        Realiza predicción para un estudiante específico
        
        Args:
            week: Semana de predicción
            student_name: Nombre del estudiante
            data_dict: Datos del estudiante
            
        Returns:
            Diccionario con resultado de predicción
        """
        try:
            # Extraer características necesarias
            features = self.get_features_by_week(week)
            features_dict = {feature: data_dict.get(feature) for feature in features}
            
            # Predicción
            prediction, confidence = self.predict(week, features_dict)
            
            # Información del desempeño
            performance_level, performance_range = self.get_performance_info(prediction)
            
            return {
                "student_name": student_name,
                "prediction": int(prediction),
                "performance_level": performance_level,
                "performance_range": performance_range,
                "week": week,
                "confidence_score": round(confidence, 4),
                "prediction_date": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Error en predicción de estudiante: {e}")
            raise
    
    def batch_predict(
        self, 
        week: int, 
        students_data: List[Dict]
    ) -> Tuple[List[Dict], float]:
        """
        Realiza predicciones en lote
        
        Args:
            week: Semana de predicción
            students_data: Lista de diccionarios con datos de estudiantes
            
        Returns:
            Tupla (predicciones, tiempo_procesamiento)
        """
        import time
        
        start_time = time.time()
        predictions = []
        
        try:
            for student_data in students_data:
                student_name = student_data.pop("student_name", "Unknown")
                prediction_result = self.predict_student(week, student_name, student_data)
                predictions.append(prediction_result)
            
            processing_time = time.time() - start_time
            return predictions, processing_time
        except Exception as e:
            logger.error(f"Error en predicción en lote: {e}")
            raise
