#!/usr/bin/python

"""
Provides a Python-compatible interface for the Apple Remote.
Requires this modified version of iremoted: http://github.com/swinton/iremoted.

Usage:
1. Install iremoted from http://github.com/swinton/iremoted along with this Python module.
2. Construct your source code like so:

from iremote import IRemote

def my_iremote_handler(event):
    if event == IRemote.NEXT:
        # Next button pressed
        # ...

iremote = IRemote()
iremote.add_listener(my_iremote_handler)
iremote.start()
"""

import subprocess, sys
from threading import Thread

class IRemote(Thread):
    listeners = []
    NEXT = "0x16 depressed"
    PREV = "0x17 depressed"
    UP = "0x1d depressed"
    DOWN = "0x1e depressed"
    PLAY_PAUSE = "0x15 depressed"
    
    def __init__(self):
        Thread.__init__(self)
        
    def add_listener(self, listener):
        if callable(listener):
            IRemote.listeners.append(listener)
        
    def run(self):
        proc = subprocess.Popen(
            'iremoted',
           shell=True,
           stdout=subprocess.PIPE,
           stderr=subprocess.PIPE,
        )
        while proc.poll() is None:
           output = proc.stdout.readline()
           for listener in IRemote.listeners:
               listener(output[:-1])

def listener(event):
    print "received: ", event, "\n",
    if event == IRemote.NEXT:
        print "skip\n",
                
def main():
    iremote = IRemote()
    iremote.add_listener(listener)
    iremote.start()
    print "iremote running",

if __name__ == "__main__":
    main()