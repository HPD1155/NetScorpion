# Welcome to the documentation to the Scorpion library!
This folder will contain everything you will need to know to use and run scorpion on your own projects.
The guide is constantly being updated and will be regularly updated to reflect the latest changes to the Scorpion library.

Lets get started on what you need so far

# Download scorpion

Since the package is still very new and needs to be updated a significant amount for it to be used by non-beta and pre-release testers, you cannot install it using pip.
You will need to clone the repository into your project to access the library.
I will stil include the pip installation though.

**pip**:
```bash
pip install scorpion
```
**Github**:
```bash
cd <project folder>
git clone https://github.com/HPD1155/Scorpion
```

# Importing

To import Scorpion and it's submodules, use:
```python
import Scorpion
from Scorpion import *
# Example of what you can import from scorpion
from Scorpion.scanning import portscanning
```

# Running your first port scan using Scorpion

```python
# Scorpion provides a default but customizable medium speed for scanning ports, but it is accurate
from Scorpion.scanning import portscanning as ps

port = ps.scanPort("127.0.0.1", 80)

# To print out the result
print(port) # or
print(ps.scanPort("127.0.0.1", 80))
```