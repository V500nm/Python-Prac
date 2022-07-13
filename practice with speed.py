# if you run 10 km in 43 min 30 sec? avg time per mile? avg speed in mph
dk = 10.0
dm = (dk/1.61)
realdm = (dm)
#avg time per mile
TKM = (43.5/dk)
TM = (43.5/dm)
print ("time for 1KM:", TKM )
print ("time for 1M:", TM )
print("Total KM to M:", dm)
#avg mile per hour
MPH = (60.0/TM)
print ("average speed in M:", MPH)
