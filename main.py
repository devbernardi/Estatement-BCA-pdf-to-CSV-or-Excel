from converter_estatement_bca import PDFEstatementProcessor

def main():
    pdf_processor = PDFEstatementProcessor()

    # Process files in a directory
    directory = "file/dir"
    pdf_processor.process_files_in_directory(directory)

    # Process a single file
    file_path = "C://ESTATEMENT FEB 24.pdf"
    pdf_processor.process_file(file_path)

if __name__ == "__main__":
    main()
