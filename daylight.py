#!/usr/bin/env python3

import json
import lib as l

def myFunc(e):
    return e.daylight_index

TMU = l.TimeManagementUnit()

# a container for all the jobs
jobs = []
# load all the jobs from disk
jobs = l.deserialize()
# sort the jobs using length
l.quickSort(jobs, 0, len(jobs)-1)

for job in jobs:
    TMU.schedule(job)

l.print_jobs(jobs)

# TODO
# add jobs while the program is running
