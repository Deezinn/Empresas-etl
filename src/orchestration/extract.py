from core.http.fetch import Http

import aiohttp
import asyncio

class Extract:
    # SEMAPHORE = asyncio.Semaphore(5)

    def __init__(self, http: Http):
        self.__http: Http = http

    async def run(self, cfg: dict) -> list:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=50)) as session:
            tasks: list = [
                asyncio.create_task(
                    self.__http.fetch(
                        url=url,
                        serie=serie,
                        session=session
                    )
                ) for serie, url in cfg.items()
            ]
            return await asyncio.gather(*tasks, return_exceptions=True)