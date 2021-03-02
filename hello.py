print("hello,jenkins")
print("start build")
print("building")
#print("running shell,python")
#print("success")
#print("waiting for test")

import os
os.system('python /var/lib/jenkins/workspace/develop_main/algorithm.py')
