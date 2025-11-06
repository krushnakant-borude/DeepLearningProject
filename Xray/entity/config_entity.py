
import os,sys
from dataclasses import dataclass
from torch import device
from Xray.constant.training_pipeline import *

@dataclass
class DataIngestionConfig:
    artifacts_dir=os.path.join('artifacts',TIMESTAMP)
    data_path=os.path.join(artifacts_dir,'data_ingestion',Data_folder)

    train_data_path=os.path.join(data_path,'train')
    test_data_path=os.path.join(data_path,'test')
