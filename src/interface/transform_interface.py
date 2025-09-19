from abc import ABC, abstractmethod

class EmpresaTransformInterface(ABC):
    """
    Interface para transformação de dados da API de empresas.
    """
    
    @abstractmethod
    def transform(self,json_fields, json_records):
        """
        Transformar os dados em dataframe
        """
        pass
