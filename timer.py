import time

print("-------- Timer ---------")
t = int(input("Choose the duration in seconds: "))
print("========================")

while t>0:
    print("T minus", t, "s")
    t = (t - 1)
    time.sleep(1)
print("Time is up!")
