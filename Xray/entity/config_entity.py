
import os,sys
from dataclasses import dataclass
from torch import device
from Xray.constant.training_pipeline import *

@dataclass
class DataIngestionConfig:
    data_path=Data_folder
    artifacts_dir=os.path.join('artifacts',)