from src.interface import EmpresaLoadInterface

class EmpresaLoad(EmpresaLoadInterface):
    def saveRawCsv(self, dados):
        import os
        if not os.path.exists('src/datasets'):
            os.makedirs('src/datasets')
        dados.to_csv('src/datasets/rawEmpresas.csv')   
        return dados
    
    def saveProcessCsv(self, dados):
        """
        Salva o csv com dados processados
        """
        pass