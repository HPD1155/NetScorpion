# import libs
import requests
import sys
import time
import asyncio
from Scorpion.scanning import portscanning
from Scorpion import warnings as sw
from Scorpion.scanning.portscanning import _sp as sp

# get the top ports list from portscanning module
top_ports = portscanning.top_ports

# Display the async warning if enabled
if sw._warnings_enabled == True and sw._async_enabled == True:
    sw._asyncWarning()


async def scanPortAsync(host, port, tm=1):
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
        return sp(host, port, timeout=tm)
    except:
        print("Failed for unknown reason!")
    
async def pScanTopPortsAsync(host, display=False, tm=1):
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
                if "open" in await sp(host, port, timeout=tm):
                    openPorts.append(port)
            except:
                print("Failed for unknown reason!")
        return openPorts
    else:
        for port in top_ports:
            try:
                print(await sp(host, port, timeout=tm))
            except:
                print("Failed for unknown reason!")

async def pScanPortRangeAsync(host, minPort, maxPort, display=False, tm=1):
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
                if "open" in await sp(host, port, timeout=tm):
                    openPorts.append(port)
            except:
                print("Failed for unknown reason!")

__warningmessage = """
You cannot run this file directly. Please use the following:
import Scorpion.async_port_scanning
or
from Scorpion import async_port_scanning
"""

if __name__ == "__main__":
    print(__warningmessage)