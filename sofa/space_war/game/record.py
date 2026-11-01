import json
from configuration import config as cfg


def load():
    try:
        with open(cfg.RECORD_DIR, "r", encoding="utf-8") as file:
            count = json.load(file)

            return count.get("count", 0)
    except:
        return 0
    
def save(score):
    with open(cfg.RECORD_DIR, "w", encoding="utf-8") as file:
        json.dump({"count": score}, file)