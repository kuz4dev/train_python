from game import config as cfg
import json

def load_record():
    try:
        with open(cfg.RECORD_DIR, "r", encoding='utf-8') as file:
            data = json.load(file)
                        
        return data.get("record", 0)
    except:
        return 0
        

def save_record(score):
    with open(cfg.RECORD_DIR, 'w', encoding='utf-8') as file:
        json.dump({ "record": score }, file)