import os, shutil

#specify the path to the files location
path = r"C:/Users/Alexandra-PK/Desktop/Work/Portfolio/Python/File_sorter/"
file_names = os.listdir(path)
print(file_names)

#create new folders
folder_names = ["xlsx files", "images", "Power BI files"]
for i in range(0,3):
   if not os.path.exists(path + folder_names[i]):
      print((path + folder_names[i]))
      os.makedirs(path + folder_names[i])
      
for file in file_names:
   if ".xlsx" in file and not os.path.exists(path + "xlsx files/" + file):
      shutil.move(path + file, path + "xlsx files/" + file)
   if ".jfif" in file and not os.path.exists(path + "images/" + file):
      shutil.move(path + file, path + "images/" + file)
   if ".pbix" in file and not os.path.exists(path + "Power BI files/" + file):
      shutil.move(path + file, path + "Power BI files/" + file)
      