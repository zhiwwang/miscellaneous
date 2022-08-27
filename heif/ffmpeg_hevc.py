import os
import imageio

path0 = 'D:/mp4/'

files_list = os.listdir(path0)
total_file_number = len(files_list)
i=0
size_jpg=0
for fn in files_list:
    file_jpg = os.path.join(path0, fn)

    reader = imageio.get_reader(file_jpg)
    meta_data = reader.get_meta_data()

    if meta_data['codec']=='h264':
        size_jpg=size_jpg+os.path.getsize(file_jpg)
        i+=1
        print(size_jpg)
        print(i)

    # print(meta_data['codec'])
    # print(fn)
