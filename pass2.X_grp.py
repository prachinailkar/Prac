# --- DATA STRUCTURES ---
OPTAB = { "LOAD": "01", "STORE": "02", "ADD": "03", "SUB": "04" }

# SIMULATING INPUT FROM PASS-I (Normally read from file)
SYMTAB = {'FIRST': 1000, 'ALPHA': 1009, 'BETA': 1012}
intermediate_code = [
    (1000, 'COPY', 'START', '1000'),
    (1000, 'FIRST', 'LOAD', 'ALPHA'),
    (1003, None, 'ADD', 'BETA'),
    (1006, None, 'STORE', 'ALPHA'), # Using ALPHA again for example
    (1009, 'ALPHA', 'WORD', '5'),
    (1012, 'BETA', 'WORD', '10'),
    (1015, None, 'END', 'FIRST')
]

def pass2():
    final_code = []
    
    for locctr, label, opcode, operand in intermediate_code:
        # 1. Handle Imperative Statements (Instructions)
        if opcode in OPTAB:
            machine_opcode = OPTAB[opcode]
            # Look up operand address in SYMTAB
            if operand in SYMTAB:
                address = f"{SYMTAB[operand]:04X}"
            else:
                address = "0000"
            final_code.append(f"{locctr:04X}  {machine_opcode}  {address}")
            
        # 2. Handle Assembler Directives
        elif opcode == "WORD":
            # Convert constant to Hex
            final_code.append(f"{locctr:04X}  00  {int(operand):04X}")
            
        elif opcode == "RESW" or opcode == "RESB":
            final_code.append(f"{locctr:04X}  --  ----")
            
        elif opcode == "END":
            final_code.append(f"      END")
            
    return final_code

def main():
    machine_code = pass2()
    print("--- PASS II OUTPUT (Machine Code) ---")
    for line in machine_code:
        print(line)

if __name__ == "__main__":
    main()