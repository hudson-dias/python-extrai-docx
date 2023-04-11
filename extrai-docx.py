import docx

def extract_text_from_docx(docx_path):
    document = docx.Document(docx_path)
    full_text = []
    for paragraph in document.paragraphs:
        full_text.append(paragraph.text)
    with open("arquivo.txt", "w") as log_file:
        log_file.write("\n".join(full_text))
    return '\n'.join(full_text)

docx_file_path = 'arquivo.docx'
text_content = extract_text_from_docx(docx_file_path)
# print(text_content)