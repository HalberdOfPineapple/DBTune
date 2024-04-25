import json
import os

if __name__ == '__main__':
    KNOB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts', 'experiment', 'gen_knobs')
    knob_file = os.path.join(KNOB_DIR, 'JOB_shap_postgres.json')
    with open(knob_file, 'r') as f:
        knob_dict = json.load(f)
    print(knob_dict.keys())