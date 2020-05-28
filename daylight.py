#!/usr/bin/env python3

import json
import lib as L
import TimeManagementUnit as T


TMU = T.TimeManagementUnit()
# a container for all the jobs
job_list = []
# load all the jobs from disk
jobs = L.loadFromDisk()
L.addJob(job_list)
L.printJobs(job_list)
L.saveToDisk(job_list)
