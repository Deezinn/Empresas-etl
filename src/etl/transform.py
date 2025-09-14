from src.interface import EmpresaTransformInterface
import pandas as pd

class EmpresaTransform(EmpresaTransformInterface):
    def __init__(self):
        pass
    
    def transformDataframe(self,json_fields, json_records):
        print(json_fields)
        print(json_records)