
import aiohttp

class Http:
  async def fetch(self, url: str, serie: str, session: aiohttp.ClientSession) -> dict:
    """
    Args:
        url (str): _description_
        serie (str): _description_
        session (aiohttp.ClientSession): _description_
    """
    async with session.get(url) as resp:
        resp.raise_for_status()
        return {
          "serie": serie,
          "data": await resp.text()
        }
    
