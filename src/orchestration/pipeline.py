from core.logging import log
from core.http.fetch import Http

from orchestration.extract import Extract
from core.constants.urls import urls

import asyncio

class Pipeline:
    def run(self):
        e = Extract(http=Http())
        log(status='info', message='Iniciando a extração assícrona.')
        data = asyncio.run(e.run(cfg=urls))
        log(status='info', message='Finalizando a extração assícrona.')