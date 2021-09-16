# epoch == a date and time from which a computer measures system time (thinks time began)
import time

#print(time.ctime())  # current computer time
#print(time.ctime(0))  # converts time expressed in seconds since epoch into a readable string
#print(time.ctime(1000000))

#print(time.time())  # current seconds that have passed since epoch

#print(time.ctime(time.time()))  # gives current time

time_object = time.localtime()
print(time_object)
local_time = time.strftime('%B %d %Y %H:%M:%S',time_object) # time.strftime(format,time object)
print(local_time)

t_object = time.gmtime()
utc_time = time.strftime('%B %d %Y %H:%M:%S',t_object)
print(utc_time)

time_string = '27 August, 2021 11:25:00'
time_object = time.strptime(time_string,'%d %B, %Y %H:%M:%S')  # strptime(string,format), convert time string into time object
print(time_object)

# (year, mon, day, hour, min, sec, wday, yday, isdst)
time_tuple = (2021, 8, 27, 11, 32, 0, 0, 0, 0) # fill all fields
time_string = time.asctime(time_tuple) # asctime(tuple) # converts a time tuple representation into a readable string
print(time_string)

time_string = time.mktime(time_tuple)  # converts tuple to seconds since epic
print(time_string)
