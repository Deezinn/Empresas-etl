from src.interface import EmpresaLoadInterface
import pandas as pd

class EmpresaLoad(EmpresaLoadInterface):
    def saveRawCsv(self, campos, dados):
        import os
        if not os.path.exists('csv/raw/'):
            os.makedirs('csv/raw/')
        else:
            pd.DataFrame(dados).to_csv('csv/raw/Fields.csv')  
            pd.DataFrame(campos).to_csv('csv/raw/Empresas.csv')
        return pd.DataFrame(dados), pd.DataFrame(campos)
    
    def saveProcessCsv(self, dados):
        """
        Salva o csv com dados processados
        """
        pass