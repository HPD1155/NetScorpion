_warnings_enabled = True
_async_enabled = True
_nFilter_enabled = True

def _asyncWarning():
    """
    Prints a warning message indicating that async functions should be run using asyncio.run() or asyncio.create_task().

    Parameters:
        None

    Returns:
        None
    """
    print("\033[33mTo use async functions, you need to use asyncio.run() or asyncio.create_task(), (to hide this warning please import Scorpion.warnings and then use 'Scorpion.warnings.showWarning(False) or Scorpion.warnings.Warnings.Async(False)')\033[37m\n")

def _blockingWarning():
    """
    Displays a network and firewall filter warning message if both warnings and network filtering are enabled.
    """
    if _warnings_enabled == True and _nFilter_enabled == True: 
        print("\033[33mThis function may cause your network or firewall to start blocking packets due to the number of requests being sent to the/a given amount of ports. Please make sure your firewall or network filter is not blocking packets.\033[37m")
        print("\033[32mTo disable this warning, please use Scorpion.warnings.showWarning(False) or Scorpion.warnings.Warnings.nFilter(False)\033[37m\n")    
    else:
        pass

def showWarning(tf):
    """
    Set whether warnings are enabled or disabled.
    Put this function before the items causing the warning

    Parameters:
        tf (bool): The value indicating whether warnings should be enabled or disabled.

    Returns:
        None
    """
    global _warnings_enabled
    try:
        _warnings_enabled = tf
    except:
        print("\033[31mPlease use a boolean argument to set Scorpion.warnings\033[37m")

def _main():
    print("Testing main functions in Scorpion.warnings")
    _asyncWarning()

class Warnings:
    def Async(tf):
        """
        Set the global variable _async_enabled to the value of tf.
        Disables only async warnings.

        Parameters:
            tf (bool): The value to set _async_enabled to.

        Returns:
            None
        """
        global _async_enabled
        _async_enabled = tf

        
    def nFilter(tf):
        """
        Set the global variable _nFilter_enabled to the value of tf.
        Disables only network and firewall filter warnings.
        
        Parameters:
            tf (bool): The value to set the _nFilter_enabled flag to.

        Returns:
            None
        """
        global _nFilter_enabled
        _nFilter_enabled = tf


if __name__ == "__main__":
    _main()