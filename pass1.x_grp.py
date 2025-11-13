# --- DATA STRUCTURES ---
# OPTAB: Maps instruction mnemonics to opcodes (Dictionary)
OPTAB = { "LOAD": "01", "STORE": "02", "ADD": "03", "SUB": "04", "JMP": "05" }
# SYMTAB: Maps labels to addresses (Dictionary)
SYMTAB = {} 
# Intermediate Code: Stores (Address, Label, Opcode, Operand) (List of Tuples)
intermediate_code = []

def pass1(input_lines):
    locctr = 0
    for line in input_lines:
        parts = line.split()
        # Parse Line logic
        label = parts[0] if len(parts) == 3 else None
        opcode = parts[1] if len(parts) == 3 else parts[0]
        operand = parts[2] if len(parts) == 3 else parts[1] if len(parts) == 2 else None

        # Handle START
        if opcode == "START":
            locctr = int(operand)
            intermediate_code.append((locctr, label, opcode, operand))
            continue

        # Handle Label (Add to SYMTAB)
        if label:
            if label in SYMTAB:
                print(f"Error: Duplicate symbol {label}")
            else:
                SYMTAB[label] = locctr

        # Handle Opcodes & Directives (Update LOCCTR)
        current_loc = locctr
        if opcode in OPTAB:
            locctr += 3
        elif opcode == "WORD":
            locctr += 3
        elif opcode == "RESW":
            locctr += 3 * int(operand)
        elif opcode == "RESB":
            locctr += int(operand)
        elif opcode == "END":
            pass # END does not increment location counter
        
        intermediate_code.append((current_loc, label, opcode, operand))

def main():
    # Input Assembly Code
    input_lines = [
        "COPY START 1000",
        "FIRST LOAD ALPHA",
        " ADD BETA",
        "ALPHA WORD 5",
        "BETA WORD 10",
        " END FIRST"
    ]
    pass1(input_lines)
    
    print("--- PASS I OUTPUT ---")
    print("SYMBOL TABLE:", SYMTAB)
    print("INTERMEDIATE CODE:")
    for line in intermediate_code:
        print(line)

if __name__ == "__main__":
    main()