'''
Will take in the users hours, mins and seconds and will display a clock wich wil count down, making sure to redue the time when applicable
TODO Could add a clock and turn it into a command line tool with some nice looking command line trickery
'''
from time import sleep

def doClock(hours, mins, secs):
    if hours == mins == secs == 0:
        return
    while True:
        sleep(1)
        secs -= 1
        if hours == 0 and mins == 0 and secs == 0:
            break
        print(f"Time Remaining: {hours} hours, {mins} mins, {secs} secs")
        if secs == 0:
            secs = 60
            if mins != 0:
                mins -= 1
            if mins == 0 and secs == 60:
                mins = 59
                if hours != 0:
                    hours -= 1
    print("TIME FINISHED")
    

while True: 
    userTime = input("Please enter the time needed, using ':' ").split(":")
    if userTime[0].isnumeric() and userTime[1].isnumeric() and userTime[2].isnumeric():
        hours, mins, secs = int(userTime[0]), int(userTime[1]), int(userTime[2])
        if mins >= 0 and mins < 60 and  secs >= 0 and secs:
            doClock(hours, mins, secs)
            
