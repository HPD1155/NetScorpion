import Scorpion.scanning.portscanning as ps
import Scorpion.scanning.async_port_scanning as sp
import Scorpion.warnings as sw
import requests
import asyncio

sw.showWarning(False)

print(asyncio.run(sp.scanPortAsync("127.0.0.1", 445)))

