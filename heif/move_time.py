import os
import time
import shutil

def get_file_time(filename):
    filename = os.path.abspath(filename)
    create_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime(os.path.getctime(filename)))
    update_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime(os.path.getmtime(filename)))
    access_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime(os.path.getatime(filename)))
    return create_time, update_time, access_time


def set_file_time(filename, updatetime, access_time):
    filename = os.path.abspath(filename)
    new_update_time = time.mktime(
        time.strptime(updatetime, '%Y-%m-%d %H:%M:%S'))
    new_access_time = time.mktime(
        time.strptime(access_time, '%Y-%m-%d %H:%M:%S'))
    os.utime(filename, (new_access_time, new_update_time))


path0 = 'C:/Users/Xuanbo/Desktop/Screenshots/'
path1 = 'H:/Screenshots2/'
path2 = 'C:/Users/Xuanbo/Desktop/Screenshots0/'

files_list = os.listdir(path0)

i = 0
total_file_number = len(files_list)
for fn in files_list:
    file_jpg = os.path.join(path0, fn)
    fn_list = fn.split(".")[:-1]

    name = str()
    for item in fn_list:
        name = str(name) + item + '.'

    file_heic = os.path.join(path1, name + 'heic')
    # os.system('magick ' + file_jpg + ' ' + file_heic)

    # file_90jpg = os.path.join(path1, name + 'jpg')
    # os.system('magick ' + file_jpg + ' -quality 90 ' + file_90jpg)

    create_time, update_time, access_time = get_file_time(file_jpg)
    set_file_time(file_heic, update_time, access_time)

    size_jpg=os.path.getsize(file_jpg)
    size_heic=os.path.getsize(file_heic)

    if size_jpg>size_heic:
        source=file_heic
    else:
        source=file_jpg
    
    target = os.path.join(path2, os.path.basename(source))
    shutil.copy(source, target)
    
    set_file_time(target, update_time, access_time)

    i += 1
    if i % 100 == 1:
        print(i, '/', total_file_number)
    # print(file_heic)

print('Total processed :', i)
