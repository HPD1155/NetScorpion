# NetScorpion

![Status](https://img.shields.io/badge/Status-Not%20Publish%2FPackage%20Ready-red)

[![CodeQL](https://github.com/HPD1155/Scorpion/actions/workflows/codeql.yml/badge.svg)](https://github.com/HPD1155/NetScorpion/actions/workflows/codeql.yml)

# Description
NetScorpion is an open-source Python library for network scanning and analysis. It provides tools to discover active hosts, perform port scans, identify services running on open ports, and conduct vulnerability assessments. With NetScorpion, you can gain insights into your network's health, security, and performance.

# Features
- Network discovery: Find active hosts on the network using various scanning techniques.
- Port scanning: Scan for open ports on discovered hosts to identify available services.
- Service detection: Identify the services running on open ports to understand your network's configuration.
- Vulnerability scanning: Integrate with vulnerability databases to identify potential risks.
- Network topology mapping: Visualize the network layout to understand device connections.
- Network traffic analysis: Capture and analyze network traffic for performance and security insights.

# Installation
To install NetScorpion, use pip:

```bash
pip install netscorpion
```
# Usage

```python
import netscorpion
from netscorpion import *
from netscorpion.scanning import portscanning
```

# Contributing
NetScorpion is open-source library, and we welcome contributions from the community. Please see the contributing.txt file for more information.

# Contributions we need at the moment
- new features Priority: HIGH
- bug fixes Priority: LOW
- documentation Priority: HIGH
- unit tests Priority: MEDIUM
- testing files Priority: MEDIUM
- reviewing files Priority: MEDIUM
- new components Priority: HIGH