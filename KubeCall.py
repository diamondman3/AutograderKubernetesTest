#Use py -3.10 KubeCall.py to run
#I might need to make that time.sleep even longer, but for now, just run this on an existing deployment

import os, sys
import importlib.util
import http.client
import subprocess
import time
from kubernetes import client, config

def runTest(existingDep):
    #Create deployment
    if not existingDep:
        subprocess.run(["kubectl", "apply", "-f", "fastchatdep.yaml"])

    #Wait for pod to be ready
    podReady = False
    podCheck = ""
    strPodCheck = ""
    while not podReady:
        podCheck = subprocess.check_output(['kubectl', 'get', 'pods'])
        strPodCheck = podCheck.decode("utf-8")
        if 'Running' in strPodCheck:
            podReady = True
    print(strPodCheck)

    #Enter pod and start fastchat
    podNameIndex = strPodCheck.index("fastchatdep-")
    #It's always 27 characters, fastchatdep-9 numbers-5 alphanumeric
    podNameLength = 27
    podName = strPodCheck[podNameIndex:podNameIndex+podNameLength]

    if not existingDep:
        time.sleep(30) #Takes a real long time to download fastchat
    os.system("kubectl exec -it " + podName + " -- python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5")
    #Runs out of memory when executed.

    #Execute Fastchat prompt
    prompt = "Among us"
    #print(subprocess.check_output(prompt))


    #End program

    #os.system("exit")
    #Above line does not activate on server.
    if not existingDep:
        os.system("kubectl delete deployments fastchatdep")
        

#Actually run from command line
runTest(True)