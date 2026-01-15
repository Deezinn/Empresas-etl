from email import header
from io import StringIO
from entities.empresas.http import Http

from orchestration.extract import Extract
from core.constants.urls import urls

import asyncio
import pandas as pd


if __name__ == "__main__":
    e = Extract(http=Http())
    data = asyncio.run(e.run(cfg=urls))
    for d in data:
        data = d['data']
        serie = d['serie']
        dataframe = pd.read_csv(StringIO(data), sep=';')
        dataframe.to_csv(f'../csv/{serie}.csv')