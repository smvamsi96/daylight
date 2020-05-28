#!/usr/bin/env python3

import json
import lib as L
import TimeManagementUnit as T


TMU = T.TimeManagementUnit()
# a container for all the jobs
jobs = []
# load all the jobs from disk
jobs = L.loadFromDisk()
# sort the jobs using length
#L.quickSort(jobs, 0, len(jobs)-1)
#for job in jobs:
#    TMU.schedule(job)

L.saveToDisk(jobs)
