from src.interface import EmpresaLoadInterface
import pandas as pd

class EmpresaLoad(EmpresaLoadInterface):
    def saveRawCsv(self, dadosAtivos, dadosInativos, ativosCampos,inativoCampos):
        import os
        if not os.path.exists('data/csv/raw/'):
            os.makedirs('data/csv/raw/')
        else:
            pd.DataFrame(ativosCampos).to_csv('data/csv/raw/EmpresaCampos.csv') 
            pd.DataFrame(dadosAtivos).to_csv('data/csv/raw/EmpresasAtivas.csv')  
            pd.DataFrame(dadosInativos).to_csv('data/csv/raw/EmpresasInativas.csv')
       
    
    def saveProcessCsv(self, dados):
        """
        Salva o csv com dados processados
        """
        pass