from src.interface.extract_interface import EmpresaExtractInterface
from src.utils.constant import APIURLCSV

import requests
from requests import HTTPError, JSONDecodeError

class EmpresaExtract(EmpresaExtractInterface):
    def __init__(self):
        self.__empresasAtivasCsv = None
        self.__empresasInativasCsv = None
        
    def extract_data(self):
        ativosCsv, inativosCsv = self.__get_csv_api()
        return ativosCsv, inativosCsv
        
    def __get_csv_api(self):
        if not APIURLCSV:
            raise ModuleNotFoundError("Não consegui acessar a constante do módulo em utils.")
        
        if APIURLCSV == {}:
            raise ValueError("Constante com valores vázios, impossível de fazer a extração.")
        try:
            for api in APIURLCSV:
                r = requests.get(api[list(api.keys())[0]])
                if r.status_code == 200:
                    if list(api.keys())[0] == 'empresaAtivaCsv':
                        self.__empresasAtivasCsv = r.text
                    if list(api.keys())[0] == 'empresaInativaCsv':
                        self.__empresasInativasCsv = r.text
            return self.__empresasAtivasCsv, self.__empresasInativasCsv
        except requests.HTTPError :
             raise HTTPError("Erro de extração de dados")
        except requests.JSONDecodeError:
             raise JSONDecodeError("Dados não vieram no formato errado. Esperado: 'JSON'")