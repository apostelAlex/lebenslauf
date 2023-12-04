import time
import easyocr
from pypdf import PdfReader

def create_pdf(docx_path):
    pass


def image_detect(paths, langs=['de']) -> str:
    reader = easyocr.Reader(langs)
    text = ""
    for path in paths:
        result = reader.readtext(path)
        for i in result:
            text += i[-2] + "\n"
    return text


def main(path=None):
    if path == None:
        path = input("Please enter the path for the pdf: \n")
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)
    count = 0
    text = []
    images = []
    for n in range(number_of_pages):
        page = reader.pages[n]
        text += [page.extract_text()]

        # for i in page.images:
        #     i = i.data
        #     with open(f"/Users/a2/.cache/img/{count}image", "wb") as f: 
        #         f.write(i)
        #     images += [f"/Users/a2/.cache/img/{count}image"]
        #     count += 1
            
    text += [image_detect(images)]

    t = "\n".join(text)
    return t
    ti = str(int(time.time()))
    # with open("/Users/a2/Documents/transcripts/"+ti+".txt", "w") as f:
    #     f.write(t)

if __name__ == "__main__":
    main()
   