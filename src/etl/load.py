from src.interface import EmpresaLoadInterface
import pandas as pd

class EmpresaLoad(EmpresaLoadInterface):
    def saveRawCsv(self, dadosAtivos, dadosInativos, ativosCampos,inativoCampos):
        import os
        os.makedirs('data/csv/raw/campos/', exist_ok=True)
        os.makedirs('data/csv/raw/dados/', exist_ok=True)

        pd.DataFrame(ativosCampos).to_csv('data/csv/raw/campos/EmpresaCamposAtivas.csv') 
        pd.DataFrame(inativoCampos).to_csv('data/csv/raw/campos/EmpresaCamposInativas.csv') 
        pd.DataFrame(dadosAtivos).to_csv('data/csv/raw/dados/EmpresasAtivas.csv')  
        pd.DataFrame(dadosInativos).to_csv('data/csv/raw/dados/EmpresasInativas.csv')
       
    
    def saveProcessCsv(self, dados):
        """
        Salva o csv com dados processados
        """
        pass