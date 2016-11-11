#!/usr/bin/python

import subprocess
import os

ZNC_BINARY_FILE='znc'
ZNC_EXECUTABLE_LOCATION='/usr/bin/znc'


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

    # noinspection PyBroadException
    try:
        fnull = open(os.devnull, 'w')
        subprocess.call(execpath, stdout=fnull, stderr=subprocess.STDOUT)
    except Exception:
        print "Errored out running ZNC.  Run manually."


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