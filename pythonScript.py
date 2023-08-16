import fitz

def process_pdf(input_fname, output_fname):
    doc = fitz.open(input_fname)

    # List of words to search for
    words_to_search = [
       "word1","word2" # Add more words here
    ]

    # List of corresponding words to insert for each search word
    words_to_insert = [
       "insert1","insert2"   # Add more words here
    ]



    for page_number in range(doc.page_count):
        page = doc.load_page(page_number)
        page.clean_contents(False)

        for i in range(len(words_to_search)):
            word = words_to_search[i]
            insert_word = words_to_insert[i]

            draft = page.search_for(word)

            for rect in draft:
                annot = page.add_redact_annot(rect)
                page.apply_redactions()
                page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
                page.insert_text((rect.x0, rect.y0 + 5), insert_word, fontsize=7)

    doc.save(output_fname)
    doc.close()

if __name__ == "__main__":
    input_file = r"input.pdf"
    output_file = r"output.pdf"
    process_pdf(input_file, output_file)

