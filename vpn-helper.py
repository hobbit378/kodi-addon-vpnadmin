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
    conn = 'iptv'
    p = None
    msg = 'NONE'

    addondir=os.path.dirname(os.path.realpath(__file__))  
    xbmc.log(addondir,level=xbmc.LOGNOTICE)
    
    dialog = xbmcgui.Dialog()
    cmds = ["on","off","status","restart"]
    nr = dialog.select("Select VPN ... ?", cmds)
    
    if nr>=0:
        cmd = cmds[nr]
        p = subprocess.Popen(['sudo','./scripts/switch-vpn',cmd],cwd=addondir,stdout=subprocess.PIPE)
        msgobj = p.communicate()
        msg = msgobj[0]
        dialog.textviewer('VPN Status',msg)
    
    if p.returncode !=None and p.returncode !=0:
        dialog.notification('VPN', "VPN operation failed (exit code: {0})".format(p.returncode), xbmcgui.NOTIFICATION_ERROR, 5000, True)
         
    return
    
if __name__ == '__main__':
    main()
