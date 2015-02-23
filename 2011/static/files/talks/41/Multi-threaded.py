#!/usr/bin/env python

_app_name = "PyCon11"
_version = "1.0"
_license = """
    Copyright 2010 Chetan Giridhar and Vishal Kanaujia <cjgiridhar@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License v3 for more details.

"""
__author__ = "Chetan Giridhar, Vishal Kanaujia"
__date__ = "$Aug 31, 2011 09:37:00$"

from datetime import datetime
import threading
import random

def cpu(n):
	while n>0:
		n-=1
		(random.uniform(1, 10000))/(random.uniform(1, 100000))
		(random.uniform(1, 10000))*(random.uniform(1, 100000))


iterations = 12000000
startTime  = datetime.now()
thread1 = threading.Thread(target=cpu, args=(iterations,))
thread2 = threading.Thread(target=cpu,  args=(iterations,))
thread3 = threading.Thread(target=cpu,  args=(iterations,))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
endTime = datetime.now()

diffTime = endTime - startTime
print diffTime