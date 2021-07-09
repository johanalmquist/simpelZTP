# SimpelZTP

## Stackover view
A simpel system to auto provision for ciscos. Can also work with others vendor with some changes.

### Aruba 2930f 8P - Access switch
IP: 10.10.0.2/24
Acting as a accessswitch between OneAccess modem, PFsense and auto-prov switch.
- Port 10 is connected to OneAccess mode via fiber for feed system with DIA (Direct Internet Access) via vlan 3010 tagget
- Port 9 is conntet to Pfsense router. Is a trunkport for feed system trafic over spec vlan.
  - Vlan 3010 is untagget to Pfsense router
- Port 8 is connteced to the "Autoprov switch" and passing down vlan 100.
- Port 7 is mgmt port for access to system over vlan 10.
- Port 1 is connected to Aruba AP-305 for wireless mgmt access.
  - Vlan 10 is untagged for feed accesspoint with a mgmt IP.
  - Vlan 20 is tagget to Accesspoint for the wireless mgmt network.

### Pfsense
Handels all trafic and holds all ip and vlan interface.
Network defindes in the router will come soon

### Aruba 2530 24P - auto-prov switch
IP: 10.10.0.3/24
Is the switch for handle trafic for auto provision
- Port 26 is connected to the Access switch over vlan 100 tagged
- Port 25 is connted to server that holdning the auto provision system over vlan 100 untagged.
- Port 1-12 is auto provisions port for connteing decvies to. All port passing down vlan 100 untagged.

### Auto provision server
OS: Ubuntu 20.04
IP: 172.16.100.10/23

## Brief overview of the auto provision progress.
- Cisco is booting up and getting a from the DHCP-server in the auto-prov server.
- DHCP request is passing option 150 to tell cisco to ash tftp server for configutaton.
- cisco devide will do request the tftp-server for configuration.
  - TFTP-server will only passdown configuration when cisco is asking for the cisconet.cfg file.
  - After the cisco has read in the cisconet.cfg configuration will ask for the R1.cfg file. This file does not extis but will trigger the auto provision progress to call the function trigger_job as IP-address of the device as a parameter.
- The trigger_job function will place the device to the cue. The function will also check if the device alrady are in line or are getting provisioning. If its true the function will dropp the request.
- When is the devides turn to get provisioning the trigger_job function will call the function start form the ztp.py file and the IP-address of the device as a parameter.
- The start function will start to get the Serial number from the device and save it to the variable Serial
- A notification will be trigger to tell a user that device has staring provisioning.
- Via the function getGolden the system will load the final configutaton. The getGolden function has the IP-address of the device as a parameter.
  - getgolden function will start to login to the device and run the enable commad for executes commands.
  - its execute commad for grab the final configutaton from the tftp-server and save it to start-up config
- If all goes will a new notification will be trigger to tell the user that device has been provision.









