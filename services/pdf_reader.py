import pymupdf


def extract_text(upload_file):

    filename = upload_file.filename.lower()

    if filename.endswith(".txt"):
        return upload_file.file.read().decode("utf-8")

  
    elif filename.endswith(".pdf"):

        pdf_bytes = upload_file.file.read()

        document = pymupdf.open(stream=pdf_bytes, filetype="pdf")

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    else:
        raise ValueError("Only PDF and TXT files are supported.")