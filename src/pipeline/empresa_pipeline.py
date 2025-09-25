from src.etl import EmpresaExtract,EmpresaTransformJson,EmpresaTransformCsv,EmpresaLoad
from src.utils import separatorJson, denerateDocFields

class EmpresaPipeline:
    def __init__(self):
        self.__extract = EmpresaExtract()  
        self.__transformJson = EmpresaTransformJson()
        self.__transformCsv = EmpresaTransformCsv()
        # self.__load = EmpresaLoad()
    
    def run_pipeline(self):
        ativosJson, inativosJson, ativosCsv, inativosCsv = self.__extract.extract_data()
        
        ativosCampos, ativosDados = separatorJson(ativosJson)
        inativoCampos, inativosDados = separatorJson(inativosJson)
        # Campos dos inativos é igual ao dos ativos
        
        denerateDocFields(ativosCampos)
        
        self.__transformJson.transform(ativosCampos, ativosDados)
        self.__transformCsv.transform(inativoCampos, inativosDados)
        
        # self.__load.saveRawCsv(json_fields, json_records)
        # self.__load.saveProcessCsv(result_process_data)

