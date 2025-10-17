from src.interface import EmpresaAtivaTransformInterface
from io import StringIO
import pandas as pd

class EmpresaInativaTransform(EmpresaAtivaTransformInterface):
    def __init__(self):
        self.__raw_inativas = None
        self.__df = None
        self.__text_default = 'Não informado'
        
    def transform(self, inativosCsv):
        self.__raw_inativas = inativosCsv
        self.__transform_to_dataframe()
        self.__rename_columns()
        self.__transform_cnpj_column()
        self.__transform_razao_social_column()
        self.__transform_nome_fantasia_column()
        self.__transform_cod_logradouro_column()
        self.__transform_nome_logradouro()
        self.__transform_numero_residencia_column()
        self.__transform__numero_lote_column()
        self.__transform_cod_bairro_column()
        self.__transform_nome_bairro_column()
        self.__transform_situacao_empresa_column()
        
    def __transform_to_dataframe(self):
        self.__df = pd.read_csv(
            StringIO(self.__raw_inativas),
            sep=';',
            dtype=str,
            encoding='utf-8-sig' 
        )
        
    def __rename_columns(self):
        self.__df.rename({'ï»¿cnpj': 'cnpj'}, axis=1, inplace=True)
        return self.__df
        
    def __transform_cnpj_column(self):
        cnpj_invalidos = self.__df['cnpj'].str.contains(r'[^0-9]', na=False)
        self.__df = self.__df[~cnpj_invalidos]
        return self.__df

    def __transform_razao_social_column(self):
        self.__df['razao_social'] = self.__df['razao_social'].replace({'.': self.__text_default})
        self.__df['razao_social'] = self.__df['razao_social'].fillna(self.__text_default)
        self.__df['razao_social'] = self.__df['razao_social'].str.title()
        return self.__df
    
    def __transform_nome_fantasia_column(self):
        self.__df['nome_fantasia'] = self.__df['nome_fantasia'].replace({'.': self.__text_default})
        self.__df['nome_fantasia'] = self.__df['nome_fantasia'].fillna(self.__text_default)
        self.__df['nome_fantasia'] = self.__df['nome_fantasia'].str.title()
        return self.__df
    
    def __transform_cod_logradouro_column(self):
        self.__df['cod_logradouro'] = self.__df['cod_logradouro'].fillna(self.__text_default)
        return self.__df
    
    def __transform_nome_logradouro(self):
        self.__df['nome_logradouro'] = self.__df['nome_logradouro'].fillna(self.__text_default)
        return self.__df
    
    def __transform_numero_residencia_column(self):
        self.__df['numero_residencia'] = self.__df['numero_residencia'].fillna(self.__text_default)
        return self.__df
    
    def __transform__numero_lote_column(self):
        self.__df['numero_lote'] = self.__df['numero_lote'].fillna(self.__text_default)
        return self.__df
    
    def __transform_cod_bairro_column(self):
        self.__df['cod_bairro'] = self.__df['cod_bairro'].fillna(self.__text_default)
        return self.__df
    
    def __transform_nome_bairro_column(self):
        self.__df['nome_bairro'] = self.__df['nome_bairro'].fillna(self.__text_default)
        self.__df['nome_bairro'] = self.__df['nome_bairro'].str.title()
        return self.__df
    
    def __transform_situacao_empresa_column(self):
        self.__df['situacao_empresa'] = self.__df['situacao_empresa'].fillna(self.__text_default)
        self.__df['situacao_empresa'] = self.__df['situacao_empresa'].str.title()
        return self.__df