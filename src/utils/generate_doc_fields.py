from src.constant import DESCRICAO

def denerateDocFields(fields):
    output="src/docs/fields.txt"
    
    if not fields:
        print("Não consegui achar os campos")
        return
    with open(output, "w", encoding="utf-8") as f:
        f.write("Campos e seu significados com seus tipos. \n\n\n")
        for field in fields:
            fid = field['id']
            ftype = field['type']
            desc = DESCRICAO.get(fid, "Sem descrição")
            f.write(f"{fid} ({ftype}): {desc} \n \n")
