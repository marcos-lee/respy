#!/usr/bin/env python
"""  This script can be registered as a cron job on the development server.
The idea is to have the test battery executed automatically if the CPU load
allows.
"""

# standard library
import socket
import os

# Specify request
HOURS, NOTIFICATION = 0.0000001, True

# Get some basic information about the system.
HOSTNAME = socket.gethostname()
LOADAVG = os.getloadavg()[2]

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
PACKAGE_DIR = PACKAGE_DIR.replace('/tools', '')

# Move into the testing directory
os.chdir(PACKAGE_DIR + '/development/testing')

# Execute script on the development server.
#if HOSTNAME == 'zeus':
if True:
    is_available = LOADAVG < 2.5

    if is_available:
        cmd = 'python run.py --compile --hours ' + str(HOURS)
        if NOTIFICATION:
            cmd += '  --notification'

        os.system(cmd)




