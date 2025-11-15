# --- DATA STRUCTURES ---
# MNT (Macro Name Table): Stores Macro Name and index in MDT (Dictionary)
MNT = {}
# MDT (Macro Definition Table): Stores the body of macros (List)
MDT = []
# Intermediate Code: Source code with Macro Definitions removed (List)
intermediate_code = []

def pass1_macro(input_lines):
    """
    Performs Pass 1 of a macro processor.
    Populates MNT, MDT, and intermediate_code.
    """
    mdt_index = 0
    macro_on = False
    
    for line in input_lines:
        parts = line.split()
        
        # Guard against empty lines
        if not parts:
            continue

        # Check for MACRO start
        # Fixed: Check len(parts) > 1 to prevent index error
        if len(parts) > 1 and parts[1].upper() == "MACRO":
            macro_name = parts[0]
            MNT[macro_name] = mdt_index
            macro_on = True
            # Don't add the 'MACRO' line to MDT or intermediate code
        
        # Check for MEND
        elif parts[0].upper() == "MEND":
            MDT.append(line) # Add MEND to MDT
            mdt_index += 1
            macro_on = False
            # Don't add MEND to intermediate code

        # If inside a Macro Definition
        elif macro_on:
            MDT.append(line) # Add macro body line to MDT
            mdt_index += 1
            # Don't add to intermediate code
            
        # If not a macro line, it's normal code
        else:
            intermediate_code.append(line)

def main():
    # --- Dynamic Input Section ---
    input_lines = []
    print("Enter your assembly code line by line.")
    print("Type 'DONE' (all caps) on a new line when you are finished:")
    
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        input_lines.append(line)
    # --- End of Dynamic Input ---
    
    
    # Process the dynamically entered code
    pass1_macro(input_lines)
    
    print("\n--- PASS I MACRO OUTPUT ---")
    
    print("\n## MNT (Macro Name Table)")
    print(MNT)
    
    print("\n## MDT (Macro Definition Table)")
    if not MDT:
        print("(No macros defined)")
    for i, line in enumerate(MDT):
        print(f"Index {i}: {line.strip()}") # .strip() for 
    print("\n## Intermediate Code (Definitions Removed)")
    if not intermediate_code:
        print("(No intermediate code generated)")
    for line in intermediate_code:
        print(line)

if __name__ == "__main__":
    main()



#
#Enter your assembly code line by line.
Type 'DONE' (all caps) on a new line when you are finished:
INCR MACRO  # Macro Definition Start
LOAD A
ADD B
MEND       
START 100
INCR     
STORE C
END
DONE

--- PASS I MACRO OUTPUT ---

## MNT (Macro Name Table)
{'INCR': 0}

## MDT (Macro Definition Table)
Index 0: LOAD A
Index 1: ADD B
Index 2: MEND

## Intermediate Code (Definitions Removed)
START 100
INCR     
STORE C
END

=== Code Execution Successful ===
#
#
#
#
#


How to Explain This Code in a Viva
Examiner: "Can you please explain the program you have written?"

You: "Yes, sir/ma'am. This program implements the Pass 1 of a Two-Pass Macro Processor."

Examiner: "And what is the main purpose of Pass 1?"

You: "The main purpose of Pass 1 is to read the entire source code and separate the macro definitions from the main program logic. It doesn't expand any macros. It just finds them, catalogues them, and prepares the code for Pass 2.

To do this, it builds three key data structures:"

1. The MNT (Macro Name Table)
"First, as you can see in the output {'INCR': 0}, it builds the MNT, or Macro Name Table.

This is a Dictionary.

Its job is to act as a 'table of contents' or an index for all the macros.

When the code finds a line like INCR MACRO, it stores the macro's name (INCR) as the key, and its starting line number in the MDT (which is 0) as the value."

2. The MDT (Macro Definition Table)
"Second, it builds the MDT, or Macro Definition Table.

This is a List.

This is the 'library' that stores the actual body of the macro.

As you can see from the output, it stores every line between MACRO and MEND. So, Index 0 is LOAD A, Index 1 is ADD B, and so on. The MNT just points to the start of this table."

3. The Intermediate Code
"Finally, it generates the Intermediate Code.

This is the original source code, but with the macro definitions completely removed.

If you look at the output, you'll see it contains START 100, INCR, STORE C, and END.

The definition for INCR is gone, but the call to INCR is still there.

This Intermediate Code is the final output of Pass 1 and is the direct input for Pass 2."

How the Code Logic Works
Examiner: "How does your code know when it's inside a macro?"

You: "It uses a simple boolean flag called macro_on.

Initially, macro_on is False. Any line it reads is considered Intermediate Code and is saved.

When it finds a line with the word MACRO (e.g., INCR MACRO), it flips the flag to macro_on = True.

As long as macro_on is True, it knows it's inside a macro definition, and it appends every line it reads only to the MDT.

When it finally hits a MEND line, it flips the flag back to macro_on = False and goes back to writing normal Intermediate Code."

Summary:

"So, in summary, Pass 1 just finds, catalogues, and removes all the macro definitions. It creates the MNT and MDT as a 'rulebook' and cleans up the code into an Intermediate File. This file is now perfectly prepared for Pass 2, which will do the actual work of expanding the INCR call."