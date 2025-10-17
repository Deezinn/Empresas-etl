from abc import ABC, abstractmethod

class EmpresaInativaTransformInterface(ABC):
    """
    Interface para transformação de dados da API de empresas.
    """
    
    @abstractmethod
    def transform(self, inativosCsv):
        """
        Processar os dados (atuará como orquestrador)
        """
        pass
    
    @abstractmethod
    def __transform_to_dataframe():
        """
        Transformar em dataframe os dados de empresas Inativas
        """
        pass