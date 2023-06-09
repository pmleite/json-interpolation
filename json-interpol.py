from jsonmerge import merge
import glob
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
    
    for realm in realms_dict:
        Files = glob.glob(input_folder + realm)
        for i, singlefile in realms_dict[realm]:
            if i==0:
                with open(input_folder + singlefile) as jf:
                    data = json.load(jf)         
            else:
                with open(input_folder + singlefile) as jf1:
                    data['data'].extend(json.load(jf1)['data'])
                    print(data)

            
    # for realm in realms_dict:
    #     interpolated_json = {}
    #     for json_file in realms_dict[realm]:
    #         with open(input_folder + json_file) as json_file:
    #             data = json.load(json_file)
    #             interpolated_json = merge(interpolated_json, data, schema={"mergeStrategy": "objectMerge"})
    #     with open(outFolder + base_output_file_name + realm + '.json', 'w') as outfile:
    #         json.dump(interpolated_json, outfile, indent=2)
             
      
def main():
    create_json_file_dictionary()


if __name__ == "__main__":
    main()
    
    
    
#Loop through the dictionary of json files, interpolate them, creating non existent values and save them in the output folder
# for realm in realms_dict:
#     interpolated_json = {}
#     for json_file in realms_dict[realm]:
#         with open(input_folder + json_file) as json_file:
#             data = json.load(json_file)
#             interpolated_json = {**interpolated_json, **data}
#     with open(outFolder + base_output_file_name + realm + '.json', 'w') as outfile:
#         json.dump(interpolated_json, outfile, indent=2)

    