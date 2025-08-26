from src.etl import EmpresaExtract, 

class EmpresaPipeline:
    def __init__(self):
        self.__extract = EmpresaExtract()  
    
    def run_pipeline(self):
        json_data = self.__extract.get()
        print(json_data)


if __name__ == "__main__":
    eP = EmpresaPipeline()
    eP.run_pipeline()