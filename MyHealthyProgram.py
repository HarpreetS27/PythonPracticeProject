import time
import datetime
from pygame import mixer

currentTime=time.strftime("%H:%M:%S")
print(currentTime)
start_Time="09:00:00"
end_Time="17:00:00"
print("Office Timings are : "+start_Time+" to "+end_Time)
# report=("Health Report : "+str(datetime.datetime.now().date())+".txt")
# print("Report"+"   "+report)

total_Working_Time=8*60  #in mins

water_To_Drink=input("Enter the water target (in ml) : ")
glass_Size=input("Enter the glass size(100/200/300 ml) : ")
no_of_Glasses_to_Drink=round(int(water_To_Drink)/int(glass_Size))
water_Interval=round(int(total_Working_Time)/int(no_of_Glasses_to_Drink))
water_Alarm="Brown Munde.mp3"

eyes_Excercise=input("Enter time duration(in mins) after which you want to relax eyes : ")
eyes_Interval=round(int(total_Working_Time)/int(eyes_Excercise))
eyes_Alarm="Brown Munde.mp3"

body_Excercise=input("Enter time duration(in mins) after which you want to do Body Stretch : ")
body_Interval=round(int(total_Working_Time)/int(body_Excercise))
body_Alarm="Brown Munde.mp3"



def musicPlay(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

def reminder_for_water():
    stop=""
    while stop!="DONE":
        musicPlay(water_Alarm)
        stop=input("Please drink your water, and type 'DONE' to stop the alarm ").upper()
        if stop=='DONE':
            f=open("Health_Report.txt","a")
            f.write("Water Drank at : "+str(datetime.datetime.now())+"\n")
            f.close()
            mixer.music.stop()
            time.sleep(int(water_Interval)*60)
            break

def reminder_for_eyes():
    stop = ""
    while stop != "DONE":
        musicPlay(eyes_Alarm)
        stop = input("Please relax your eyes, and type 'DONE' to stop the alarm ").upper()
        if stop == 'DONE':
            f=open("Health_Report.txt","a")
            f.write("Eyes relaxed at : " + str(datetime.datetime.now())+"\n")
            f.close()
            mixer.music.stop()
            time.sleep(int(eyes_Excercise)*60)
            break

def reminder_for_body():
    stop = ""
    while stop != "DONE":
        musicPlay(eyes_Alarm)
        stop = input("Please do stretching and type 'DONE' to stop the alarm ").upper()
        if stop == 'DONE':
            f=open("Health_Report.txt","a")
            f.write("Body exercises done at : " + str(datetime.datetime.now())+"\n")
            f.close()

            mixer.music.stop()
            time.sleep(int(body_Excercise)*60)
            break


try:
    while(currentTime>=start_Time and currentTime<=end_Time):
        print(currentTime+"       "+start_Time+"   "+end_Time)
        print("Set up Complete\n\n")
        print(f"You'll be notified for drinking water in every {water_Interval} minutes from {start_Time} to {end_Time}")
        print(f"You'll be notified for relaxing eyes in every {eyes_Excercise} minutes from {start_Time} to {end_Time}")
        print(f"You'll be notified for body stretching in every {body_Excercise} minutes from {start_Time} to {end_Time}")

        reminder_for_water()
        reminder_for_eyes()
        reminder_for_body()

    print("Sorry, Out of Business Hours.Your alarm will be set from 9am to 5 pm")

except Exception as e:
    print(e)