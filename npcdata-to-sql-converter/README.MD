# Preparation
1. Make sure you have Python 3.9+ installed (maybe older versions will work, but definitely Python 3)
2. Run `sudo apt install python3.9-venv`
3. Go to the folder with the script (where this README is located)
4. Run `python3 -m venv venv`
5. Run `source venv/bin/activate`

You can now use the script

# Usage
1. Go to the folder with the script (where this README is located)
2. (Only need to run once for each session) Run `source venv/bin/activate` (you should notice `(venv)` next to your command line after this)
3. Run `python3 npcdata_converter.py {input_file_name} {start_id} {end_id} {output_file_name}`, for example if we want to process the `npcdata.txt` file (in the same folder as the script) for IDs 20001 to 22227 and write to `output.sql` (in the same folder) then run: `python3 npcdata_converter.py npcdata.txt 20001 22227 output.sql`
