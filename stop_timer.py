import time


def convert_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    print("Time = {0}:{1}:{2}".format(int(hours), int(minutes), seconds))


input('Hit the ENTER key to START the timer')
start = time.time()

input('Hit the ENTER key to STOP the timer')
stop = time.time()

total_time = stop - start

convert_time(total_time)
