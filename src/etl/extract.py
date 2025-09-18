from src.interface.extract_interface import EmpresaExtractInterface
from src.utils.constant import APIURL

from requests import HTTPError, JSONDecodeError
import requests

class EmpresaExtract(EmpresaExtractInterface):
    def __init__(self):
        self.__jsonData = None

    def get(self):
        if not APIURL:
            raise FileNotFoundError("Não consegui achar o link da api no arquivo de constantes.")
        if APIURL == {}:
            raise ValueError("Constante com os valores vázio, impossível fazer extração.")
        try:
            r = requests.get(APIURL['empresas'])
            r.raise_for_status()
            if r.status_code == 200:
                self.__jsonData = r.json()
            return self.__jsonData
        except requests.HTTPError :
            raise HTTPError("Erro de extração de dados")
        except requests.JSONDecodeError:
            raise JSONDecodeError("Dados não vieram no formato errado. Esperado: 'JSON'")
