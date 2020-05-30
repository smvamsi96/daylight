import lib as L
import Job as Job
# import TimeManagementUnit as T

def myFunc(e):
    return e.signature['daylight_index']


# TMU = T.TimeManagementUnit()
# a container for all the jobs
job_list = []
# load all the jobs from disk
job_list = L.loadFromDisk()



L.printJobs(job_list)

L.saveToDisk(job_list)
