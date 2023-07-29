import Scorpion.scanning.portscanning as ps
import Scorpion.warnings as sw
sw.showWarning(False)
import Scorpion.scanning.async_port_scanning as sp
import requests
import asyncio

ps.scanPort("127.0.0.1", 80)