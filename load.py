#!/usr/bin/python
import subprocess
subprocess.call(['sudo make clean'], shell=True)
subprocess.call(['sudo make'], shell=True)
subprocess.call(['avrdude -p m328p -c gpio -e -U flash:w:build-cli/piduino.hex'], shell=True)
