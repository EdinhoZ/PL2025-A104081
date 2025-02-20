import os
import sys

def parse_csv(filename):
    rows = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        next(file)
        row = []
        field = ""
        inside_quotes = False

        for line in file:
            line = line.strip()

            i = 0
            while i < len(line):
                char = line[i]

                if char == '"':
                    if inside_quotes and i + 1 < len(line) and line[i + 1] == '"':
                        field += '"'
                        i += 1
                    else:
                        inside_quotes = not inside_quotes
                elif char == ';' and not inside_quotes:
                    row.append(field.strip())
                    field = ""
                else:
                    field += char 
                
                i += 1
            
            if inside_quotes:
                field += " "
            else:
                row.append(field.strip())
                rows.append(row)
                row = []
                field = ""

    return rows


def order_composers(filename, outputs):
    pieces = parse_csv(filename)

    output_file = f"{outputs}/ordered_composers.txt"

    ordered_composers = set()

    with open(output_file, "w") as f:
        for piece in pieces:
            composer = piece[4]
            if composer not in ordered_composers:
                ordered_composers.add(composer)

    
        ordered_composers = sorted(set(ordered_composers), key=str.lower)
        for composer in ordered_composers:
            f.write(composer + "\n")
        
        return ordered_composers

def distribute_per_period(filename, outputs):
    pieces = parse_csv(filename)

    output_file = f"{outputs}/distribution_per_period.txt"

    dist_periods = {}
    for piece in pieces:
        period = piece[3]

        if period not in dist_periods:
            dist_periods[period] = 1
        else:
            dist_periods[period] += 1

    with open(output_file, "w") as f:
        for period in dist_periods:
            f.write(f"{period}: {dist_periods[period]}\n")
    
    return dist_periods

def titles_per_period(filename, outputs):
    pieces = parse_csv(filename)

    output_file = f"{outputs}/titles_per_period.txt"

    dist_titles_per_period = {}

    for piece in pieces:
        title = piece[0]
        period = piece[3]

        if period not in dist_titles_per_period:
            dist_titles_per_period[period] = []
        
        dist_titles_per_period[period].append(title)

    with open(output_file, "w") as f:   
        for period in dist_titles_per_period:
            dist_titles_per_period[period].sort()
            f.write(f"{period}: {dist_titles_per_period[period]}\n")
            print(f"{period}: {dist_titles_per_period[period]}")

    
    return dist_titles_per_period

   
folder = "outputs"
os.makedirs(folder, exist_ok=True)
print(distribute_per_period(sys.argv[1], folder))
print(order_composers(sys.argv[1], folder))
print(titles_per_period(sys.argv[1], folder))