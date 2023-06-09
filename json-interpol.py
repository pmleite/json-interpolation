import json
import os   

input_folder:str            = './data/'
output_folder:str           = './out/'
base_output_file_name:str   = 'realm_'

json_files:list             = []
realms_dict:dict            = {}

#Get a list of JSON files in a folder
def getListOfJSONFileNames(folder:str = input_folder):
    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            json_files.append(filename)

#Creates a dictionary of JSON files agrupaded by the word after the first dash of file name
def createJSONFileDictionary(folder:str = input_folder):
    json_files = getListOfJSONFileNames(folder)
    for filename in json_files:
        if filename.endswith(".json"):
            json_file_name = filename.split('-')[1]
            if json_file_name not in realms_dict:
                realms_dict[json_file_name] = []
            realms_dict[json_file_name].append(filename)

# Get realm name from JSON file
def get_realm_name(json_data):
    return json_data[0]['realm']


def main():
    print(createJSONFileDictionary())
    print(realms_dict)
  
if __name__ == "__main__":
    main()