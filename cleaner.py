import os
import shutil

try:
    path="path where the folder is"
    for (path,dirs,files) in os.walk(path):
        for file in files:
            extension=file.split('.')[1]
            if os.path.exists(r"D:\\path"+extension):
                if file.endswith(extension):
                    shutil.move(file,"D:\\path"+extension)
            else:
                
                os.system('mkdir'+extension)
                shutil.move(file,"d:\\path")
except:
     print("an error occured")

#def createIfNotExist(folder):
#    if not os.path.exists(folder):
#        os.makedirs(folder)
#
#def move(folderName, files):
#    for file in files:
#        os.replace(file, f'{folderName}/{file}')
#
#files=os.listdir()
#files.remove("cleaner.py")
#
#createIfNotExist('Images')
#createIfNotExist('Docs')
#createIfNotExist('Media')
#createIfNotExist('Others')

#imgExts = [".png", ".jpg", ".jpeg"]
#images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

#docExts = [".txt", ".docx", "doc", ".pdf"]
#docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

#mediaExts = [".mp4", ".mp3", ".flv"]
#medias = [file for file in files if os.path.splitext(file)[1].lower() in  mediaExts]

#others=[]
#for file in files:
#    ext=os.path.splitext(file)[1].lower()
#    if(ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
#        others.append(file)

#print(others)
#move("Images",images)
#move("Docs",docs)
#move("Media",medias)
#move("Others",others)
