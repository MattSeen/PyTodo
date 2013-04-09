#! C:/Python27/python.exe
##################
## PyTodo List
##################
import datetime
import os

guiSize = 40
taskList = {}


class taskObj:
    """docstring for taskObj"""
    text = ""
    startDate = ""

    def __init__(self, text, startDate):
        self.text = text
        self.startDate = startDate


clear = lambda: os.system('cls')


def header():
    print ""
    print "#" * guiSize
    print "TODO List".center(guiSize)
    print ":)".center(guiSize)
    print "#" * guiSize
    print ""


def printGUI():
    clear()
    header()

    if(len(taskList) != 0):
        for key, value in taskList.iteritems():
            print value.text, timeSinceStamp(value.startDate)
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
    if(newTaskName != ""):
        taskList[len(taskList)] = taskObj(newTaskName, datetime.datetime.now())


def deleteEntry():
    count = 1
    indexList = {}
    for key, value in taskList.iteritems():
        print count, value.text, timeSinceStamp(value.startDate)
        indexList[count] = key
        count += 1

    print ""
    if(len(taskList) != 0):
        try:
            taskToRemove = int(raw_input("Choose a task to remove: "))

            if(taskToRemove in indexList):
                del(taskList[indexList[int(taskToRemove)]])
        except ValueError:
            print 'I cannot delete that task'
            raw_input("Press enter to continue")


def mainLoop():
    while(1):
        printGUI()
        print "1) Refresh"
        print "2) New Entry"
        print "3) Delete Entry"
        print "0) Exit"
        print ""

        action = raw_input("Choose an option: ")

        try:
            if (int(action) in performAction):
                performAction[int(action)]()
            elif(int(action) == 0):
                break
            else:
                print "@....<--- tumble weed"
        except ValueError:
            print 'Please supply integer arguments'
            raw_input("Press enter to continue")


performAction = {
    1: refresh,
    2: addEntry,
    3: deleteEntry
}

if __name__ == '__main__':
    mainLoop()
