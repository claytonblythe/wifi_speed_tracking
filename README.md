# wifi_speed_tracking

This is a project called wifi_speed_tracking created by Clayton Blythe on 2017/04/10 
Email: blythec1@central.edu

# Tracking wifi speeds

Background: I was finding myself disappointed and frustrated with the speed of the wifi at my university. So I used a terminal client called speed-test cli 
that allows you to test your wifi speed from the command line. I then piped this result to a wireless speed log file in text form. Finally, I automated
this process with a crontab command, and created a python file to clean the wireless speed log file and plot it in matplotlib. Below is an example of the
result. 

![Alt Test](https://github.com/claytonblythe/wifi_speed_tracking/blob/master/figures/wireless_speeds_Apr_10_09:01_.png)


Here it looks like that the wifi speed that I've been connected has been quite variable over the past couple months that I've been tracking it. 
I plan on allowing this scheduled wifi speed tracker run for months in the background of my laptop, so that I can track how my wifi speed changes
over time depending on the various locations/cities that I am located in. 

Another interesting possibility is to do this tracking for the rest of my life, to get a real first-hand measure of how quickly wifi speeds have increased
throughout my lifetime. I think that this type of data would be really interesting, as it would provide real data for my specific experiences.

