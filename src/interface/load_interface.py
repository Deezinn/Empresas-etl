from abc import ABC, abstractmethod

class EmpresaLoadInterface(ABC):
    """
    Interface para carregar de dados da API de empresas.
    """
    
    @abstractmethod
    def saveRawCsv(self, dados):
        """
        Salva o csv com dados não processados
        """
        pass
    
    @abstractmethod
    def saveProcessCsv(self, dados):
        """
        Salva o csv com dados processados
        """
        pass