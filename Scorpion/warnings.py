import atexit as atx

_warnings_enabled = True
_async_enabled = True

def _asyncWarning():
    """
    Prints a warning message indicating that async functions should be run using asyncio.run() or asyncio.create_task().

    Parameters:
        None

    Returns:
        None
    """
    print("\033[33mTo use async functions, you need to use asyncio.run() or asyncio.create_task(), (to hide this warning please import Scorpion.warnings and then use 'Scorpion.warnings.showWarning(False)')\033[37m\n")

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


if __name__ == "__main__":
    _main()