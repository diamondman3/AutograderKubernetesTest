#Use py -3.10 KubeCall.py to run
#I might need to make that time.sleep even longer, but for now, just run this on an existing deployment

"""
llm shell commands through kubectl notes

Attempting to use "llm chat" from another computer crashes the llm program
Attempting to use llm -m [MODEL] prompt with an invalid model causes an error, but does stop the program
Can't do cd through -i without -it

"""

import os, sys
import importlib.util
import http.client
import subprocess
import time
from kubernetes import client, config

def runTest(existingDep):
    #Create deployment
    if not existingDep:
        subprocess.run(["kubectl", "apply", "-f", "llmdep.yaml"])

#        subprocess.run(["kubectl", "apply", "-f", "fastchatdep.yaml"])

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
    print(strPodCheck)
    podNameIndex = strPodCheck.index("llmdep-")
    #It's always 23 characters, llmdep-9 numbers-5 alphanumeric
    podNameLength = 23
    podName = strPodCheck[podNameIndex:podNameIndex+podNameLength]

    if not existingDep:
        print("Loading", end = "")
        for i in range(1, 10):
            time.sleep(60) #Takes like 10 minutes to start up
            print (".", end = "")

    #Execute Fastchat prompt
    prompt = "Among us"
#    os.system("kubectl exec -i " + podName + " -- python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5")
    os.system("kubectl exec -i " + podName + " -- llm install llm-gpt4all") #-i means only use standard input, -t means actually accesing the pod. IT'S THAT EASY.
    
    print("Attempting to pass in prompt...")

    os.system("kubectl exec -i " + podName + " -- llm -m orca-mini-3b \"test\"") #These commands work fine outside python, hangs here



    #End program

    #os.system("exit")
    #Above line does not activate on server.
    if not existingDep:
        os.system("kubectl delete deployments llmdep")
        

#Actually run from command line
runTest(True)