from src.interface import EmpresaLoadInterface
from io import StringIO
import pandas as pd

class EmpresaLoad(EmpresaLoadInterface):
    def saveRawCsv(self,ativosCsv, inativosCsv):
        import os
        os.makedirs('data/csv/raw/dados/', exist_ok=True)
        df_raw_ativos = pd.read_csv(StringIO(ativosCsv), sep=';', low_memory=False)
        df_raw_inativos = pd.read_csv(StringIO(inativosCsv), sep=';', low_memory=False)
        
        df_raw_ativos.to_csv('data/csv/raw/dados/EmpresaAtivas.csv') 
        df_raw_inativos.to_csv('data/csv/raw/dados/EmpresaInativas.csv') 

    def saveProcessCsv(self, dados):
        """
        Salva o csv com dados processados
        """
        pass