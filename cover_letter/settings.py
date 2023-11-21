import pydantic as pdt
import pydantic_settings as pds
from pathlib import Path

import yaml
class Settings(pds.BaseSettings):
    openai_api_key: str
    model:str

def load_settings():
    settings_path = Path.home()/".cover_letter"/ "settings.yaml"
    settings_yaml = yaml.load(settings_path.read_text(), Loader=yaml.FullLoader)
    return Settings(**settings_yaml)
