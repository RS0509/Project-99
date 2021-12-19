import shutil
import os
import time
path = '/MyPythonProjects'
days = 30

days = time.time()
if os.path.exists(path):
    files = os.walk(path)
    name,ext = os.path.splitext(files)
    os.path.join(path + name)
    ctime = os.stat(path).st_ctime

    if(ctime > days):
        isFile = os.path.isfile(path)
        if(isFile == True):
            os.remove(path)
        else: 
            shutil.rmtree(path)
         
else:
    print("Not Found")
