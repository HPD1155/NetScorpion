# import libs
import socket
import requests
import sys
import time
import asyncio
from netscorpion.scanning import portscanning
from netscorpion import warnings as sw
import tracemalloc
tracemalloc.start()

import sys
sys.dont_write_bytecode = True

# Display the async warning if enabled
if sw._warnings_enabled == True and sw._async_enabled == True:
    sw._asyncWarning()

async def _sp(host, port, timeout=1):
    """
    Check if a port on a host is open.
    
    Args:
        host (str): The hostname or IP address of the host to check.
        port (int): The port number to check.
        timeout (float, optional): The timeout value in seconds for the connection attempt.
            Defaults to 1.

    Returns:
        str: A message indicating whether the port is open or not.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(timeout)
        
        result = s.connect_ex((host,port))
        s.close()
        if result ==0:
            return "Port " + str(port) + " is open"
        else:
            return "Port " + str(port) + " is closed"
    except KeyboardInterrupt:
            sys.exit()
    except socket.gaierror:
            print("\n Hostname could not be resolved")
            sys.exit()
    except socket.error:
            print("\n Server connection timed out or is not responding")
            sys.exit()

# get the top ports list from portscanning module
top_ports = portscanning.top_ports




def scanPortAsync(host, port, tm=1):
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
        return _sp(host, port, timeout=tm)
    except:
        print("Failed for unknown reason!")
    
def pScanTopPortsAsync(host, display=False, tm=1, exclude: list = [int]):
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
            if port not in exclude:
                try:
                    if "open" in _sp(host, port, timeout=tm):
                        openPorts.append(port)
                except:
                    print("Failed for unknown reason!")
        return openPorts
    else:
        for port in top_ports:
            if port not in exclude:
                try:
                    print(_sp(host, port, timeout=tm))
                except:
                    print("Failed for unknown reason!")

def pScanPortRangeAsync(host, minPort, maxPort, display=False, tm=1, exclude: list = [int]):
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
            if port not in exclude:
                try:
                    if "open" in _sp(host, port, timeout=tm):
                        openPorts.append(port)
                except:
                    print("Failed for unknown reason!")
        return openPorts
    else:
        for port in range(minPort, maxPort):
            if port not in exclude:
                try:
                    result = _sp(host, port, timeout=tm)
                    print(result)
                    if "open" in result:
                        openPorts.append(port)
                except:
                    print("Failed for unknown reason!")
        return openPorts

__warningmessage = """
You cannot run this file directly. Please use the following:
import Scorpion.async_port_scanning
or
from Scorpion import async_port_scanning
"""

if __name__ == "__main__":
    print(__warningmessage)