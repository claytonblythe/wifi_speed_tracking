# This is a program to plot the data that was collected from the crontab script
# of my home's wireless speed. Requires that speedtest-cli is installed for
# testing wireless speed through terminal

#import the necessary libraries
# of my home's wireless speed. Requires that speedtest-cli is installed for
# testing wireless speed through terminal

#clean up the wirless log file
import os, pandas as pd
count = 0
clean_data = ""

with open("wireless_speeds.log", "r") as f:
    lines = f.readlines()
#print(lines)

for i in range(0,len(lines)):
    if lines[i][3:7] == lines[i-1][3:7]:
        pass
    else:
        clean_data += lines[i]

#print(clean_data)
file1 = open("clean_wireless.log","w")
file1.write(clean_data)
file1.close()


#import the necessary libraries
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter, HourLocator
import matplotlib.dates
import time
import os
import matplotlib.dates

#create a list from a text file (column format) where the wireless tests are logged
# format is time string, then under it is Download speed, then under it is Upload Speed
base_path = os.path.abspath('/users/claytonblythe/Desktop/Mega/Data_Science/projects/wifi_speed_tracking')
filename_basic='/code/clean_wireless.log'
filename = open(base_path+filename_basic,'r')
lines = filename.readlines()
print(len(lines))

#parsing the correct strings for time, download, upload speeds
download_speeds = [i[10:15] for i in lines if 'Download' in i]
download_speeds_floats= [float(i) for i in download_speeds]
upload_speeds = [i[8:12] for i in lines if 'Upload' in i]
date_times = [i[:-1] for i in lines if 'CST' in i or 'CDT' in i or 'MST' in i]

date_times_parsed=[i[11:16] for i in date_times]
#print(date_times_parsed)
#print(date_times)
date_times = [i.replace('MST', 'CST') for i in date_times]


converted_times = [datetime.strptime(i, "%a %b %d %H:%M:%S %Z %Y") for i in date_times]  
dates = matplotlib.dates.date2num(converted_times)


#moving average function from numpy
def movingaverage(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')
y_av = movingaverage(download_speeds_floats, 15)


#create plots for the visualization
fig, ax = plt.subplots(figsize=(17,10))
#scatterpoints
ax.plot_date(dates,download_speeds)
#average trend
ax.plot_date(dates[6:-6],y_av[6:-6], ls='solid', color='r', label="running average")

#This finds the correct locations for certain hours to place the ticks, and also
#does the formatting for the labels
ax.xaxis.set_major_locator(HourLocator(range(0,1,1)))
ax.xaxis.set_major_formatter(DateFormatter('%b %dth\n'))
plt.ylabel("(Mb/s)", fontsize=23)
plt.title("Wireless Speed Over Time", fontsize=28)
plt.xticks(rotation=70)
plt.legend()
plt.grid(which="major",axis="x")
date_and_time_string = time.strftime("%b_%d_%H:%M_")
fig.savefig(base_path+'/figures/wireless_speeds_'+date_and_time_string+'.pdf')
fig.savefig(base_path+'/figures/wireless_speeds_'+date_and_time_string+'.png')
