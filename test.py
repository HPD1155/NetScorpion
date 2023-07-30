import netscorpion.scanning.portscanning as ps
import netscorpion.warnings as sw
sw.showWarning(False)
import netscorpion.scanning.async_port_scanning as sp
import requests
import asyncio

ps.scanPort("127.0.0.1", 80)