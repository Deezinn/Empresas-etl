from src.interface import EmpresaInativaTransformInterface
from io import StringIO
import pandas as pd

class EmpresaInativaTransform(EmpresaInativaTransformInterface):
    def __init__(self):
        self._raw_inativas = None
        self._df = None
        self._text_default = 'Não informado'
        
    def transform(self, inativosCsv):
        """
        Método orquestrador que aplica todas as transformações
        """
        self._raw_inativas = inativosCsv
        self._transform_to_dataframe()
        self._rename_columns()
        self._transform_cnpj_column()
        self._transform_razao_social_column()
        self._transform_nome_fantasia_column()
        self._transform_cod_logradouro_column()
        self._transform_nome_logradouro_column()
        self._transform_numero_residencia_column()
        self._transform_numero_lote_column()
        self._transform_cod_bairro_column()
        self._transform_nome_bairro_column()
        self._transform_situacao_empresa_column()
        
    def _transform_to_dataframe(self):
        """Converte CSV para DataFrame"""
        self._df = pd.read_csv(
            StringIO(self._raw_inativas),
            sep=';',
            dtype=str,
            encoding='utf-8-sig',
            low_memory=False
        )

    def _rename_columns(self):
        """Renomeia colunas problemáticas"""
        self._df.rename({'ï»¿cnpj': 'cnpj'}, axis=1, inplace=True)

    def _transform_cnpj_column(self):
        """Limpa CNPJs, mantendo apenas números"""
        self._df['cnpj'] = self._df['cnpj'].str.replace(r'\D', '', regex=True)

    def _transform_razao_social_column(self):
        """Normaliza 'razao_social' e preenche valores ausentes"""
        self._df['razao_social'] = self._df['razao_social'].replace({'.': self._text_default})
        self._df['razao_social'] = self._df['razao_social'].fillna(self._text_default)
        self._df['razao_social'] = self._df['razao_social'].str.title()

    def _transform_nome_fantasia_column(self):
        self._df['nome_fantasia'] = self._df['nome_fantasia'].replace({'.': self._text_default})
        self._df['nome_fantasia'] = self._df['nome_fantasia'].fillna(self._text_default)
        self._df['nome_fantasia'] = self._df['nome_fantasia'].str.title()

    def _transform_cod_logradouro_column(self):
        self._df['cod_logradouro'] = self._df['cod_logradouro'].fillna(self._text_default)

    def _transform_nome_logradouro_column(self):
        self._df['nome_logradouro'] = self._df['nome_logradouro'].fillna(self._text_default)

    def _transform_numero_residencia_column(self):
        self._df['numero_residencia'] = self._df['numero_residencia'].fillna(self._text_default)

    def _transform_numero_lote_column(self):
        self._df['numero_lote'] = self._df['numero_lote'].fillna(self._text_default)

    def _transform_cod_bairro_column(self):
        self._df['cod_bairro'] = self._df['cod_bairro'].fillna(self._text_default)

    def _transform_nome_bairro_column(self):
        self._df['nome_bairro'] = self._df['nome_bairro'].fillna(self._text_default)
        self._df['nome_bairro'] = self._df['nome_bairro'].str.title()

    def _transform_situacao_empresa_column(self):
        self._df['situacao_empresa'] = self._df['situacao_empresa'].fillna(self._text_default)
        self._df['situacao_empresa'] = self._df['situacao_empresa'].str.title()
