from llama_parse import LlamaParse, base

instruction = '''
The provided document is a FortiGate Administration Guide.  
Try to ignore all the images.
Try to remove the headers and footers. 
The provided document contains the configuration CLI, keeping all the configuration.
'''

parser = LlamaParse(api_key="llx-rN9lacezooFnMmkIkiDJdWvHEIpfGl5ka9p0K9jtvtKtXEf8", parsing_instruction="instruction", 
                    disable_ocr=True, skip_diagonal_text=True,
                    result_type=base.ResultType.MD, bounding_box="0.1, 0, 0.1, 0")
documents = parser.load_data("./input/policy.pdf")
text = ''
for document in documents:
    print(document.text)
    text += document.text

output_txt = './input/policy.txt'
with open(output_txt, 'w', encoding='utf-8') as txt_file:
    txt_file.write(text)
