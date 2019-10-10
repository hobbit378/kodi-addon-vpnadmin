# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Matthias Wetzel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import xbmc
import xbmcgui
import os
import subprocess


def main():

    CMDS = ["start","stop","status","restart"]
    DIRBIN = os.path.dirname(os.path.realpath(__file__))
    SCRIPT = os.path.join(DIRBIN,'resources','lib','switch-vpn')

    dialog = xbmcgui.Dialog()
    nr = dialog.select("VPN ... ?", CMDS)
    
    if nr>=0:
        cmd = CMDS[nr]
        p = subprocess.Popen(['sudo',SCRIPT,cmd],stdout=subprocess.PIPE)
        msgobj = p.communicate()
    
        if p.returncode !=None and p.returncode !=0:
            dialog.notification('VPN', "VPN operation failed (exit code: {0})".format(p.returncode), xbmcgui.NOTIFICATION_ERROR, 5000, True)
            xbmc.log("VPN operation failed (exit code: {0})".format(p.returncode),xbmc.LOGERROR)
            xbmc.log(msgobj[0],xbmc.LOGDEBUG)
            return
        
        if cmd == 'start':
            dialog.notification('VPN', "VPN is now ON", xbmcgui.NOTIFICATION_INFO, 5000, True)
            xbmc.log("VPN started",xbmc.LOGINFO)
            return
        
        if cmd == 'stop':
            dialog.notification('VPN', "VPN is now OFF", xbmcgui.NOTIFICATION_INFO, 5000, True)
            xbmc.log("VPN stopped",xbmc.LOGINFO)
            return
            
        if cmd == 'status' or cmd == 'restart':
            dialog.textviewer('VPN Status',msgobj[0])
         
    return
    
if __name__ == '__main__':
    main()
