import time

with open("test.txt","w") as f:
    st=time.time()
    f.write(str(st))