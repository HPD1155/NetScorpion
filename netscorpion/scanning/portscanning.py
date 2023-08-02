import sys
import time
import asyncio
from netscorpion import warnings as sw
import socket
import sys
import threading
import csv

sys.dont_write_bytecode = True

_highest_port_scanned = -1
top_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 587, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443, 8888, 9000, 9001, 9090, 9100, 9200, 9300, 10000, 10050, 10051, 11211, 27017, 27018, 27019, 28017, 50000, 50070, 50030, 50060, 50075, 50090, 5432, 5984, 6379, 7001, 7002, 8000, 8001, 8002, 8008, 8081, 8082, 8088, 8090, 8091, 8444, 8880, 8883, 8888, 9001, 9090, 9091, 9200, 9300, 9418, 9999, 11211, 27017, 27018, 27019, 28017, 50000, 50070, 50030, 50060, 50075, 50090, 5432, 5984, 6379, 7001, 7002, 8000, 8001, 8002, 8008, 8081, 8082, 8088, 8090, 8091, 8444, 8880, 8883, 8888, 9001, 9090, 9091, 9200, 9300, 9418, 9999]
_open = []

def _write_csv(file, data1, data2):
    with open(file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([data1, data2])
    csvfile.close()
def __sp(host, port, timeout=1):
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

def _threadingSP(host, port, tm=1, disp=False, save=""):
    global _highest_port_scanned
    if _highest_port_scanned == -1:
        _highest_port_scanned = port
    else:
        _highest_port_scanned = _highest_port_scanned + 1
        port = _highest_port_scanned
    result = __sp(host, port, timeout=tm)
    if "open" in result:
        _open.append(port)
        if save != "":
             _write_csv(save, host + ":" + str(port), "open")
    else:
        if save != "":
             _write_csv(save, host + ":" + str(port), "closed")
        else:
            pass
    if disp == True:
        print(result)
        return result
    else:
        return result
    


    

def scanPort(host, port, tm=1, save=""):
    """
    Scans a specified port on a host for connectivity and saves the result to a CSV file.

    Parameters:
        host (str): The IP address or hostname of the target host.
        port (int): The port number to scan for connectivity.
        tm (int, optional): The timeout value in seconds for the port scan. Default is 1 second.
        save (str, optional): The file path to save the scan result as a CSV file. Default is an empty string.

    Returns:
        str: The result of the port scan. If the save parameter is an empty string, the result is returned as a string. If the save parameter is provided, the result is also saved to the specified CSV file.

    Raises:
        Exception: If the port scan fails for an unknown reason, an exception is raised and "Failed for unknown reason!" is printed.
    """
    try:
        if save == "":
            return _threadingSP(host, port, tm)
        else:
            result = __sp(host, port, timeout=tm)
            if "open" in result:
                _write_csv(save, host + ":" + str(port), "open")
            else:
                _write_csv(save, host + ":" + str(port), "closed")
            return result
        
    except:
        print("Failed for unknown reason!")

def scanTopPorts(host, display=False, tm=1, exclude=[], save=""):
    """
    Scans the top ports of a given host for open ports.
    
    Parameters:
        host (str): The target host to scan for open ports.
        display (bool, optional): If True, displays the output of each port scan. Defaults to False.
        tm (int, optional): The timeout value for each port scan in seconds. Defaults to 1.
        exclude (list, optional): A list of ports to exclude from the scan. Defaults to an empty list.
        save (str, optional): Choose a file name such as "savedata.csv" or leave blank to not save the data to a file.
    
    Returns:
        list: A list of open ports found during the scan if `display` is False.
    
    Raises:
        None.
    """
    
    sw._blockingWarning()
    if display == False:
        openPorts = []
        for port in top_ports:
            try:
                if port not in exclude:
                    if "open" in __sp(host, port, timeout=tm): 
                        openPorts.append(port)
                        if save != "":
                            _write_csv(save, host + ":" + str(port), "open")
                    else:
                        if save != "":
                            _write_csv(save, host + ":" + str(port), "closed")
                        else:
                            pass

            except:
                print("Failed for unknown reason!")
        return openPorts
    else:
        for port in top_ports:
            if port not in exclude:
                try:
                    result = __sp(host, port, timeout=tm)
                    print(result)
                    if save != "":
                        if "open" in result:
                            _write_csv(save, host + ":" + str(port), "open")
                        else:
                            _write_csv(save, host + ":" + str(port), "closed")
                except:
                    print("Failed for unknown reason!")

def scanPortRange(host, minPort, maxPort, display=False, tm=1, exclude=[], save=""):
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
                if port not in exclude:
                    try:
                        if "open" in __sp(host, port, timeout=tm): 
                            openPorts.append(port)
                            if save != "":
                                _write_csv(save, host + ":" + str(port), "open")
                        else:
                            _write_csv(save, host + ":" + str(port), "closed")
                    except:
                        print("Failed for unknown reason!")
        return openPorts
    else:
        for port in range(minPort, maxPort):
            if port not in exclude:
                try:
                    result = __sp(host, port, timeout=tm)
                    print(result)
                    if save != "":
                        if "open" in result:
                            _write_csv(save, host + ":" + str(port), "open")
                        else:
                            _write_csv(save, host + ":" + str(port), "closed")
                except:
                    print("Failed for unknown reason!")

def getTopPorts():
    """
    Retrieves the top ports.

    Returns:
        top_ports (list): A list of the top ports.
    """
    return top_ports

class multithreading:
    sw._blockingWarning()

    def scanPortRange(host, minPort, maxPort, display=False, timeout=1, threads=2, exclude: list = [int], save=""):
        """
        Scans a range of ports on a given host to check for open ports.

        Args:
            host (str): The IP address or hostname of the target host.
            minPort (int): The minimum port number to start scanning from.
            maxPort (int): The maximum port number to scan up to.
            display (bool, optional): Whether to display the progress of the scan. Defaults to False.
            ttm (int, optional): The time to wait between each scan in milliseconds. Defaults to 1.
            threads (int, optional): The number of threads to use for scanning. Defaults to 2.

        Returns:
            list: A list of open ports found during the scan.
        """

        if sw._warnings_enabled == True and sw._multithreading_enabled == True:
            sw._multithreading_warning()

        # List of what ports are open
        _open = []

        # iterates through the ports
        for port in range(minPort, maxPort):
            if port not in exclude:
                # Check if the the highest port scanned is greater than the maxports
                if _highest_port_scanned > maxPort:
                    break
                
                # Running threads
                _threads = []
                
                # Set up the threads
                for i in range(threads):
                    thread = threading.Thread(target=_threadingSP, args=(host, port, display, timeout, save))
                    _threads.append(thread)

                # Start the threads for the current port
                for thread in _threads:
                    thread.start()

                # Wait for all threads to finish for the current port
                for thread in _threads:
                    thread.join()
        
        # returns the open ports
        return _open