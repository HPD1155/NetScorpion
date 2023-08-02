
import netscorpion.warnings as sw
sw.showWarning(False)
import netscorpion.scanning.portscanning as ps
import netscorpion.scanning.async_port_scanning as sp
import requests
import asyncio

excluded = [5, 6, 10, 20]


ps.multithreading.scanPortRange("127.0.0.1", 1, 100, display=True, exclude=excluded, threads=3, save="test.csv")