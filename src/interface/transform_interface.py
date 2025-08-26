from abc import ABC, abstractmethod

class EmpresaTransformInterface(ABC):
    """
    Interface para transformação de dados da API de empresas.
    """
    
    @abstractmethod
    def sliceJson(self, dados):
        """
        Separa o que for fields e records.
        """
        pass
