# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract

import os
import glob

class File_reader:

    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.files_path = self.dir_path + '/files'
        self.texts = [] # здесь будет список всех текстовых файлов (переработанные)
        self.images = [] # здесь будет список всех фотографий
        self.all_files()

# вытаскивает все названия файлов из папки
    def all_files(self):
        image_files = glob.glob(self.files_path + '/*.png')
        self.images.extend(image_files)

        image_files = glob.glob(self.files_path + '/*.jpg')
        self.images.extend(image_files)

        image_files = glob.glob(self.files_path + '/*.gif')
        self.images.extend(image_files)

        text_files = glob.glob(self.files_path + '/*.txt')
        self.texts.extend(text_files)

        self.check_new_files()

# сравнивает, есть ли не переведенные из фото в текст файлы, если такие есть, переводит в текст
    def check_new_files(self):
        if len(self.texts) <= len(self.images):
            for i in self.images:
                if i + '.txt' not in self.texts:
                    self.read_and_wite(i)
        else:
            for i in self.texts:
                if i  not in self.images + '.txt':
                    self.texts.pop(self.texts.index(i))

# поиск ключевых слов, возвращает список с файлами
    def searh(self, words):
        files = []
        if words:
            for word in words:
                for text in self.texts:
                    if text not in files:
                        try:

                            with open(text, 'r') as f:
                                for line in f:
                                    if word.lower() in line.lower():
                                        files.append(text)
                                        break

                        except:
                            pass
        
        return files
# переводит фото файлы в текст
    def read_and_wite(self, path):
        try:
            with open(path+'.txt', 'w') as f:
                text = pytesseract.image_to_string(Image.open(path), lang = 'rus')
                f.write(text)
        except:
            pass

if __name__ == "__main__":
    a = File_reader()
    print(a.searh(['печать', 'Довереность']))