import sys

def somar(l):
    total = 0
    enabled = True
    buffer = ""

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
            print(f"Total: {total}")
            i += 1
        else:
            i += 1

for line in sys.stdin:
    somar(line)