import json
import os

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
