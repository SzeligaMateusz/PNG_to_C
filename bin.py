#------------------------------------------# Autor #----------------------------------------------#
# yes, that code was generated by ChatGPT,                                                        #
#   why?                                                                                          #
# Because I wouldn't have written it myself, it's only for my convenience （*゜ー゜*）             #
# I just edit this for my preferences, that's all. ¯\_(ツ)_/¯                                     #
#-------------------------------------------------------------------------------------------------#

# This code uses Pillow, which is licensed under the HPND License.~
# This code uses datatime/os, which is licensed under the Python Software Foundation License.
# See the "https://github.com/python-pillow/Pillow/blob/main/LICENSE" access: 18.08.2024 | 20:23| for details.
# See the "https://docs.python.org/3/license.html" access: 18.08.2024 | 20:23| for details.
# This code in the bin.py file except pillow and datatime is for everyone, just make sure you follow the HPND and Python Software Foundation License.

#-------------------------------------- # How to use # -------------------------------------------#
# 1. Take your PNG file to folder and rename to "input.png".                                      #
# 2. Compile the program                    (!)_You must have a Pillow ("pip install pillow")_(!) #
# 3. Now you can see the output file (output_year_month_day-hour_minute)                          #
# 4. Copy the contents of the file and Ctrl-V to your project.                            #
#-------------------------------------------------------------------------------------------------#
#-------------------------------# Thanks, good luck with your code :P #-------------------------- #
#-------------------------------------------------------------------------------------------------#
import os
from datetime import datetime
from PIL import Image

def convert_image_to_rgb565(image_path, output_base_name):
    # Otwórz obraz
    image = Image.open(image_path)
    # Zmień rozmiar obrazu, jeśli to konieczne
    image = image.resize((240, 240))
    # Konwertuj obraz do RGB
    image = image.convert('RGB')
    
    # Przygotuj tablicę na dane RGB565
    rgb565_data = []

    for y in range(240):
        for x in range(240):
            r, g, b = image.getpixel((x, y))
            rgb565 = ((r & 0xf8) << 8) | ((g & 0xfc) << 3) | (b >> 3)
            rgb565_data.append(rgb565)

    print("Generating time label")
    now = datetime.now()
    date_str = now.strftime("%Y_%m_%d")
    time_str = now.strftime("%H_%M")
    output_path = f"{output_base_name}_{date_str}-{time_str}.c"
    
    # Zapisz dane do pliku C
    with open(output_path, 'w') as f:
        for i, value in enumerate(rgb565_data):
            if i % 12 == 0:
                f.write('\n')
            f.write(f'0x{value:04X}, ')

    print(f"Date: {date_str} Time:{time_str} :)")
    print(f"Output file = {output_path}")

# Ścieżka do obrazu wejściowego
image_path = 'input.png'
# Nazwa bazowa pliku wyjściowego (bez rozszerzenia)
output_base_name = 'output'
convert_image_to_rgb565(image_path, output_base_name)

