import datetime as d

class TimeManagementUnit:
    """A class that manages time slots for all jobs"""
    base_time = d.datetime.now()
    base_time = base_time.replace(hour=0, minute=0, second=0)
    min_time_slice = 5 #minutes
    hours = 0
    days = 1
    weeks = 0
    months = 0
    years = 0
    total_slices= ((years*365*24*60) + (months*30*24*60) + (weeks*7*24*60) + (days*24*60) + (hours*60))/min_time_slice
    # right now, the time_container equals 1440 slices!
    free_slots = [value for value in range(1, int(total_slices)+1)]

    def schedule(self, job):
        # grab the first free time-slice in free_slots
        grab = int(job.signature["job_length"])
        job.base = self.free_slots.pop(0)
        slice_length = 1
        while (slice_length*self.min_time_slice < grab):
            job.bound = self.free_slots.pop(0)
            slice_length += 1
        if (job.bound == 0):
            job.bound = job.base
        job.base, job.bound = self.map_slice_to_time(job.base, job.bound)

    def map_slice_to_time(self, base, bound):
        x = base*(self.min_time_slice)
        y = bound*(self.min_time_slice)
        base = self.base_time + d.timedelta(minutes=x-self.min_time_slice)
        bound = self.base_time + d.timedelta(minutes=y)
        return base, bound
