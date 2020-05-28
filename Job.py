import datetime as d

class Job:
    """A class for representing a single job"""
    def __init__(self, arg_dict):
        self.signature = {
                "name" : arg_dict["name"],
                "job_length" : int(arg_dict["job_length"]),
                # jobs start out with this default priority level
                "priority" : 9999,
                "daylight_index" : 0,
                }
        # job_length in minutes
        self.base = 0
        self.bound = 0
        # this assumes that the job executes in one contiguous time_slice

    def calc_daylight_index(self):
        self.signature['daylight_index'] = ((self.signature['priority'])/(self.signature['job_length']))

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

    def setPriority(self, priority):
        self.signature['priority'] = priority
