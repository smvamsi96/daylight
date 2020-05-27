import json
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
        grab = int(job.job_length)
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

def input_job():
    name = input("Enter Job Name: ")
    job_length = input("Enter Job Length: ")
    j = Job(name, job_length)
    return j

def serialize(job_dump, file_name='jobs.json'):
    """convert an array of jobs to json"""
    l = len(job_dump)
    i = 0
    d = []
    while (i < l):
        a = []
        a.append(job_dump[i].name)
        a.append(job_dump[i].job_length)
        #a.append(job_dump[i].base)
        #a.append(job_dump[i].bound)
        d.append(a)
        i += 1
    
    with open(file_name, 'w') as j:
        json.dump(d, j)





def deserialize(file_name='jobs.json'):
    """convert a json of jobs to a job array"""
    d = []
    with open(file_name) as j:
        d = json.load(j)

    jobs = []
    l = len(d)
    i = 0
    while (i < l):
        a = Job(d[i][0], d[i][1])#, d[i][2], d[i][3])
        jobs.append(a)
        i += 1
    return jobs

def print_jobs(jobs):
    l = len(jobs)
    i = 0
    while (i < l):
        print(f"Job {i}:")
        print(f"Name: {jobs[i].name}\nLength: {jobs[i].job_length}\nStarts at: {jobs[i].get_base()}\nFinishes at: {jobs[i].get_bound()}\n")
        i += 1


def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high].job_length     # pivot 
    for j in range(low , high): 
        if   arr[j].job_length <= pivot: 
            i = i+1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1] ,arr[high] = arr[high] ,arr[i+1]
    return ( i+1 ) 
  
def quickSort(arr,low,high): 
    if low < high: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
 

