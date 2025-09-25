from src.interface import EmpresaTransformJsonInterface
import pandas as pd

class EmpresaTransformJson(EmpresaTransformJsonInterface):
    def __init__(self):
        self.__rawFields = None
        self.__rawRecords = None
        
        self.__rawDataframeFields = None
        self.__rawDataframeRecords = None
        
        self.__processDataframeFields = None
        self.__processDataframeRecords = None
                
    def transform(self,json_fields, json_records):
        self.__rawFields = json_fields
        self.__rawRecords = json_records
        
        self._to_dataframe()
        self._apply_column_name()
        
        # return self.__processDataframeFields, self.__processDataframeRecords
        # tirar o comentario quando o processo de tratamento for concluído
        
    def _to_dataframe(self):
        self.__rawDataframeFields = pd.DataFrame(self.__rawFields)
        self.__rawDataframeRecords = pd.DataFrame(self.__rawRecords)
        
    def _apply_column_name(self):
        if 'id' not in self.__rawDataframeFields.columns:
            raise ValueError("O JSON de campos deve conter a coluna 'id'")
        self.__rawDataframeRecords.columns = self.__rawDataframeFields['id']
        print(self.__rawDataframeRecords)
        