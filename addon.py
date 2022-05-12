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

    BTNS = ['VPN on','VPN off','Routing Table']
    CMDS = ['ip rule add uidrange 111-111 lookup kodi','ip rule del uidrange 111-111 lookup kodi','ip rule']

    dialog = xbmcgui.Dialog()
    nr = dialog.select('VPN', BTNS)
    
    if nr>=0:
        cmd = CMDS[nr]
        p = subprocess.Popen(['sudo',cmd],stdout=subprocess.PIPE)
        msgobj = p.communicate()
    
        if p.returncode !=None and p.returncode !=0:
            dialog.notification('VPN', "VPN error (exit code: {0})".format(p.returncode), xbmcgui.NOTIFICATION_ERROR, 5000, True)
            xbmc.log("VPN error (exit code: {0})".format(p.returncode),xbmc.LOGERROR)
            xbmc.log(msgobj[0],xbmc.LOGDEBUG)
            return
         
        if BTNS[nr] == 'Routing Table' :
            dialog.textviewer('VPN Routing Status',msgobj[0])
         
    return
    
if __name__ == '__main__':
    main()
