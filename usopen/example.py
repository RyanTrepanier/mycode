import os
import netmiko


os.system("ping -c 1 sw-1")

# open an ssh connection to sw-1
conn = netmiko.ConnectHandler(device_type="arista_eos",
                                 ip="sw-1",
                                 username="admin",
                                 password="alta3")

resp = conn.send_command("show ip int brief")
print(resp)
