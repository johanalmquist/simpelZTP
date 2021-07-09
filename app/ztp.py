from app.notifications import viaSlack
from app.network import getGolden, featch_serial
import napalm
import time
import sys
import os
def start(host):
    Serial = featch_serial(host)
    viaSlack('{} started ZTP'.format(Serial))
    #viaTeams('{} started ZTP'.format(Serial))
    if getGolden(host=host):
        viaSlack('{} has saved golden config to startup-config. Device is finshed and can been turnd off'.format(Serial))
        #viaTeams('{} has saved golden config to startup-config. Device is finshed and can been turnd off'.format(Serial))
        #os.system("supervisorctl reload")
    else:
        viaSlack('ZTP for {} not successfull. Please reboot device!'.format(Serial))
        #viaTeams('ZTP for {} not successfull. Please reboot device!'.format(Serial))
    return
    