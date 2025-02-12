import sys
import os

def somar(l, line_number):
    total = 0
    enabled = True
    buffer = ""
    folder = "TPC1/outputs"
    
    os.makedirs(folder, exist_ok=True)
    
    filename = f"{folder}/output_{line_number}.txt"

    with open(filename, "w") as f:
        i = 0
        while i < len(l):
            if l[i:i+3].lower() == "off":
                enabled = False
                i += 3
            elif l[i:i+2].lower() == "on":
                enabled = True
                i += 2
            elif l[i].isdigit():
                buffer = ""
                while l[i].isdigit():
                    buffer += l[i]
                    i += 1
                if enabled:
                    total += int(buffer)
            elif l[i] == "=":
                output_line = f"Total: {total}\n"
                print(output_line, end="")
                f.write(output_line)
                i += 1
            else:
                i += 1


line_number = 1
for line in sys.stdin:
    somar(line, line_number)
    line_number += 1