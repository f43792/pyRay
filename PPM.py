import os
from time import time
from PIL import Image


class ppm:
    """Class for save data in ppm format
    Data from: https://en.wikipedia.org/wiki/Netpbm_format"""
    def __init__(self, filename, width, height, binary=True):
        self.init_time = time()
        self.filename = filename
        self.width = width
        self.height = height
        self.binary = binary
        self.file_handle = None
        self.open_file()

    def __enter__(self):
        return self
    
    def open_file(self):
        self.file_handle = open(self.filename, 'wb+')
        self.write_header()

    def write_header(self):
        if self.file_handle is not None:
            mode = 'P6' if self.binary else 'P3'
            header = '# CREATOR: Python code "by FCN" Version 1.01'
            self.file_handle.write(f'{mode}\n{header}\n{self.width} {self.height}\n255\n'.encode('utf8'))
    
    def write_data(self, data):
        for y in range(self.height):
            for x in range(self.width):
                pix = data[y][x]
                if self.binary:
                    self.file_handle.write(bytes([pix[0], pix[1], pix[2]]))
                else:
                    self.file_handle.write(f'{pix[0]} {pix[1]} {pix[2]}\n'.encode('utf8'))
    def close(self):
        if self.file_handle:
            self.file_handle.close()

    def saveas(self, file_format):
        supported_types = ['png']
        if file_format.lower() in supported_types:
            self.close()
            im = Image.open(self.filename)
            png_filename = os.path.splitext(self.filename)[0]+'.'+supported_types[supported_types.index(file_format)]
            im.save(png_filename)
            print(f'File saved as {png_filename}')
            os.remove(self.filename)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_handle:
            self.file_handle.close()
            end_time = time() - self.init_time
            pix_by_sec = int((self.width * self.height) / end_time)
            print(f'Render of {self.width}px by {self.height}px done in {end_time:0.3f}s')
            print(f'Pixels per sec: {pix_by_sec}')


