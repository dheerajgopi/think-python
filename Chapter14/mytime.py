from time1 import *

def is_after(t1,t2):
    t1_in_sec = (t1.hour*3600) + (t1.minute*60) + (t1.second)
    t2_in_sec = (t2.hour*3600) + (t2.minute*60) + (t2.second)
    return t1_in_sec > t2_in_sec

def increment(time, seconds):
    time_sec = (time.hour*3600)+(time.minute*60)+time.second
    new_time_sec = time_sec + seconds
    upd_time = Time()
    upd_time.hour = new_time_sec/3600
    upd_time.minute = (new_time_sec%3600)/60
    upd_time.second = ((new_time_sec%3600)%60)
    return upd_time
