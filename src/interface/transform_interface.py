from abc import ABC, abstractmethod

class EmpresaTrasnform(ABC):
    """
    Classe modelo para transformação de dados.
    """
    @abstractmethod
    def transform(self):
        """
        Método de transformar os dados da api
        """
        pass
