from src.etl import EmpresaExtract,EmpresaAtivaTransform,EmpresaInativaTransform,EmpresaLoad
from src.utils import separatorJson, denerateDocFields
from src.interface import EmpresaPipelineInterface
from io import StringIO
import pandas as pd

class EmpresaPipeline(EmpresaPipelineInterface):
    def __init__(self):
        self.__extract = EmpresaExtract()  
        self.__transformAtiva = EmpresaAtivaTransform()
        self.__transformInativa = EmpresaInativaTransform()
        self.__load = EmpresaLoad()
    
    def run_pipeline(self):
        ativosCsv, inativosCsv = self.__extract.extract_data()
        
        # Colunas dos inativos é igual ao dos ativos
        self.__load.saveRawCsv(ativosCsv, inativosCsv)
        
        # denerateDocFields(ativosCampos)
        
        # dadosProcessadosAtivos = self.__transformAtiva.transform(ativosCampos, ativosDados)
        # dadosProcessadosInativos = self.__transformInativa.transform(inativoCampos, inativosDados)
        
        # self.__load.saveProcessCsv(result_process_data)

