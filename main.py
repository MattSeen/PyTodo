##################
## PyTodo List
##################
import datetime
import os

guiSize = 20
taskList = {}

clear = lambda: os.system('cls')

def header():
    print ""
    print "#"*guiSize
    print "# ToDo List"
    print "#"*guiSize
    print ""

def printGUI():
    clear()
    header()
    
    if(len(taskList) != 0):
        for key, value in taskList.iteritems():
            print key, timeSinceStamp(value)
    else:
        print "Yay, no tasks!"
    print ""

def timeSinceStamp(taskTime):
    timeNow = datetime.datetime.now()
    timeSince = timeNow - taskTime
    return timeSince
    
def refresh():
    print ""
    print "No Refresh Function Yet"
    
def addEntry():
    print "." * guiSize
    print ""
    newTaskName = raw_input("Enter a new for your new task: ")
    if( newTaskName != ""):
        taskList[newTaskName] = datetime.datetime.now()

def deleteEntry():
    count = 1
    indexList = {}
    for key, value in taskList.iteritems():
        print count, key, timeSinceStamp(value)
        indexList[count] = key
        count += 1
    
    print ""
    taskToRemove = raw_input("Choose a task to remove: ")
    
    del(taskList[indexList[int(taskToRemove)]])
        
def mainLoop():
    while(1):
        printGUI()
        print "1) Refresh"
        print "2) New Entry"
        print "3) Delete Entry"
        print "q) Exit"
        print ""

        action = raw_input("Choose an option: ")        
        
        if(action == "q"):
            break #Kill program
            
        performAction[int(action)]()

performAction = {
    1: refresh,
    2: addEntry,
    3: deleteEntry
    }

if __name__ == '__main__':
    mainLoop()