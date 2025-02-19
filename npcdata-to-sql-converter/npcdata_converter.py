import sys
import os
import re

ID_REGEX = r"npc_begin\s+.+\s+(\d+)"
REGEX = r"npc_begin\s+.+\s+(\d+)\s+.*level=([\d.]+).+org_hp=([\d.]+).+org_mp=([\d.]+).+base_physical_attack=([\d.]+).+base_attack_speed=([\d.]+).+base_magic_attack=([\d.]+).+base_defend=([\d.]+).+base_magic_defend=([\d.]+)"


def main(input_file, start_id, end_id, output_file):
    # Ensure the output file is empty before starting
    if os.path.exists(output_file):
        os.remove(output_file)
    
    # Ensure the input file exists
    if not os.path.exists(input_file):
        raise Exception(f"{input_file} does not exist")
    
    # Read data and store what we are interested in
    print(f"Processing from {start_id} to {end_id} (inclusive)")
    output = {}
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            # Extract the ID
            id_match = re.search(ID_REGEX, line)
            id = int(id_match.groups()[0])

            # Ignore IDs out of scope
            if id < start_id or id > end_id:
                continue

            # Process
            match = re.search(REGEX, line)
            id, level, hp, mp, patk, atkspd, matk, pdef, mdef = match.groups()
            #print(f"id: {id}, level: {level}, hp: {hp}, mp: {mp}, patk: {patk}, atkspd: {atkspd}, matk: {matk}, pdef: {pdef}, mdef: {mdef}")
            output[id] = {
                "level": float(level),
                "hp": float(hp),
                "mp": float(mp),
                "patk": float(patk),
                "atkspd": float(atkspd),
                "matk": float(matk),
                "pdef": float(pdef),
                "mdef": float(mdef)
            }
    
    # Write to an SQL output file
    with open(output_file, "a") as file:
        for npc_id, stats in output.items():
            sql = (
                f"UPDATE npc SET hp = {stats['hp']}, mp = {stats['mp']}, "
                f"patk = {stats['patk']}, atkspd = {stats['atkspd']}, matk = {stats['matk']}, "
                f"pdef = {stats['pdef']}, mdef = {stats['mdef']} "
                f"WHERE id = {npc_id};\n"
            )
            file.write(sql)
    
    print("Done!")



    



if __name__ == "__main__":
    # Ensure proper arguments are passed
    if len(sys.argv) != 5:
        print("Usage: python npcdata_converter.py <input_file> <start_id> <end_id> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    start_id = int(sys.argv[2])
    end_id = int(sys.argv[3])
    output_file = sys.argv[4]
    
    main(input_file, start_id, end_id, output_file)