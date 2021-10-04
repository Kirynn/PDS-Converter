"""
Author: Kirynn

Description: Converts a powerpoint file to a mp4 file

TODO:
* Multithread
* Add proper handling for paths
* Progressbar
* Better error handling
"""

import win32com.client
import time
import os

from pathlib import Path
from collections import deque

def convert(file : str, outputDir : str):

        powerpoint = win32com.client.Dispatch("Powerpoint.Application")
        filename = Path(file).stem

        output_file = f'C:\\stuff\\{filename}.mp4'

        if (os.path.isfile(output_file)):
            print("File already done.")
            return

        try:
            # Attempt to open file
            #presentation = powerpoint.Presentations.Open(FileName='lol.pptx', WithWindow=False)
            presentation = powerpoint.Presentations.Open(FileName=file, WithWindow=False)
        except:
            # If file cannot be found
            print('File cannot be found')
            exit
        try:
            # May need a few other parameters as well
            print(f'{outputDir}\\{filename}')
            presentation.CreateVideo(output_file)
            while presentation.CreateVideoStatus == 1:
                time.sleep(1)
            presentation.Close()
            print('Done')
        except Exception as err:
            print('Unable to export to video')
        
           
        powerpoint.Quit()
        del powerpoint

if __name__ == "__main__":

    input_folder : str = r"C:\Users\Kirynn\OneDrive\University\School Work\CISC 447\Converter\input" #input("Input Folder:")
    output_folder : str = r"C:\Users\Kirynn\OneDrive\University\School Work\CISC 447\Converter\output" #input("Output Folder")

    work : deque = deque([])

    for root, _, files in os.walk(input_folder):

        for file in files:

            filepath = os.path.join(root, file)
            filename = file.split(".")[0]
            
            convert(filepath, output_folder)