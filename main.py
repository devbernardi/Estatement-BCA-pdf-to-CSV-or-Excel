import argparse
from converter_estatement_bca import PDFEstatementProcessor

def main():
    parser = argparse.ArgumentParser(description="Convert BCA e-statements from PDF to CSV format")
    parser.add_argument("file_path", metavar="FILE_PATH", type=str, nargs='?', help="Path to the PDF file")
    parser.add_argument("-dir", "--directory", metavar="DIRECTORY_PATH", type=str, help="Path to the directory containing PDF files")
    args = parser.parse_args()

    pdf_processor = PDFEstatementProcessor()

    # Process the specified file
    if args.file_path:
        pdf_processor.process_file(args.file_path)
    
    # Process files in the specified directory
    elif args.directory:
        pdf_processor.process_files_in_directory(args.directory)
    
    else:
        parser.error("Either provide a file path or a directory path.")

if __name__ == "__main__":
    main()
