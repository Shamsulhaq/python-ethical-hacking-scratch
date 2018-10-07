Mac changer with linux terminal.

1. open your terminal and type "ifconfig"
    It will show all of your address with eth0 or waln0. But waln0 is only showing if useing adapter.
    inet 192.168.---.--- [is your ip]
     netmask 255.---.255.---
     broadcast 192.168.---.---
     inet6 fe80::20c:----:----:---- [is your mack]

2. Than type "ifconfig eth0 down"
    This is first step. When you run this command than it will disable interface. if you see no error then this
    process will be successfully completed.

3. Then type "ifconfig eth0 hw ether 00:11:22:33:44:55"
    It will be modify your mack address. Make sure it will 12 characters.
    
4. Last step type "if config eth0 up"
   This command enable your interface. "eth" means interface.
   
5. Now if your command "ifconfig" than you will see mac address is changed.