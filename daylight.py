#!/usr/bin/env python3

import json
import lib as L
import TimeManagementUnit as T

def myFunc(e):
    return e.signature['daylight_index']


TMU = T.TimeManagementUnit()
# a container for all the jobs
job_list = []
# load all the jobs from disk
job_list = L.loadFromDisk()


for job in job_list:
    job.calc_daylight_index()
    print(job.signature['priority'], job.signature['job_length'], job.signature['daylight_index'])


queue = sorted(job_list, reverse=True, key=myFunc)
for job in queue:
    TMU.talloc(job)
L.printJobs(queue)
print(f"free-time left: {(len(TMU.free_slots)*5)/60} Hours")
