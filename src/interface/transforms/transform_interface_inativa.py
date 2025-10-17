from abc import ABC, abstractmethod

class EmpresaInativaTransformInterface(ABC):
    """
    Interface para transformação de dados da API de empresas inativas.
    Define métodos obrigatórios que qualquer classe concreta deve implementar.
    """

    @abstractmethod
    def transform(self, inativosCsv):
        """
        Método principal que orquestra toda a transformação dos dados.
        Recebe o CSV de empresas inativas.
        """
        pass

    @abstractmethod
    def _rename_columns(self):
        """
        Renomeia colunas do DataFrame conforme padrão definido.
        """
        pass

    @abstractmethod
    def _transform_cnpj_column(self):
        """Transforma a coluna CNPJ (padroniza, remove inválidos)."""
        pass

    @abstractmethod
    def _transform_razao_social_column(self):
        """Transforma a coluna 'razao_social' (normaliza e preenche nulos)."""
        pass

    @abstractmethod
    def _transform_nome_fantasia_column(self):
        """Transforma a coluna 'nome_fantasia' (normaliza e preenche nulos)."""
        pass

    @abstractmethod
    def _transform_cod_logradouro_column(self):
        """Transforma a coluna 'cod_logradouro' (padroniza e preenche nulos)."""
        pass

    @abstractmethod
    def _transform_nome_logradouro_column(self):
        """Transforma a coluna 'nome_logradouro' (normaliza e preenche nulos)."""
        pass

    @abstractmethod
    def _transform_numero_residencia_column(self):
        """Transforma a coluna 'numero_residencia' (padroniza e preenche nulos)."""
        pass

    @abstractmethod
    def _transform_numero_lote_column(self):
        """Transforma a coluna 'numero_lote' (padroniza e preenche nulos)."""
        pass

    @abstractmethod
    def _transform_cod_bairro_column(self):
        """Transforma a coluna 'cod_bairro' (padroniza e preenche nulos)."""
        pass

    @abstractmethod
    def _transform_nome_bairro_column(self):
        """Transforma a coluna 'nome_bairro' (normaliza e preenche nulos)."""
        pass

    @abstractmethod
    def _transform_situacao_empresa_column(self):
        """Transforma a coluna 'situacao_empresa' (padroniza e preenche nulos)."""
        pass
