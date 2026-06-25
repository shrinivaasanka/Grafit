##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
##############################################################################################################################################
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://acadpdrafts.readthedocs.io
##############################################################################################################################################

from collections import defaultdict
from collections import deque
from threading import Thread
import psutil
import random
import time
import sys
import asyncio
import subprocess
import os
import json

dynamic_hashmap_dict=defaultdict(list)
cpuwqdict=defaultdict(list)
pid2cpudict=defaultdict(str)
process_queue=deque()
elapsedclockticks=0


def clockticks():
#async def clockticks():
    global elapsedclockticks
    while True:
        elapsedclockticks += 1 
        print("clockticks(): elapsedclockticks = ",elapsedclockticks)
        time.sleep(1)
        #await asyncio.sleep(1)

def countdown_keys():
#async def countdown_keys():
    global dynamic_hashmap_dict
    while True:
        new_dynamic_hashmap_dict=defaultdict(list)
        dynamic_hashmap_dict_keys=dynamic_hashmap_dict.keys()
        print("dynamic_hashmap_dict_keys:",list(dynamic_hashmap_dict_keys))
        for k in list(dynamic_hashmap_dict_keys):
            if k > 0:
            	new_dynamic_hashmap_dict[k-1] = dynamic_hashmap_dict.pop(k)
            else:
                print("Timed out processes:",dynamic_hashmap_dict.pop(k))
        dynamic_hashmap_dict=new_dynamic_hashmap_dict
        print("countdown_keys(): dynamic_hashmap_dict = ",new_dynamic_hashmap_dict)
        time.sleep(1)
        #await asyncio.sleep(1)

def survival_index_scheduler():
#async def survival_index_scheduler():
    global elapsedclockticks
    global dynamic_hashmap_dict
    global cpuwqdict
    global pid2cpudict
    cpuid=-1
    while True:
        subprocess.run(["echo","workqueue:workqueue_queue_work",">","/sys/kernel/tracing/set_event"],capture_output=True)
        subprocess.run(["cp","/sys/kernel/tracing/trace","./workqueue_trace"],capture_output=True)
        wqtrace=open("./workqueue_trace")
        for task in wqtrace:
          tasktoks=task.split(" ") 
          tasktoks=list(filter(lambda x: x != '',tasktoks))
          print("tasktoks:",tasktoks)
          if tasktoks[0].strip() != "#":
              for tok in tasktoks:
                  if tok.startswith("[0") and tok.endswith("]"):
                      cpuid=tok
              print("cpuid:",cpuid)
              if tasktoks[0] not in cpuwqdict[cpuid]:
                  cpuwqdict[cpuid].append(tasktoks[0])
          pidtoks=tasktoks[0].split("-")
          print("pidtoks:",pidtoks)
          if len(pidtoks) > 1:
             pid2cpudict[pidtoks[1]]=cpuid
          else:
             pid2cpudict[tasktoks[0]]=cpuid
          print("pid2cpudict=",pid2cpudict)
        print("CPU ----------  workqueue")
        for k,v in cpuwqdict.items():
             print(k,"-----------",v)
        print("PID ------------ CPU",pid2cpudict)
        try:
            process=process_queue.popleft()
        except IndexError:
            print("IndexError")
            #continue
        dynamic_hashmap_dict[process[1]].append((process[0],pid2cpudict[process[0]]))
        print("survival_index_scheduler(): dynamic_hashmap_dict = ",dynamic_hashmap_dict)
        print("survival_index_scheduler(): pid2cpudict = ",pid2cpudict)
        kernelanalyticsf=open("./virgo_kernel_analytics.conf","a")
        for k,v in dynamic_hashmap_dict.items():
            kernelanalyticsf.write(str(k) + " ---- " + str(v) + "\n")
        kernelanalyticsf.write(" --------------------------------------------- ")
        kernelanalyticsf.write("\n")
        kernelanalyticsf.close()
        time.sleep(1)
        #await asyncio.sleep(1)

#def process_stream():
#async def process_stream():
#    processes=subprocess.run(["ps","-eafo","pid,cls"],capture_output=True)
#    pidsched=processes.stdout.decode("utf-8").strip().split("\n")
#    for p in pidsched[1:]:
#        ptoks=p.split()
#        process_id=ptoks[0]
#        sched_policy=ptoks[1]
#        if sched_policy=="DLN":
#            schedparams=subprocess.run(["chrt","-p",process_id],capture_output=True)
#            print(schedparams)
#            schedparamstoks=schedparams.stdout.decode("utf-8").strip().split("\n")
#            deadlinestring=schedparamstoks[2].split(":")
#            deadlinestringtoks=deadlinestring[1].split("/")
#            print("deadlinestringtoks:",deadlinestringtoks)
#            deadline=deadlinestringtoks[1]
#            process_queue.append((process_id,int(deadline)))
#        print("process_stream(): process_queue = ", process_queue)
#        time.sleep(1)
#        #await asyncio.sleep(1)

#async def process_stream():
def process_stream():
    global cpuwqdict
    while True:
        processes=subprocess.run(["ps","-eafo","pid,cls"],capture_output=True)
        pidsched=processes.stdout.decode("utf-8").strip().split("\n")
        for p in pidsched[1:]:
          ptoks=p.split()
          process_id=ptoks[0]
          sched_policy=ptoks[1]
          print("sched_policy:",sched_policy)
          if sched_policy=="DLN":
              schedparams=subprocess.run(["chrt","-p",process_id],capture_output=True)
              print(schedparams)
              schedparamstoks=schedparams.stdout.decode("utf-8").strip().split("\n")
              deadlinestring=schedparamstoks[2].split(":")
              deadlinestringtoks=deadlinestring[1].split("/")
              print("deadlinestringtoks:",deadlinestringtoks)
              deadline=deadlinestringtoks[1]
              process_queue.append((process_id,int(deadline)))
          else:
              process_queue.append((process_id,sys.maxsize))
        print("process_stream(): process_queue = ", process_queue)
        time.sleep(1)
        #await asyncio.sleep(1)

def spawn_processes(no_of_processes):
    #SCHED_DEADLINE chrt example (runtime < deadline < period):
    #----------------------------------------------------------
    #chrt -d --sched-runtime 1000000 --sched-deadline 5000000 --sched-period 5000000 -p 0 <pid>
    #chrt -d --sched-runtime 1000000 --sched-deadline 5000000 --sched-period 5000000 0 <processname>
    envdeadline=os.environ["DEADLINE"]
    envruntime=os.environ["RUNTIME"]
    envperiod=os.environ["PERIOD"]
    for n in range(no_of_processes):
        #os.system("chrt -d --sched-runtime 1000000 --sched-deadline 5000000 --sched-period 5000000 0 python3.13 SurvivalIndexScheduler_process.py&")
        os.system("chrt -d --sched-runtime "+envruntime+" --sched-deadline "+envdeadline+" --sched-period "+envperiod+" 0 python3.13 SurvivalIndexScheduler_process.py&")

if __name__=="__main__":
    sys.setswitchinterval(0.01)
    spawn_processes(5)
    thread1 = Thread(target=process_stream)
    thread2 = Thread(target=clockticks)
    thread3 = Thread(target=survival_index_scheduler)
    thread4 = Thread(target=countdown_keys)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    #asyncio.run(process_stream())
    #asyncio.run(clockticks())
    #asyncio.run(survival_index_scheduler())
    #asyncio.run(countdown_keys())
