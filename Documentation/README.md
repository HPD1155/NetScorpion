# Welcome to the documentation to the NetScorpion library!
This folder will contain everything you will need to know to use and run scorpion on your own projects.
The guide is constantly being updated and will be regularly updated to reflect the latest changes to the Scorpion library.

Lets get started on what you need so far

# Download NetScorpion

**pip**:
```bash
pip install netscorpion
```
**Github**:
```bash
cd <project folder>
git clone https://github.com/HPD1155/NetScorpion
```

# Importing

To import netscorpion and it's submodules, use:
```python
import netscorpion
from netscorpion import *
# Example of what you can import from scorpion
from netscorpion.scanning import portscanning
```

# Running your first port scan using NetScorpion

```python
# Scorpion provides a default but customizable medium speed for scanning ports, but it is accurate
from netscorpion.scanning import portscanning as ps

port = ps.scanPort("127.0.0.1", 80)

# To print out the result
print(port) # or
print(ps.scanPort("127.0.0.1", 80))
```