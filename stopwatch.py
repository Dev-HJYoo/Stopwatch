import time

input("시작하기 위해서 아무키나 입력하세요")

now = time.gmtime(time.time())

input("끝내기 위해서 아무키나 입력하세요")

last = time.gmtime(time.time())

    
hour = last.tm_hour - now.tm_hour
mins = last.tm_min - now.tm_min
sec = last.tm_sec - now.tm_sec

if mins < 0:
    hour -= 1
    mins += 60

print("{} 분".format(hour*60 + mins))
print("{} 초".format(sec))

input()
