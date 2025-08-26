from abc import ABC, abstractmethod

class EmpresaExtractInterface(ABC):
    """
    Classe modelo para extração de dados.
    """

    @abstractmethod
    def get(self):
        """
        Método de extração dos dados da api
        """
        pass
