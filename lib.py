import json
from Job import Job




def addJob():
    name = input("Enter Job Name: ")
    job_length = input("Enter Job Length: ")
    j = Job(name, job_length)
    return j





def saveToDisk(job_list, file_name='jobs.json'):
    """convert an array of jobs to json"""
    i = 0
    signature_container = []
    while (i < len(job_list)):
        # the signature of a job is collection of its unique attributes
        signature = []
        signature.append(job_list[i].name)
        signature.append(job_list[i].job_length)
        signature_container.append(signature)
        i += 1
    with open(file_name, 'w') as dump_file:
        json.dump(signature_container, dump_file)





def loadFromDisk(file_name='jobs.json'):
    """convert a json of jobs to a job array"""
    signature_container = []
    with open(file_name) as dump_file:
        signature_container = json.load(dump_file)
    job_list = []
    i = 0
    while (i < len(signature_container)):
        new_job = Job(signature_container[i][0], signature_container[i][1])
        job_list.append(new_job)
        i += 1
    return job_list





def printJobs(jobs):
    i = 0
    while (i < len(jobs)):
        print(f"Job {i}:")
        print(f"Name: {jobs[i].name}\nLength: {jobs[i].job_length}\nStarts at: {jobs[i].get_base()}\nFinishes at: {jobs[i].get_bound()}\n")
        i += 1

#############################################################
### This Section of Code is directly lifted from the web ####
#############################################################

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
