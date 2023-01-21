from django.apps import AppConfig
from django.conf import settings
import os
# import keras
# import tensorflow


class ModelDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_data'
    path = os.path.join(settings.MODELS, "saved_model.pb") 
