#!/usr/bin/python

# znc_monitor
# Copyright (C) 2016  Thomas Ward
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import os
from datetime import datetime

# Default binary name for the bouncer's exectuable
ZNC_BINARY_FILE = 'znc'
# Default directory for ZNC executable binary to be located in
ZNC_EXECUTABLE_LOCATION = '/usr/bin/'

# Default log file path (in /tmp/)
LOG_PATH = '/tmp/zncmonitor_log.py'


def process_is_running(name=ZNC_BINARY_FILE):
    try:
        pidlist = map(int, subprocess.check_output(["pidof", name]).split())
    except subprocess.CalledProcessError:
        pidlist = None

    if pidlist is None:
        return False
    else:
        return True


def execute_process(process=ZNC_BINARY_FILE, workdir=ZNC_EXECUTABLE_LOCATION):
    # Check if execpath was specified, and then construct the path.
    if workdir is not None:
        if workdir[-1:] != '/':
            execpath = workdir + '/' + process
        else:
            execpath = workdir + process
    else:
        execpath = process

    logfile = open(LOG_PATH, 'a')
    logfile.write("[%s] Attempting to launch process..." %
                  datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    if os.path.exists(execpath) and os.path.isfile(execpath):
        # noinspection PyBroadException
        try:
            subprocess.call(execpath, stdout=logfile, stderr=logfile)
        except Exception:
            print "Errored out running ZNC; log file at %s may have details" % LOG_PATH
    else:
        logfile.write("[%s] Cannot find process to execute, please check file paths." %
                      datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def main():
    try:
        if not process_is_running('znc'):
            execute_process(workdir=ZNC_EXECUTABLE_LOCATION, process=ZNC_BINARY_FILE)
        else:
            return
    except Exception as e:
        print "Error: %s" % str(e)

if __name__ == "__main__":
    main()
