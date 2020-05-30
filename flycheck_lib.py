import json
from Job import Job




def addJob(job_list):
    signature = {}
    signature['name'] = input("Enter Job Name: ")
    signature['job_length'] = input("Enter Job Length: ")
    job = Job(signature)
    priority = binary_search(job_list, job, 0, len(job_list)-1)
    job.setPriority(priority)
    job_list.insert(priority, job)






def saveToDisk(job_list, file_name='jobs.json'):
    """convert an array of jobs to json"""
    signature_container = []
    for job in job_list:
        # the signature of a job is collection of its unique attributes
        signature_container.append(job.signature)
    with open(file_name, 'w') as dump_file:
        json.dump(signature_container, dump_file)





def loadFromDisk(file_name='jobs.json'):
    """convert a json of jobs to a job array"""
    signature_container = []
    with open(file_name) as dump_file:
        signature_container = json.load(dump_file)
    job_list = []
    for signature in signature_container:
        job = Job(signature)
        job.setPriority(signature['priority'])
        determineRoutine(job)
        job_list.append(job)
    quickSortJobs(job_list, 0, len(job_list)-1)
    updatePriority(job_list)
    
    return job_list




def isLessThan(a, b):
    if (bool(a.signature['priority'] == 9999) ^ bool(b.signature['priority'] == 9999)):
        if (input(f"is \"{b.signature['name']}\" > \"{a.signature['name']}\": ") == 'y'):
            return True
        else:
            return False
    else:
        if (a.signature['priority'] <= b.signature['priority']):
            return True
        else:
            return False





def printJobs(job_list):
    i = 0
    for job in job_list:
        print(f"Job {i}:")
        print(f"Tags: {job.signature['tags']}")
        print(f"Name: {job.signature['name']}\nLength: {job.signature['job_length']}\nStarts at: {job.get_base()}\nFinishes at: {job.get_bound()}\n")
        i += 1




def isRoutine(job):
    if ('Routine' in job.signature['tags']):
        return True
    return False

def determineRoutine(job):
    if isRoutine(job):
        job.base = input(f'when should {job.name} start: ')
        job.bound = input(f'when should {job.name} end: ')

def updatePriority(jobs):
    i = 0
    for job in jobs:
        job.signature['priority'] = i
        i += 1




#############################################################
### This Section of Code is directly lifted from the web ####
#############################################################

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]
    for j in range(low , high): 
        if (isLessThan(arr[j], pivot)): 
            i = i+1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1] ,arr[high] = arr[high] ,arr[i+1]
    return ( i+1 ) 
  
def quickSortJobs(arr,low,high): 
    if low < high: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before
        # partition and after partition
        quickSortJobs(arr, low, pi-1)
        quickSortJobs(arr, pi+1, high)








def binary_search(arr, val, start, end):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if isLessThan(val, arr[start]):
            return start
        return start+1

    # this occurs if we are moving beyond left's boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
        return start

    mid = int((start+end)/2)
    if isLessThan(arr[mid], val):
        return binary_search(arr, val, mid+1, end)
    if isLessThan(val, arr[mid]):
        return binary_search(arr, val, start, mid-1)
    return mid
