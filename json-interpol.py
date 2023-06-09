from datetime import datetime
import json
import os   
import argparse

parser = argparse.ArgumentParser("JSON Mergerator.\n\n")
parser.description = "Merge JSON files in a folder, agrupaded by the word after the first dash of file name"
parser.description += "The files should have a common name between '-' as second word of file name:"
parser.description += "Example: 'users-abc-file.json', 'groups-abc-file.json', will be merged in 'realm_abc.json', if not used the flag -b for onother base name'\n\n"
parser.add_argument("-j","--jsonsDir",  help="The folder where the JSON files are located, default './jsons/'. This folder MUST exist", type=str, default="./jsons/")
parser.add_argument("-o","--outDir", help="The folder where the interpolated JSON files will be saved, default './jsons/out/'. This folder MUST exist", type=str)
parser.add_argument("-b","--baseName", help="The base name of the interpolated JSON files, default 'merged_'", type=str, default="merged_")
parser.add_argument("-v","--verbose", help="Verbose mode", action="store_true")
args = parser.parse_args()

input_folder:str            = args.jsonsDir
output_folder:str           = args.outDir
base_output_file_name:str   = args.baseName
verbose_mode:bool           = args.verbose

json_files:list             = []
realms_dict:dict            = {}


#Creates a dictionary of JSON files agrupaded by the word after the first dash of file name
def create_json_file_dictionary(inFolder:str = input_folder, outFolder:str = output_folder, verbose:bool = verbose_mode):
    """
    Update an JSON file dictionary with the files in the folder,
    agrupaded by the word after the first dash of file name

    Args:
        folder (str): Folder where the JSON files are located

    """
    
    #check if the folder exists, otherwise create it
    if not os.path.exists(inFolder):
        os.makedirs(inFolder)
        print("Directory " , inFolder ,  " not found! It was created.\n"+
              "Please put the JSON files, to merge, into this folder and run the script again!\n")
        print("The files must have the .json extension and shoud have the same agregation name between '-' as second word of file name:\n")
        print("Example:\n\n"+
              "'users-abc-file.json', 'groups-abc-file.json', will be merged in 'realm_abc.json', if not used the flag -b for onother base name'\n\n")    
   
    if (outFolder):
        if not os.path.exists(outFolder):
            os.makedirs(outFolder)
            print("Directory " , outFolder ,  " not found! It was created\n"+
                "You will find the interpolated JSON file in this folder\n")
    else:
        print("Output folder not defined! This is a demended parameter!")
        print("Please use the flag -o OUTDIR to define the output folder!\n")
        print("Example:   -o ./teste/\n")
        exit(1)

    #Update the list of json files
    for f in os.listdir(inFolder):
        if f.endswith(".json"):
            if (verbose):print("Found the file: " + f)
            json_files.append(f)
    if (verbose):print("\n:The list of files is: " + str(json_files) + "\n")
    
    #Update the dictionary of json files
    for ff in json_files:
        if ff.endswith(".json"):
            json_file_name = ff.split('-')[1]
            if json_file_name not in realms_dict:
                if (verbose):print("Creating the key: " + json_file_name)
                realms_dict[json_file_name] = []
            realms_dict[json_file_name].append(ff)
            if (verbose):print("Adding the file: " + ff + " to the key: ") 
            
    #Interpolate the json filespyi
    for key in realms_dict: 
        merged:dict      = {} 
        for json_file in realms_dict[key]:
            data = json.load(open(inFolder + json_file))
            merged.update(data)
        if(verbose):print("The file " + json_file + " was merged into the file " + base_output_file_name + key + ".json")
               
        #Save the interpolated json file     
        with open(outFolder + base_output_file_name + key + '.json', 'w') as outfile:
            json.dump(merged, outfile, indent=2)
            if(verbose):print("The file " + base_output_file_name + key + ".json was created into the folder " + outFolder )
    
def main():
    create_json_file_dictionary()

if __name__ == "__main__":
    main()