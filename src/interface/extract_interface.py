from abc import ABC, abstractmethod

class EmpresaHTTP(ABC):
    """
    Classe modelo para extração de dados.
    """
    @abstractmethod
    def get(self):
        """
        Método de extração dos dados da api
        """
        pass
