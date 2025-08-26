
# Empresas-ETL

Projeto para **extração, transformação e carregamento (ETL)** de dados de empresas da cidade do Recife.

## Descrição

Este projeto realiza a coleta de informações sobre **empresas ativas no Recife**, utilizando dados públicos disponíveis no portal de dados abertos da cidade. O objetivo é consolidar e disponibilizar essas informações para análises e consultas.

## Fonte de Dados

Os dados utilizados neste projeto estão disponíveis em:

[Empresas da Cidade do Recife](http://dados.recife.pe.gov.br/dataset/empresas-da-cidade-do-recife/resource/87fc9349-312c-4dcb-a311-1c97365bd9f5)

## Dados Obtidos

O dataset contém informações como:

- Nome da empresa
- CNPJ
- Situação cadastral (ativa/inativa)
- Endereço
- Atividades econômicas
- Outros dados relevantes

## Funcionalidades

- **Extração:** Coleta os dados da API pública do Recife.
- **Transformação:** Processa os dados para padronização e limpeza.
- **Carga (Load):** Salva os dados em formato estruturado (CSV, JSON ou banco de dados).

## Tecnologias Utilizadas

- Python
- Requests / HTTP para consumo da API
- Pandas para transformação de dados

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/empresas-etl.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script de extração:
   ```bash
   python -m src.pipeline.empresa_pipeline
   ```

## Observações

- Este projeto tem caráter **educacional**, servindo como exemplo de ETL com dados públicos.
- Os dados são fornecidos pela Prefeitura do Recife e estão sujeitos a atualizações no portal oficial.

---

Desenvolvido por [Deezinn]
