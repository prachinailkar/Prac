# --- DATA STRUCTURES ---
# SIMULATING INPUT FROM PASS-I (Normally read from file)
MNT = {'INCR': 0} # INCR starts at index 0 of MDT
MDT = [
    "LOAD A",
    "ADD B",
    "MEND"
]
# Intermediate code containing the Call "INCR"
input_source = [
    "START 100",
    "INCR",       # This is a macro call
    "STORE C",
    "END"
]

def pass2_macro():
    expanded_source = []
    
    for line in input_source:
        parts = line.split()
        token = parts[0]
        
        # Check if token is in MNT (It's a Macro Call)
        if token in MNT:
            mdt_index = MNT[token]
            
            # Expand the macro: Copy lines from MDT until MEND
            current_mdt_line = MDT[mdt_index]
            i = mdt_index
            while True:
                line_content = MDT[i]
                if line_content == "MEND":
                    break
                expanded_source.append(f"+ {line_content}") # + indicates expansion
                i += 1
        
        # Not a macro call, just copy the line
        else:
            expanded_source.append(line)
            
    return expanded_source

def main():
    output = pass2_macro()
    print("--- PASS II MACRO OUTPUT (Expanded Code) ---")
    for line in output:
        print(line)

if __name__ == "__main__":
    main()