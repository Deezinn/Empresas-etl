from abc import ABC, abstractmethod

class EmpresaExtractInterface(ABC):
    """
    Classe modelo para extração de dados.
    """

    @abstractmethod
    def extract_data(self):
        """
        Método orquestrador da classe EmpresaExtract
        """
        pass
    
    def __get_json_api(self):
        """
        Método de extração dos dados em json
        """
        pass
    
    def __get_csv_api(self):
        """
        Método de extração dos dados em csv
        """
        pass