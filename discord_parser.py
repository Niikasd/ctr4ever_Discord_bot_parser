from datetime import datetime
import time


unixdate = 0
lap = 0
lineN = 0
tracks = {
    "Crash Cove":1,
    "Roo Tubes":3,
    "Roo's Tubes":3,
    "Tiger Temple":5,
    "Coco Park":7,
    "Mystery Caves":9,
    "Blizzard Bluff":11,
    "Sewer Speedway":13,
    "Dingo Canyon":15,
    "Papu Pyramid":17,
    "Papu's Pyramid":17,
    "Dragon Mines":19,
    "Polar Pass":21,
    "Cortex Castle":23,
    "Tiny Arena":25,
    "Hot Air Skyway":27,
    "N.Gin Labs":29,
    "N. Gin Labs":29,
    "Oxide Station":31,
    "Slide Coliseum":33,
    "Turbo Track":35
}
storage = []
def scoreConvert(timeStr):
    lengthValue = len(timeStr)
    if lengthValue <7:
        seconds = int(timeStr[0:2])
        sentis = int(timeStr[4:6])
        score=seconds*100+sentis
        return(score)
    else:
        minutes = int(timeStr[0])
        seconds = int(timeStr[2:4])
        sentis = int(timeStr[6:8])       
        score = (minutes*6000)+(seconds*100)+sentis
        return(score)


with open("messages.txt") as file:
    #first loop runs through the messages and gathers all times submitted before the country name bug was fixed.
    for line in file:
        lineN+=1
        #skips pointless lines
        if line == "Records Bot\n":
            print("skipped RB line on line "+str(lineN)+".\n")
            continue
        if line == "BOT\n":
            print("skipped BOT line on line "+str(lineN)+".\n")
            continue
        lineLen = len(line)
        key = line[0]
        #updates the date.
        if key == " ":
            dateStr = line[5:15]
            dateSet = datetime.strptime(dateStr, '%m/%d/%Y')
            unixdate = int(time.mktime(dateSet.timetuple()))
            print("Set date as "+ str(dateSet)+" on line "+str(lineN)+".\n")
            continue
        key2 = line[lineLen-2]
        #gets whether it is a lap or a course.
        if key2 == ")":
            if lineLen < 40:
                selection = line[14:lineLen-1]
                if(selection[-2])=="p":
                    lap = 1
                    subSelect = 6
                if(selection[-2])=="e":
                    lap = 0
                    subSelect = 9
                track = selection[0:-(subSelect)]
                trackID = tracks[track]+lap
                print("TrackID is "+str(trackID)+" on line "+str(lineN)+".\n")
        #gets the user and score.
            else:
                nameEnd = line.find(", ")
                name = line[0:nameEnd]
                if "United" in name:
                    name = name[0:-7]
                scoreStart = line.find("time of ")+8
                scoreEnd = line.find(", has")
                scoreRaw = line[scoreStart:scoreEnd]
                databaseScore = scoreConvert(scoreRaw)
                storage.append([lineN, name, unixdate, trackID, databaseScore])
        elif key2 == "p":
            #once the bot detects a "p" in key2 location, it means that the bot update was reached.
            print("Reached bot update")
            break
    #second loop is a while loop to keep reading from the same location.
    #open for suggestions for how to do this better.
    while True:
        lineN+=1
        line = file.readline()
        #skips pointless lines
        if line == "Records Bot\n":
            print("skipped RB line on line "+str(lineN)+".\n")
            continue
        if line == "BOT\n":
            print("skipped BOT line on line "+str(lineN)+".\n")
            continue
        if len(line) < 1:
            break
        key = line[0]
        if key == " ":
            dateStr = line[5:15]
            dateSet = datetime.strptime(dateStr, '%m/%d/%Y')
            unixdate = int(time.mktime(dateSet.timetuple()))
            print("Set date as "+ str(dateSet)+" on line "+str(lineN)+".\n")
            continue
        lineLen = len(line)
        #gets track, course/lap, score, and username.
        if lineLen> 43:
            key2 = line[-11]
            if key2 == "-":
                lap = 1
                subSelect = 12
            elif key2 == " ":
                if line[-10] == "-":
                    lap = 1
                    subSelect = 11
                else:
                    lap = 0
                    subSelect = 1
            else:
                lap = 0
                subSelect = 1
            trackStart = line.find("place in ")+9
            trackStr = line[trackStart:-(subSelect)]
            trackID = tracks[trackStr]+lap
            print("TrackID is "+str(trackID)+" on line "+str(lineN)+".\n")
            scoreStart = line.find("time of ")+8
            scoreEnd = line.find(", has")
            scoreRaw = line[scoreStart:scoreEnd]
            databaseScore = scoreConvert(scoreRaw)            
            nameEnd = line.find(", with")-9
            name = line[0:nameEnd]
            storage.append([lineN, name, unixdate, trackID, databaseScore])


for i in storage:
    print(i)





