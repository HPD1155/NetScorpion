import requests
import sys
import time
import asyncio
from Scorpion import warnings as sw

top_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 587, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443, 8888, 9000, 9001, 9090, 9100, 9200, 9300, 10000, 10050, 10051, 11211, 27017, 27018, 27019, 28017, 50000, 50070, 50030, 50060, 50075, 50090, 5432, 5984, 6379, 7001, 7002, 8000, 8001, 8002, 8008, 8081, 8082, 8088, 8090, 8091, 8444, 8880, 8883, 8888, 9001, 9090, 9091, 9200, 9300, 9418, 9999, 11211, 27017, 27018, 27019, 28017, 50000, 50070, 50030, 50060, 50075, 50090, 5432, 5984, 6379, 7001, 7002, 8000, 8001, 8002, 8008, 8081, 8082, 8088, 8090, 8091, 8444, 8880, 8883, 8888, 9001, 9090, 9091, 9200, 9300, 9418, 9999]


def scanPort(host, port):
    """
    Scan a given host and port to check if the port is open or closed.

    Parameters:
        host (str): The IP address or hostname of the target host.
        port (int): The port number to scan.

    Returns:
        str: A message indicating whether the port is open or closed.
    """
    try:
        requests.get("http://127.0.0.1:" + port)
        return "Port " + str(port) + " is open\n"
    except:
        return "Port " + str(port) + " is closed\n"

def scanTopPorts(host, display=False):
    sw._blockingWarning()
    if display == False:
        openPorts = []
        for port in top_ports:
            try:
                requests.get("http://127.0.0.1:" + port)
                openPorts.append(port)
            except:
                pass
        return openPorts
    else:
        for port in top_ports:
            try:
                requests.get("http://127.0.0.1:" + port)
                print("Port " + str(port) + " is open")
            except:
                print("Port " + str(port) + " is closed")

def scanPortRange(host, minPort, maxPort, display=False):
    sw._blockingWarning()
    """
    Scans a range of ports on a given host to check for open ports.
    
    Args:
        host (str): The IP address or hostname of the target host.
        minPort (int): The minimum port number to start scanning from.
        maxPort (int): The maximum port number to scan up to.
        display (bool, optional): Whether to display the open ports during the scan. 
            Defaults to False.
    
    Returns:
        list: A list of open ports found during the scan. 
            Returns an empty list if no open ports are found.
    """
    if display == False:
        openPorts = []
        for port in range(minPort, maxPort):
            try:
                requests.get("http://127.0.0.1:" + port)
                openPorts.append(port)
            except:
                pass
        return openPorts
    else:
        for port in range(minPort, maxPort):
            try:
                requests.get("http://127.0.0.1:" + port)
                print("Port " + str(port) + " is open")
            except:
                print("Port " + str(port) + " is closed")

def getTopPorts():
    """
    Retrieves the top ports.

    Returns:
        top_ports (list): A list of the top ports.
    """
    return top_ports
