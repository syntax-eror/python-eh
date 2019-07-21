#!/usr/bin/env python

import subprocess

command = "msg * Test Message"
subprocess.Popen(command, shell=True)
