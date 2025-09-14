from src.pipeline import EmpresaPipeline

class Main:
    def __init__(self):
        self.__pipeline = EmpresaPipeline()

    def run(self):
        EmpresaPipeline().run_pipeline()


if __name__ == "__main__":
    m = Main()
    m.run()