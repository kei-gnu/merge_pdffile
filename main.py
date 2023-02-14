import re
import os 
import PyPDF2

PDF_DIR = "./makefile_oreily"

def main():
    pdf_file_merge = PyPDF2.PdfMerger()
    list_folder_pdf = os.listdir(PDF_DIR)
    sort_list_folder_pdf = sorted(list_folder_pdf)
    print(sort_list_folder_pdf)
    
    print('start append')
    for pdf_file in sort_list_folder_pdf:
        print("test")
        pdf_file_merge.append(PyPDF2.PdfReader(PDF_DIR + "/" + pdf_file, 'rb'))
    # print('start wirte ')
    pdf_file_merge.write("./makefile_oreily.pdf")
    pdf_file_merge.close()

if __name__ == '__main__':
    main()

