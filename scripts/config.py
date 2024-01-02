import tomli, tomli_w
import scripts.state as state
from typing import *
from dataclasses import dataclass


@dataclass
class ConfigEndpoint:
    url: str
    api_key: Optional[str]


@dataclass
class ConfigParameters:
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float


@dataclass
class Config:
    endpoint: ConfigEndpoint
    parameters: ConfigParameters


class MostimaConfig:
    config_path: str

    def __init__(self, config_path: str):
        self.config_path = config_path
        with open(config_path, "rb") as f:
            state.config = tomli.load(f)

    def get(self) -> Config:
        return state.config

    def update_config(self):
        with open(self.config_path, "wb") as f:
            tomli_w.dump(state.config, f)
