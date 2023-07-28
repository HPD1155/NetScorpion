import Scorpion.scanning.portscanning as ps

print(ps.scanPort("127.0.0.1", 80))

ps.scanTopPorts("127.0.0.1")