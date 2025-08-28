from pypdf import PdfReader

def extract_text_from_pdf(pdf_path, output_txt_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:  # Skip empty pages
            full_text += f"--- Page {page_num} ---\n{text}\n\n"
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"Text extracted to {output_txt_path}")

# Usage: Replace with your file paths
extract_text_from_pdf("life 3.0.pdf", "life_3.0_extracted.txt")