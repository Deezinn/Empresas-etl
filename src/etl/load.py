from src.interface import EmpresaLoadInterface
import pandas as pd

class EmpresaLoad(EmpresaLoadInterface):
    def saveRawCsv(self, campos, dados):
        import os
        if not os.path.exists('data/csv/raw/'):
            os.makedirs('data/csv/raw/')
        else:
            pd.DataFrame(campos).to_csv('data/csv/raw/Fields.csv')  
            pd.DataFrame(dados).to_csv('data/csv/raw/Empresas.csv')
        return pd.DataFrame(dados), pd.DataFrame(campos)
    
    def saveProcessCsv(self, dados):
        """
        Salva o csv com dados processados
        """
        pass