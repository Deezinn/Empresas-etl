from src.interface import EmpresaTransformInterface
import pandas as pd


class EmpresaTransform(EmpresaTransformInterface):
    def __init__(self):
        self.__fields = None
        self.__records = None

    def sliceJson(self, json_data):

        for k,v in json_data.items():
            if k == 'fields':
                self.__fields = v
            elif k == 'records':
                self.__records = v
            else:
                return 0
        
        return pd.DataFrame(self.__records), pd.DataFrame(self.__records)
    