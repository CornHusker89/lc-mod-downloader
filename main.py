
import gdown
import os
import shutil
import traceback

from links import instructions

lc_path = ""
if os.path.exists("C:\Program Files (x86)\Steam\steamapps\common\Lethal Company"):
    lc_path = "C:\Program Files (x86)\Steam\steamapps\common\Lethal Company"
elif os.path.exists("D:\Program Files (x86)\Steam\steamapps\common\Lethal Company"):
    lc_path = "D:\Program Files (x86)\Steam\steamapps\common\Lethal Company"
elif os.path.exists("E:\Program Files (x86)\Steam\steamapps\common\Lethal Company"):
    lc_path = "E:\Program Files (x86)\Steam\steamapps\common\Lethal Company"
elif os.path.exists("F:\Program Files (x86)\Steam\steamapps\common\Lethal Company"):
    lc_path = "F:\Program Files (x86)\Steam\steamapps\common\Lethal Company"
elif os.path.exists("G:\Program Files (x86)\Steam\steamapps\common\Lethal Company"):
    lc_path = "G:\Program Files (x86)\Steam\steamapps\common\Lethal Company" # if someone has past G: then they need to get their life together
else:
    raise Exception("couldn't find Lethal Company directory")

try:
    for line in instructions:

        if not "*" in line[0]:
            raise Exception("DEBUG: path must contain a * (forward this error to rat and/or corn)")

        path = line[0].replace("*", lc_path)
        instruction = line[1]

        # make sure the path exists. if it dosent, make it exist
        if not os.path.exists(path):
            path = path.replace("\\", "/").replace("//", "/")
            directory_path_list = path.split("/")

            print(directory_path_list)

            if not "BepInEx" in directory_path_list:
                print("----------------------------------------")
                response = input(f"WARNING: BepInEx did not exist before this was ran. A BepInEx installation is required. Are you sure you want to continue? (say \"n\" if you don't know) (y/n) ")
                if response == "y" or response == "Y" or response == "yes" or response == "Yes":
                    pass
                else:
                    raise Exception("canceled by user")

            for i in range(len(directory_path_list)):
                if i == 0:
                    continue
                directory_path = ""
                for j in range(i + 1):
                    directory_path += directory_path_list[j] + "/"
                print(directory_path)
                if not os.path.exists(directory_path):
                    os.mkdir(directory_path)

        if instruction == "delete_existing_files":
            print(f"removing all files/directories in {path}")
            for file in os.listdir(path):
                if os.path.isfile(path + "/" + file):
                    os.remove(path + "/" + file)
                else:
                    shutil.rmtree(path + "/" + file)

        else:
            # download folders
            try:
                gdown.download_folder(url=instruction, output=path)
            except:
                raise Exception(f"An error occured while downloading a folder with link {instruction} (make sure this is a valid and publicly accessable link). Error: {traceback.format_exc()}")
                
except Exception as e:
    print("An error occured:")
    print(traceback.format_exc())
    input("Press enter to exit")