#!/usr/bin/env python3

import json
import lib as l

jobs = []
i = 0

jobs = l.deserialize()

l.print_jobs(jobs)
l.print_jobs(l.schedule_jobs(jobs))

# TODO
# add jobs while the program is running
