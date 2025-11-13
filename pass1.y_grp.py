# --- DATA STRUCTURES ---
# MNT (Macro Name Table): Stores Macro Name and index in MDT (Dictionary)
MNT = {}
# MDT (Macro Definition Table): Stores the body of macros (List)
MDT = []
# Intermediate Code: Source code with Macro Definitions removed (List)
intermediate_code = []

def pass1_macro(input_lines):
    mdt_index = 0
    macro_on = False
    
    for line in input_lines:
        parts = line.split()
        
        # Check for MACRO start
        if parts[1] == "MACRO":
            macro_name = parts[0]
            MNT[macro_name] = mdt_index
            macro_on = True
            continue # Don't add 'MACRO' line to MDT, skip to body
            
        # If inside a Macro Definition
        if macro_on:
            MDT.append(line) # Add line to MDT
            mdt_index += 1
            if parts[0] == "MEND":
                macro_on = False
        # If normal code
        else:
            intermediate_code.append(line)

def main():
    # Input Code containing a Macro
    input_lines = [
        "INCR MACRO",    # Macro Definition Start
        "LOAD A",
        "ADD B",
        "MEND",          # Macro Definition End
        "START 100",
        "INCR",          # Macro Call
        "STORE C",
        "END"
    ]
    
    pass1_macro(input_lines)
    
    print("--- PASS I MACRO OUTPUT ---")
    print("MNT (Macro Name Table):", MNT)
    print("MDT (Macro Definition Table):")
    for i, line in enumerate(MDT):
        print(f"Index {i}: {line}")
    print("\nIntermediate Code (Definitions Removed):")
    for line in intermediate_code:
        print(line)

if __name__ == "__main__":
    main()