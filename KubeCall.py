#Use py -3.10 KubeCall.py to run

import os, sys
import importlib.util
import http.client
import subprocess
import time
from kubernetes import client, config

#Create deployment
os.system("kubectl apply -f fastchatdep.yaml")

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

#Enter pod
podNameIndex = strPodCheck.index("fastchatdep-")
#It's always 27 characters, fastchatdep-9 numbers-5 alphanumeric
podNameLength = 27
podName = strPodCheck[podNameIndex:podNameIndex+podNameLength]
print(podName)

os.system("kubectl exec -it " + podName + " -- /bin/bash")
time.sleep(3) #Bad practice

#Manually start Fastchat

#os.system("python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5")
#Program is halted while I'm ssh'ed into the server. Above line doesn't work as-is.

#Execute Fastchat prompt
prompt = "Among us"
#print(subprocess.check_output(prompt))


#End program

#os.system("exit")
#Above line does not activate on server.

os.system("kubectl delete deployments fastchatdep")