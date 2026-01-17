from core.logging import log

import aiohttp


class Http:
  async def fetch(self, url: str, serie: str, session: aiohttp.ClientSession) -> dict:
    """_summary_

    Args:
        url (str): _description_
        serie (str): _description_
        session (aiohttp.ClientSession): _description_

    Returns:
        dict: _description_
    """
    async with session.get(url) as resp:
        log(status='info', message=f'{serie} sendo extraida.')
        resp.raise_for_status()
        return {
          "serie": serie,
          "data": await resp.text()
        }
    
