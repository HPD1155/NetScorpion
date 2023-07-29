import requests
import sys
import time
import asyncio
from Scorpion.scanning import portscanning
from Scorpion import warnings as sw

top_ports = portscanning.top_ports

if sw._warnings_enabled == True and sw._async_enabled == True:
    sw._asyncWarning()


async def scanPortAsync(host, port):
    """
    Asynchronously scans a given port on a specified host.

    Call:
        You will have to use asyncio.create_task() or asyncio.run() to run this function.
        
    Args:
        host (str): The IP address or hostname of the host to scan.
        port (int): The port number to scan.
    
    Returns:
        str: A string indicating whether the port is open or closed.
    """
    
    try:
        await requests.get("http://127.0.0.1:" + port)
        return "Port " + str(port) + " is open\n"
    except:
        return "Port " + str(port) + " is closed\n"
    
async def pScanTopPortsAsync(host, display=False):
    sw._blockingWarning()
    """
    Asynchronously scans the top ports of a given host.

    Call:
        You will have to use asyncio.create_task() or asyncio.run() to run this function.

    Args:
        host (str): The IP address or hostname of the host to scan.
        display (bool, optional): Whether to display the open ports or not. Defaults to False.'

    Returns:
        list: A list of open ports if display is False.
    
    Prints:
        str: A message indicating whether each port is open or closed if display is True.
    """
    if display == False:
        openPorts = []
        for port in top_ports:
            try:
                await requests.get("http://127.0.0.1:" + port)
                openPorts.append(port)
            except:
                pass
        return openPorts
    else:
        for port in top_ports:
            try:
                await requests.get("http://127.0.0.1:" + port)
                print("Port " + str(port) + " is open")
            except:
                print("Port " + str(port) + " is closed")

async def pScanPortRangeAsync(host, minPort, maxPort, display=False):
    sw._blockingWarning()
    """
    Asynchronously scans a range of ports on a given host for open connections.

    Call:
        You will have to use asyncio.create_task() or asyncio.run() to run this function.

    Args:
        host (str): The IP address or hostname of the target host.
        minPort (int): The minimum port number to start scanning from.
        maxPort (int): The maximum port number to scan up to (exclusive).
        display (bool, optional): Whether to display the progress of the scan. Defaults to False.

    Returns:
        None

    Raises:
        Any exceptions that occur during the scanning process are caught and ignored.

    """
    if display == False:
        openPorts = []
        for port in range(minPort, maxPort):
            try:
                await requests.get("http://127.0.0.1:" + port)
                openPorts.append(port)
            except:
                pass

__warningmessage = """
You cannot run this file directly. Please use the following:
import Scorpion.async_port_scanning
or
from Scorpion import async_port_scanning
"""

if __name__ == "__main__":
    print(__warningmessage)