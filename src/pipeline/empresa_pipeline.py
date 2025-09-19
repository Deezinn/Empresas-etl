from src.etl import EmpresaExtract,EmpresaTransform,EmpresaLoad
from src.utils import separatorJson, denerateDocFields

class EmpresaPipeline:
    def __init__(self):
        self.__extract = EmpresaExtract()  
        self.__transform = EmpresaTransform()
        self.__load = EmpresaLoad()
    
    def run_pipeline(self):
        json_data = self.__extract.get()
        
        # json_fields mostra cada coluna
        # json_record mostra os valores das colunas
        
        json_fields, json_records = separatorJson(json_data)
        denerateDocFields(json_fields)
        self.__transform.transform(json_fields, json_records)
        
        # self.__load.saveRawCsv(json_fields, json_records)
        # self.__load.saveProcessCsv(result_process_data)

