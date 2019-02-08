# Made in Yoo Hyeong Jun 
# github : https://github.com/cocopambag
# email : jhdf1234@naver.com

# import time library
import time 

# time.gmtime(time.time()) is returned current time.


input("In order to start stopwatch, Please press any key. : ")

now = time.gmtime(time.time())

input("In order to end stopwatch, Please press any key. : ")

last = time.gmtime(time.time())

# hour, minutes, second
# variable name of "minutes" is "mins" because "min" is keyword.
hour = last.tm_hour - now.tm_hour
mins = last.tm_min - now.tm_min
sec = last.tm_sec - now.tm_sec

# if minutes over negative number
if mins < 0:
    hour -= 1
    mins += 60

# if second over negative number    
if sec < 0:
    mins -= 1
    sec += 60

# Print minutes and seconds
print("{} minutes".format(hour*60 + mins))
print("{} seconds".format(sec))

# This is wait for display
input()
