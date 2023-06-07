import os
import shutil 
##print(dir(os))
#path=os.getcwd()
#print("The Path Is...",path)
#os.mkdir("102")
#files=os.listdir("C:/Users/sojia/OneDrive/Desktop")
#print(files)
#exist=os.path.exists("C:/Users/sojia/OneDrive/Desktop/")
#print(exist)
destination="C:/Users/sojia/downloads"
source="C:/Users/sojia/OneDrive/Desktop"
listOfFiles=os.listdir(source)
for i in listOfFiles:
    name,ext=os.path.splitext(i)
    if ext=="":
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1=source + '/' + i
        path2=destination + '/' + "imageFiles"
        path3=destination + '/' + "imageFiles" + "/" + i

        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)
