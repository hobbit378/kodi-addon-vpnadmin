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
import subprocess

def main():
    dialog = xbmcgui.Dialog()
    conn = 'iptv'
    cmds = ["on","on-uk","off","up-uk","down-uk","update-ip", "status","restart"]
    p = None
    msg = 'TODO: This is a dummy text'
    
    nr = dialog.select("select VPN action ->", cmds)
    
    if nr>=0:
        cmd = cmds[nr]
        p = subprocess.Popen(['sudo','switch-vpn',cmd],stdout=subprocess.PIPE)
        msgobj = p.communicate()
        msg = msgobj[0]
    
    stat = xbmcgui.Dialog()
    if cmd == 'status':
        stat.textviewer('VPN status',msg)
    elif p.returncode !=None and p.returncode !=0:
        stat.notification('VPN', "VPN operation failed (exit code: {0})".format(p.returncode), xbmcgui.NOTIFICATION_ERROR, 5000, True)
         
    return
    
if __name__ == '__main__':
    main()
