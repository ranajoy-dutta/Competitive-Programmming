def timeConversion(time):
    if time[-2:] == "AM" and time[:2] == "12":        #12 at Night
        return "00"+time[2:-2]
    elif time[-2:] == "AM":                  
        return time[:-2]
    elif time[-2:] == "PM" and time[:2] == "12":      #12 at Noon
        return time[:-2]
    else:
        return str(int(time[:2]) + 12) + time[2:8]    #converting to 24 hrs by adding 12 hrs

s = input().strip()
print(timeConversion(s))

