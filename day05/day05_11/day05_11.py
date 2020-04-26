'''
*****************
Date: 2020-04-26
Author: Allen
*****************
'''

import multiprocessing
import os

def copy_work(file_name, source_dir, dest_dir):
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name
    print(source_path, "--->", dest_path)

    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            while True:
                file_data = source_file.read(1024)
                if file_data:
                    dest_file.write(file_data)
                else:
                    break

if __name__ == '__main__':
    source_dir = "./test"
    dest_dir = "./dest"

    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在，未创建")

    file_list = os.listdir(source_dir)
    print(file_list)

    pool = multiprocessing.Pool(3)
    for file_name in file_list:
        pool.apply_async(copy_work, args=(file_name, source_dir, dest_dir))
    pool.close()
    pool.join()