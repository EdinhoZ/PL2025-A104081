import re
import sys
import os

def markdown_to_html(md_text):
    # Converte cabeçalhos
    md_text = re.sub(r'(?m)^###### (.+)$', r'<h6>\1</h6>', md_text)
    md_text = re.sub(r'(?m)^##### (.+)$', r'<h5>\1</h5>', md_text)
    md_text = re.sub(r'(?m)^#### (.+)$', r'<h4>\1</h4>', md_text)
    md_text = re.sub(r'(?m)^### (.+)$', r'<h3>\1</h3>', md_text)
    md_text = re.sub(r'(?m)^## (.+)$', r'<h2>\1</h2>', md_text)
    md_text = re.sub(r'(?m)^# (.+)$', r'<h1>\1</h1>', md_text)
    
    # Negrito
    md_text = re.sub(r'\*\*(.*?)\*\*|__(.*?)__', r'<b>\1\2</b>', md_text)
    
    # Itálico
    md_text = re.sub(r'\*(.*?)\*|_(.*?)_', r'<i>\1\2</i>', md_text)
    
    # Imagens
    md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', md_text)

    # Links
    md_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', md_text)
    
    # Listas ordenadas
    md_text = re.sub(r'(?m)^(\d+\.\s+.*(?:\n\d+\.\s+.*)*)', lambda m: '<ol>\n' + re.sub(r'\d+\.\s+(.*)', r'    <li>\1</li>', m.group(1)) + '\n</ol>', md_text)
    
    # Listas não ordenadas
    md_text = re.sub(r'(?m)^([*-]\s+.*(?:\n[*-]\s+.*)*)', lambda m: '<ul>\n' + re.sub(r'[*-]\s+(.*)', r'    <li>\1</li>', m.group(1)) + '\n</ul>', md_text)
    
    return md_text.strip()


def main(args):
    
    if len(args) != 3:
        print("Usage: conversorMDtoHTML.py <file.md>")
        return 1

    md_location = args[1]
    output_location = args[2]
    os.makedirs(output_location, exist_ok=True)
    output_file = f"{output_location}/{os.path.basename(md_location).replace('input.md', 'output.html')}"
    with open(md_location, "r", encoding="utf-8") as md_file:
        md_sample = md_file.read()
        res = markdown_to_html(md_sample)
        print(res)
        with open(output_file, "w", encoding="utf-8") as output:
            output.write(res)

if __name__ == "__main__":
    main(sys.argv)