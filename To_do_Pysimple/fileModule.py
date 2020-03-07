file = "/home/grimreaper/Workspace/python/file.txt"
completedFile = "/home/grimreaper/Workspace/python/completed.txt"

def readFile():
    with open(file,"r") \
            as f:
        lis = f.read().splitlines()
    return lis

def readCompleted():
    with open(completedFile,"r") \
            as f:
        complete = f.read().splitlines()
    return complete

def writeToFile(liss):
    with open(file,"w") as f:
        for i in range(len(liss)):
            f.write(liss[i])
            f.write("\n")

def writeToCompleted(liss):
    with open(completedFile,"w") as f:
        for i in range(len(liss)):
            f.write(liss[i])
            f.write("\n")
