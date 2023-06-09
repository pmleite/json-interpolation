import json
import os   

input_folder:str            = './data/'
output_folder:str           = './out/'
base_output_file_name:str   = 'realm_'

json_files:list             = []
realms_dict:dict            = {}


#Creates a dictionary of JSON files agrupaded by the word after the first dash of file name
def create_json_file_dictionary(folder:str = input_folder):
    
    #Update the list of json files
    for f in os.listdir(folder):
        if f.endswith(".json"):
            json_files.append(f)
    
    #Update the dictionary of json files
    for ff in json_files:
        if ff.endswith(".json"):
            json_file_name = ff.split('-')[1]
            if json_file_name not in realms_dict:
                realms_dict[json_file_name] = []
            realms_dict[json_file_name].append(ff)
            
    #List of json files by key of realms_dict
    for key in realms_dict:
        print(key)
        print(realms_dict[key])
        print()
        
    #Loop through the dictionary of json files, interpolate them and save them in the output folder
    for realm in realms_dict:
        print(realm)
        print(realms_dict[realm])
        interpolated_json = {}
        for json_file in realms_dict[realm]:
            #print(json_file)
            with open(input_folder + json_file) as json_file:
                data = json.load(json_file)
                interpolated_json = {**interpolated_json, **data}
        print(interpolated_json)
        with open(output_folder + base_output_file_name + realm + '.json', 'w') as outfile:
            json.dump(interpolated_json, outfile)
            
def main():
    create_json_file_dictionary()

  

if __name__ == "__main__":
    main()

    