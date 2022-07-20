import re
import os
import chardet
import codecs
def correct_encoding(book_name):
    with codecs.open(book_name, "r", "gb18030") as f:
        print("Converting Encoding")
        data = f.read()
        with codecs.open(book_name, "w", "utf-8") as newfile:
            newfile.write(data)


def check_encoding(book_name):
    with open(book_name, "rb") as f:
        data = f.read(10000)
        encoding = chardet.detect(data)['encoding']
        if encoding != 'utf-8':
            correct_encoding(book_name)
    
             

def parse(book_name):
    check_encoding(book_name)
    with open(book_name) as f:
        chapter_names = list()
        chapter_contents = list()
        counter = -1
        for line in f:
            if line == "\n":
                continue
            if line.strip().startswith("第") and line.find("章") != -1:
                chapter_names.append(line.strip())
                counter += 1
                empty_list = list()
                chapter_contents.append(empty_list)
            if counter > -1:
                chapter_contents[counter].append(line.strip())
        return (chapter_names, chapter_contents)

