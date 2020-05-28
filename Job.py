import datetime as d

class Job:
    """A class for representing a single job"""
    def __init__(self, name, job_length):
        self.name = name
        self.job_length = int(job_length) # say, in minutes
        self.daylight_index = self.calc_daylight_index()
        self.base = 0
        self.bound = 0
        # this assumes that the job executes in one contiguous time_slice

    def calc_daylight_index(self):
        index = self.job_length
        return index

    def get_base(self):
        if isinstance(self.base, d.datetime):
            return self.base.strftime("%d/%m/%Y, %H:%M:%S")
        else:
            return self.base

    def get_bound(self):
        if isinstance(self.base, d.datetime):
            return self.bound.strftime("%d/%m/%Y, %H:%M:%S")
        else:
            return self.bound
