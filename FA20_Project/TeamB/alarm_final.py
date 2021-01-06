import datetime
import os
import time
import random
import webbrowser
import sys
from datetime import datetime
from datetime import timedelta


#Checks to see if the user has entered in a valid alarm time"""
def check_alarm_input(alarm_time):
    if len(alarm_time) == 1: # [Hour] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2: # [Hour:Minute] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0 and \
           alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False


def check_alarm_input2(alarm_time):
    if len(alarm_time) == 1: # [Hour] Format
        if alarm_time[0] < 60 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2: # [Hour:Minute] Format
        if alarm_time[0] < 60 and alarm_time[0] >= 0 and \
                alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                alarm_time[1] < 60 and alarm_time[1] >= 0 and \
                alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True

    raise ValueError
    return False


def calculate_time(alarm_time, now):
    # Convert the alarm time from [H:M] or [H:M:S] to seconds
    seconds_hms = [3600, 60, 1] 
    alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

    # Get the current time of day in seconds
    now = datetime.now()
    current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

    # Calculate the number of seconds until alarm goes off
    time_diff_seconds = alarm_seconds - current_time_seconds

    # If time difference is negative, set alarm for next day
    if time_diff_seconds < 0:
        time_diff_seconds += 86400 # number of seconds in a day

    # Display the amount of time until the alarm goes off
    print("\nAlarm set to go off in %s" % timedelta(seconds=time_diff_seconds))

    # Sleep until the alarm goes off

    return time_diff_seconds


#Create playlists and add songs
def create_playlist():
    cnt = 0
    global genreNames_array
    genreNames_array = []
    global link_array
    link_array = []

    add = input("\nCreate a new playlist?\n1. Yes   2. No\nEnter your choice: ")
    if add == "2":
        managing_list()

    while add == "1":
        genreName = input("\nEnter the title: ")
        genreNames_array.append(genreName)

        # If video URL file does not exist, create one
        if not os.path.isfile(genreName):
            print('...Creating ' + genreName + ' list for you...')
            with open(genreName+'.txt', "w") as alarm_file:
                alarm_file.write(genreName)

        ans = input("\nAdd a new song to [" + genreName + "] playlist?\n"
                "1. Yes     2. No\nEnter your choice: ")

        while ans == "1":
            link = input("\nEnter the YouTube link: ")
            text_file = open(genreName+'.txt', "a+")
            text_file.write("\n" + link)
            link_array.append(link)
            print("\nAdd more songs to [" + genreName + "] playlist?")
            ans = input("1. Yes   2. No\nEnter your choice: ")

        text_file.close()

        add = input("\nCreate another playlist?\n1. Yes    2. No\nEnter your choice: ")
        if add == "2":
            managing_list()


#Show the playlists
def show_playlist():
    cnt = 0
    print("\nHere is your playlists")
    for x in range(len(genreNames_array)):
        print(str(cnt+1) + ". " + genreNames_array[cnt])
        cnt += 1

    ans = int(input("\nEnter the number to see all links: "))
    openFile = genreNames_array[ans-1]
    text_file = open(openFile + '.txt', "r")
    Lines = text_file.readlines()[1:]

    print("\n*** Here is the link for [" + openFile + "] playlist ***")
    count = 0
    for line in Lines:
        print("Link{}: {}".format(count+1, line.strip()))
        count += 1
    text_file.close()
    managing_list()


#Set up for the alarm
def setup_alarm():
    cnt = 0
    print("\nThe song will be randomly selected from the playlist you choose")
    print("** My music lists **")
    for x in range(len(genreNames_array)):
        print(str(cnt + 1) + ". " + genreNames_array[cnt])
        cnt += 1
    print("********************")

    ans = int(input("\nEnter your choice:  "))

    now, start_time = setting_time()
    time_stamp, end_time = resetting_time()
    time_diff_seconds = calculate_time(start_time, now)
    countDown(time_diff_seconds)
    print("Wake Up!")

    # Load list of possible video URLs
    genre = genreNames_array[ans - 1]
    fileToOpen = random_line(genre + ".txt")
    with open(genre + ".txt", "r") as alarm_file:
        videos = fileToOpen

    # Open a random video from the list
    link = resetting_link(videos, time_stamp)
    webbrowser.open(link)
    close_web(end_time)


