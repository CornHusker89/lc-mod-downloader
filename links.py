
# comments are made with a hashtag
# dont forget to put a comma after each line in the body (except the last line), as if this were JSON

# each line of code is a step in the program
# the first value (the one before the ",") is the path to the directory
# replace any "*" in the path with the path to the Lethal Company directory (copy path to plugins folder, EX: C:\Program Files (x86)\Steam\steamapps\common\Lethal Company\)
# the second value (the one after the ",") is either a link to a google drive folder or an instruction
# if the value is "delete_existing_files", the program will delete all files in the directory in that step. This is recommended before downloading something to that folder (aka directory)

instructions = [
    ["*", "delete_existing_files"],
    ["*", "https://drive.google.com/drive/folders/1rQFSuPN6yJ93KDOpy45J31OWcyDXZNal"]
]
