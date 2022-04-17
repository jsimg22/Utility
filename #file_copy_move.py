# file_copy_move
# 여러 폴더에 있는 mp3 파일을 한 폴더로 복사해오기

import os
import fnmatch
import shutil

os.chdir("D:\음악")
print(os.getcwd())

target_folder= "D:\음악\Target"
dest_folder = "D:\음악\Idol_cin_mil"
my_folder=os.walk(target_folder)
pattern = "*.mp3"
pattern2 = "*.flac"
result= []
except_pattern = "*Drama*"

for root,dirs,files in my_folder :
    for name in files :
        if fnmatch.fnmatch(name,except_pattern): # 파일 이름 매칭 
            pass
        elif fnmatch.fnmatch(name,pattern):
            try: # try except  중복 피하기
                result.append(os.path.join(root,name))
                print(os.path.join(root,name))
                os.chdir(root)
                shutil.copy2(name,dest_folder)
                os.chdir("D:\음악")
            except PermissionError as e:
                print(e)     
        elif fnmatch.fnmatch(name,pattern2):
            try:
                result.append(os.path.join(root,name))
                print(os.path.join(root,name))
                os.chdir(root)
                shutil.copy2(name,dest_folder)
                os.chdir("D:\음악")
            except PermissionError as e:
                print(e)
