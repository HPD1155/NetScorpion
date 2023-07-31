
import netscorpion.warnings as sw
sw.showWarning(False)
import netscorpion.scanning.portscanning as ps
import netscorpion.scanning.async_port_scanning as sp
import requests
import asyncio

# How to use multithreading     IP           port port show output timeout threads
ps.multithreading.scanPortRange('127.0.0.1', 400, 500, display=True, timeout=1, threads=8)