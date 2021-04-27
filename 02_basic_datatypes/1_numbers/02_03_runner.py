'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

miles = 10
kilometers = miles * 1.6
hour = 1
minute = hour/60
second = minute/60
average_speed = kilometers/(hour/2)+(minute/2)
print(average_speed)
