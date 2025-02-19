# Preparation
1. Make sure you have Python 3.10+ installed (maybe older versions will work, but definitely Python 3)
2. Run `sudo apt install python3.10-venv`
3. Go to the folder with the script (where this README is located)
4. Run `python3 -m venv venv`
5. Run `source venv/bin/activate`
6. Run `pip install playwright`
7. Run `playwright install`
8. Run `playwright install-deps`

You can now use the script

# Usage
1. Go to the folder with the script (where this README is located)
2. (Only need to run once for each session) Run `source venv/bin/activate` (you should notice `(venv)` next to your command line after this)
3. Run `python3 playwright_scrapper.py {start_id} {end_id} {monster_name} {output_file_name}`, for example if we want to grab IDs from 14799 to 14835 for the monster `dark-panther` and write the output to `dark-panther.sql` file then run: `python3 playwright_scrapper.py 14799 14835 dark-panther dark-panther.py`

# Troubleshooting

## The scrapper timeouts too fast

Try increasing the timeout at line 10 in `playwright_scrapper.py` (it is in milliseconds, so 1700 = 1.7s, etc.)