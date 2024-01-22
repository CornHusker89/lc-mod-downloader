
import gdown
import os
import traceback

from links import instructions

lc_path = ""
if os.path.exists("C:\Program Files (x86)\Steam\steamapps\common\Lethal Company"):
    lc_path = "C:\Program Files (x86)\Steam\steamapps\common\Lethal Company"
else:
    raise Exception("couldn't find Lethal Company directory")

try:
    for line in instructions:
        path = line[0].replace("*", lc_path)
        instruction = line[1]

        print(instruction)
        if instruction == "delete_existing_files":
            print(f"removing all files/directories in {path}")
            for file in os.listdir(path):   
                os.remove(path + "/" + file)
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