# clean pdf for input into llm prompt

input_path = "./data/machlearn.pdf"

def read_pdf(input_path, output_path):
    from PyPDF2 import PdfReader

    pdf_reader = PdfReader(input_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"

    # Save to txt
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Saved text to {output_path}")
    return text

def read_txt(input_path):
     # Read txt file
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text