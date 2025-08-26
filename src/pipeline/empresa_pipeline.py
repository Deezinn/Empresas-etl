from src.etl import EmpresaExtract,EmpresaTransform, EmpresaLoad

class EmpresaPipeline:
    def __init__(self):
        self.__extract = EmpresaExtract()  
        self.__transform = EmpresaTransform()
        self.__load = EmpresaLoad()
    
    def run_pipeline(self):
        json_data = self.__extract.get()
        result_raw_data, result_process_data = self.__transform.sliceJson(json_data)
        self.__load.saveRawCsv(result_raw_data)
        self.__load.saveProcessCsv(result_process_data)

if __name__ == "__main__":
    eP = EmpresaPipeline()
    eP.run_pipeline()