"""
This file contains functions that are used to manage installed vosk models
and to install new vosk models.
"""

from shutil import move
from os import listdir
from requests import get
from pathlib import Path
from vosk import Model


def download_vosk_model(model_name) -> None:
    """
    Firstly, checks whether the model has been downloaded. If exists, function warns about it.
    If not downloaded, function downloads model using built-in vosk functions and then transfers it to a .model folder.
    """
    if model_name in listdir(Path(".") / ".models"):
        print(f"{model_name} already exists")
    else:
        Model(model_name=model_name)
        move(Path.home() / f".cache/vosk/{model_name}", Path(".") / ".models")

def show_downloaded_models() -> str:
    """
    Shows installed functions. It compares the names of the models in the folder .models
    with list of functions from the https://alphacephei.com/vosk/models/model-list.json website.
    """
    models = ""
    response = get("https://alphacephei.com/vosk/models/model-list.json", timeout=10)
    for model in response.json():
        if model["name"] in listdir(Path(".") / ".models"):
            models += model["name"] + "\n"
    return models
