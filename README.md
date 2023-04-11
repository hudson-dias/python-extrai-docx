# Script Python para extrair texto de arquivos .docx

Este script Python utiliza a biblioteca `docx` para extrair o texto de arquivos .docx e salvar em um arquivo de texto.

## Como utilizar

1. Instale a biblioteca `docx` utilizando o comando `pip install python-docx`.

2. Execute o script `extract_text_from_docx.py`, passando como argumento o caminho do arquivo .docx que deseja extrair o texto.

3. O texto será salvo em um arquivo de texto chamado `arquivo.txt`.

## Exemplo de uso

```
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
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
