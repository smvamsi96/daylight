#!/usr/bin/env python3

import json
import lib as l

TMU = l.TimeManagementUnit()

# a container for all the jobs
jobs = []
# load all the jobs from disk
jobs = l.deserialize()
# organize jobs based on daylight_index
l.schedule_jobs(jobs)
for job in jobs:
    TMU.schedule(job)

l.print_jobs(jobs)


# TODO
# add jobs while the program is running
