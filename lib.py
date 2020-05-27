import json


class Job:
    """A class for representing a single job"""
    def __init__(self, name, job_length):
        self.name = name
        self.job_length = job_length
        self.daylight_index = self.calc_daylight_index()

    def calc_daylight_index(self):
        index = self.job_length
        return index

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
        a = Job(d[i][0], d[i][1])
        jobs.append(a)
        i += 1

    return jobs

def print_jobs(jobs):
    l = len(jobs)
    i = 0
    while (i < l):
        print(f"Job {i}:")
        print(f"Name: {jobs[i].name}\nLength: {jobs[i].job_length}\n")
        i += 1

def myFunc(e):
    return e.daylight_index

def schedule_jobs(jobs):
    jobs.sort(key=myFunc)
    return jobs
