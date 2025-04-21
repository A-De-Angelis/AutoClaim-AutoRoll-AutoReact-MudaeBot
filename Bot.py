#!/usr/bin/env python3
import sys
print("Using Python:", sys.executable)

import Vars
import time
import schedule
from Function import simpleRoll

timeString = ':'+ Vars.repeatMinute
schedule.every().hour.at(timeString).do(simpleRoll)

while True:
    schedule.run_pending()
    time.sleep(1)
