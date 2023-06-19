# json-interpolation
JSON files interpolation

This project is a simple json files merge.
In a folder named 'jsons' add jsons files, the name of thoses jsons files should contain:

anyText-groupName-anyText.json

The final result of the program is a single json with the name merge-groupName.json

You may have as many json you want to, and as many groupNames you intend to, knowing that will be generated one (1) json file for all the files with the same name.

This software make a blind merge, do not check duplication.

## usage ##

python3 json-interpol.py -o OUTFILE (demanded) -b OUTPUT_BASE_NAME (default merge)
