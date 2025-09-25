from abc import ABC, abstractmethod

class EmpresaPipelineInterface(ABC):
    """
    Classe modelo para a pipeline.
    """

    @abstractmethod
    def run_pipeline(self):
        """
        Método orquestrador de toda a etl
        """
        pass
    