#Getting random line
def random_line(fname):
    with open(fname) as f:
        lines = f.readlines()[1:]
        myline = random.choice(lines)
        return myline


def open_web(link):
    now, start_time = setting_time()
    time_diff_seconds = calculate_time(start_time, now)

    countDown(time_diff_seconds)
    print("\nTime's up!")
    webbrowser.open(link)


def close_web(end_time):
    time.sleep(end_time)
    print("\nTime to stop the song!")
    os.system("killall 'Google Chrome'")


def setting_link():
    print("\n\n===================================")
    print("  [ Setting the websites ]")
    print("===================================")
    print("1. De Anza Canvas")
    print("2. Zoom")
    print("3. Youtube")
    num = int(input("\nEnter the number >> "))

    if num == 1:
        link = "https://deanza.instructure.com/"
        open_web(link)

    elif num == 2:
        link = "https://zoom.us/"
        open_web(link)

    elif num == 3:
        link = "null"
        managing_list()

    else:
        print("Invalid input!")

    return link


def resetting_link(link,time):
    # check_alarm_input(time_stamp)
    time = [int(n) for n in time.split(":")]
    if check_alarm_input2(time):
        if len(time) == 1: # [minute] Format
            if time[0] < 60 and time[0] >= 0:
                link = link + "&t" + "=" + str(time[0]*60) + "s"
        if len(time) == 2: # [minute:seconds] Format
            if time[0] < 60 and time[0] >= 0 and \
                    time[1] < 60 and time[1] >= 0:
                link = link + "&t" +"=" + str(time[0]*60 + time[1])  + "s"
                # print(link)
        elif len(time) == 3: # [Hour:Minute:Second] Format
            if time[0] < 24 and time[0] >= 0 and \
                    time[1] < 60 and time[1] >= 0 and \
                    time[2] < 60 and time[2] >= 0:
                link = link + "&t"+ "=" + str(time[0]*3600 + time[1]*60 + time[2])  + "s"
        else:
            print("Error time_stamp output!!!")
    else:
        print("Error time_stamp output!!!")
    return link


def setting_time():
    print("\n\n===================================")
    print("   [ Setting the alarm time ]")
    print("===================================")
    print("\nSet a time in HH:MM or HH:MM:SS format")
    now = datetime.now()
    print("It's", now.strftime("%H:%M:%S"), "now")

    while True:
        alarm_input = input(" >> ")
        try:
            start_time = [int(n) for n in alarm_input.split(":")]
            if check_alarm_input(start_time):
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Enter time in HH:MM or HH:MM:SS format")

    return [now, start_time]


def resetting_time():
    print("\nSet the start point for the video")
    time_stamp = input("Where to start (M:SS) >> ")


    print("\nSet the duration of the video")
    while True:
        end_time = input("How long to play (How many seconds?) >> ")
 
        try:
            end_time = float(end_time)
            break
        except ValueError:
            print('Please enter in a number.\n')
            
    return [time_stamp, end_time]


def countDown(time_diff_seconds):
    if time_diff_seconds <= 30:
        i = 0
        while time_diff_seconds>0:
            print("00 :","%02d"% float(time_diff_seconds-1) )
            time.sleep(1)

            time_diff_seconds= time_diff_seconds-1
    else:
        time.sleep(time_diff_seconds-30)
        i = 30
        while i>0:
            print("00 :","%02d"% float(i))
            time.sleep(1)
            i= i-1


def managing_list():
    print("\n\n======= Managing YouTube playlists =======")
    print("1. Make a new playlist\n2. Show my playlists\n3. Set the time for the alarm.\n4. Done")
    ans = input("\nEnter your choice: ")
    while ans != "4":
     if ans == "1":
        create_playlist()
     elif ans == "2":
        show_playlist()
     elif ans == "3":
        setup_alarm()
        ans = "4"
        break
     else:
        print("Invalid input! Please try again.")

    if ans == "4":
        print("\nBye! Have a good day.")
        exit()

def main():
    setting_link()

if __name__ == "__main__":
    main()


