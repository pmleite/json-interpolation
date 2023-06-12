from jsonmerge import merge
import json
import os   

input_folder:str            = './data/'
output_folder:str           = './out/'
base_output_file_name:str   = 'realm_'

json_files:list             = []
realms_dict:dict            = {}

#Creates a dictionary of JSON files agrupaded by the word after the first dash of file name
def create_json_file_dictionary(inFolder:str = input_folder, outFolder:str = output_folder):
    """
    Update an JSON file dictionary with the files in the folder,
    agrupaded by the word after the first dash of file name

    Args:
        folder (str): Folder where the JSON files are located

    """
    #Update the list of json files
    for f in os.listdir(inFolder):
        if f.endswith(".json"):
            json_files.append(f)
    
    #Update the dictionary of json files
    for ff in json_files:
        if ff.endswith(".json"):
            json_file_name = ff.split('-')[1]
            if json_file_name not in realms_dict:
                realms_dict[json_file_name] = []
            realms_dict[json_file_name].append(ff)
    
    #Interpolate the json files
    interpolated_json:dict      = {}
   
    for key in realms_dict: 
        for idx,json_file in enumerate(realms_dict[key]):
            jsonData = json.load(open(inFolder + json_file))
            
            #If is the first file, just copy the data
            if (idx == 0):
                interpolated_json = jsonData    
                
            #If is not the first file, merge the data
            else:




               #interpolated_json = merge(interpolated_json, jsonData)
                
        #Save the interpolated json file       
        with open(outFolder + base_output_file_name + key + '.json', 'w') as outfile:
            json.dump(interpolated_json, outfile, indent=2)
        
def main():
    create_json_file_dictionary()

if __name__ == "__main__":
    main()
    
