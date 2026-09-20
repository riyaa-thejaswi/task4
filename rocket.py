#This script runs a short countdown from 10 down to 0 (not including) before printing the message "Blast Off"
import time
print("Written by: Riyaa")
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Blast Off 💥🚀")
