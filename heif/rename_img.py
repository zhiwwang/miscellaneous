from ctypes.wintypes import HACCEL
import os
import time
import shutil

path0 = 'C:/Users/Xuanbo/Desktop/1/'
path1 = 'C:/Users/Xuanbo/Desktop/2/'

files_list = os.listdir(path0)
total_file_number = len(files_list)

def get_file_time(filename):
    filename = os.path.abspath(filename)
    create_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime(os.path.getctime(filename)))
    update_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime(os.path.getmtime(filename)))
    access_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime(os.path.getatime(filename)))
    return create_time, update_time, access_time

def get_file_time_from_name(filename):

    # y=filename[2:6]
    # m=filename[6:8]
    # d=filename[8:10]
    # H=filename[10:12]
    # M=filename[12:14]
    # S=filename[14:16]

    # time_file=y+'-'+m+'-'+d+' '+H+':'+M+':'+S
    time_file = time.strftime("%Y-%m-%d %H:%M:%S",
                            time.localtime(1535083200))
    update_time=time_file
    access_time=time_file
    # print(time_file)

    # access_time = time.strftime("%Y-%m-%d %H:%M:%S",
    #                             time.localtime(os.path.getatime(filename)))
    return update_time, access_time

def set_file_time(filename, updatetime, access_time):
    filename = os.path.abspath(filename)
    new_update_time = time.mktime(
        time.strptime(updatetime, '%Y-%m-%d %H:%M:%S'))
    new_access_time = time.mktime(
        time.strptime(access_time, '%Y-%m-%d %H:%M:%S'))
    os.utime(filename, (new_access_time, new_update_time))


for fn in files_list:

    file_jpg = os.path.join(path0, fn)

    create_time, update_time, access_time = get_file_time(file_jpg)
    set_file_time(file_jpg, update_time, access_time)

    # update_time, access_time = get_file_time_from_name(fn,i)
    # set_file_time(file_jpg, update_time, access_time)
    fn_extname=fn.split(".")[-1]
    

    file_time=str(update_time)
    time_stamp=file_time[0:4]+file_time[5:7]+file_time[8:10]+'_'+file_time[11:13]+file_time[14:16]+file_time[17:19]

    new_name='IMG_'+time_stamp+'.'+fn_extname
    file_heic=os.path.join(path1, new_name)
    shutil.copyfile(file_jpg, file_heic)