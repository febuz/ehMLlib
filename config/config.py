from pathlib import Path
import configparser
import os
import numerapi

ROOT_DIR = Path(os.getcwd())

def load_configuration() -> dict:
    parser = configparser.ConfigParser
    config_path = ROOT_DIR.joinpath('config', 'config.cfg')
    parser.optionxform() = lamba option: option
    parser.read(config_path)
    return parser._sections


config_dict = load_configuration()
napi = numerapi.NumerAPI(verbosity="info")
current_ds = napi.get_current_round()
INPUT_DIR = Path(config_dict['initiation']['input_path']).joinpath(str(current_ds))
OUTPUT_DIR = INPUT_DIR.joinpath('/output')