import time
import asyncio
import logging
import sys
import aiohttp

from enochecker import BaseChecker, BrokenServiceException, create_app, OfflineException, ELKFormatter, CheckerTask
from logging import LoggerAdapter

class TestChecker(BaseChecker):
    port = 9012

    def __init__(self):
        super(TestChecker, self).__init__("TestService")

    async def test(self, logger: LoggerAdapter):
        async with aiohttp.ClientSession() as session:
            async with session.get("http://enowars.com") as response:
                assert response.status == 200
                ret = await response.read()
                print(ret)

    async def putflag(self, logger: LoggerAdapter, task: CheckerTask) -> None:
        await self.test(logger)
        
    async def getflag(self, logger: LoggerAdapter, task: CheckerTask) -> None:
        await self.test(logger)
        
    async def putnoise(self, logger: LoggerAdapter, task: CheckerTask) -> None:
        await self.test(logger)

    async def getnoise(self, logger: LoggerAdapter, task: CheckerTask) -> None:
        await self.test(logger)

    async def havoc(self, logger: LoggerAdapter, task: CheckerTask) -> None:
        pass

    async def exploit(self, logger: LoggerAdapter, task: CheckerTask) -> None:
        pass


logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
#handler.setFormatter(ELKFormatter("%(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

app = create_app(TestChecker())