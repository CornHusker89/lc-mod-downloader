
# comments are made with a hashtag
# dont forget to put a comma after each line in the body (except the last line), as if this were JSON

# each line of code is a step in the program
# the first value (the one before the ":") is the path to the directory
# any "*" in the path will be replaced with the path to the Lethal Company directory
# the second value (the one after the ":") is either a link to a google drive folder or an instruction
# if the value is "delete_existing_files", the program will delete all files in the directory in that step. This is recommended before downloading something to that folder (aka directory)

instructions = [
    ["*/BepInEx", "delete_existing_files"],
    ["*/BepInEx", "https://drive.google.com/drive/folders/1rQFSuPN6yJ93KDOpy45J31OWcyDXZNal"]
]