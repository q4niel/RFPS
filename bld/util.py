import os
import tomllib

def setup() -> None:
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def loadCfg() -> dict:
    with open("bld/cfg.toml", "rb") as file:
        return tomllib.load(file)