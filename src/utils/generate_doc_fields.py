from src.utils.constant import DESCRICAO
import pandas as pd
from io import StringIO
import os 


def generateDocFields(dados):
    output = 'docs/campos.txt'
    
    try:
        os.makedirs(output[:4], exist_ok=True)
    except OSError as error:
        print("Diretório não foi criado com sucesso.", error)
    else:
        if not dados:
            return
        dataframe_name_columns = pd.read_csv(
            StringIO(dados),
            sep=';',
            dtype=str,
            encoding='utf-8-sig',
            low_memory=False
        ).columns
        
        with open(output, "w", encoding="utf-8") as f:
             f.write("Campos e significados: \n\n\n")
             for field in dataframe_name_columns:
                f.write(f"Campo -> {field},\n significado:{DESCRICAO[field]} \n \n")
