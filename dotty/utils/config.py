import json
from pathlib import Path

DEFAULT_CONFIG = {
    "profiles": {
        "default": {
            "jurisdiction": "CO",
            "verbosity": "info"
        },
        "caseA": {
            "jurisdiction": "CO",
            "verbosity": "debug"
        }
    }
}

def config_path():
    return Path.home() / ".dotty" / "config.json"

def ensure_config():
    path = config_path()
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=2)

def load_profile(name="default"):
    ensure_config()
    with open(config_path()) as f:
        config = json.load(f)
    return config.get("profiles", {}).get(name, config["profiles"]["default"])
