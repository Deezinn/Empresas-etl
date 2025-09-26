from src.utils.constant import DESCRICAO
import os 


def denerateDocFields(fields):
    output = 'docs/fields.txt'
    
    try:
        os.makedirs(output[:4], exist_ok=True)
    except OSError as error:
        print("Diretório não foi criado com sucesso.", error)
    else:
        if not fields:
            return
        with open(output, "w", encoding="utf-8") as f:
            f.write("Campos e seu significados com seus tipos. \n\n\n")
            for field in fields:
                fid = field['id']
                ftype = field['type']
                desc = DESCRICAO.get(fid, "Sem descrição")
                f.write(f"{fid} ({ftype}): {desc} \n \n")
