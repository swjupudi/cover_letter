import pydantic as pdt
import pydantic_settings as pds
from pathlib import Path

import yaml
class Settings(pds.BaseSettings):
    openai_api_key: str
    model:str
    resume_path: str

"""
class Settings:
    def __init__(self, openai_api_key: str, model: str, resume_path: str):
        self.openai_api_key = openai_api_keyß
        self.model = model
        self.resume_path = resume_path
"""

def load_settings() -> Settings:
    settings_path = Path.home() / ".cover_letter" / "settings.yaml"
    settings_yaml = yaml.load(settings_path.read_text(), Loader=yaml.FullLoader)
    return Settings(**settings_yaml)



if __name__ == "__main__":
    print(load_settings())