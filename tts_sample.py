from TTS.api import TTS
import PyPDF2
import re
from tika import parser

class Main:

    def __init__(self, from_page, to_page):
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
        reader = PyPDF2.PdfReader('Spring_Microservices.pdf')
        x = 0
        string_to_append = ""
        for page in reader.pages:
            x = x + 1
            if x < from_page:
                continue
            if x > to_page:
                break
            new_string = page.extract_text()
            re.search("Chapter \\d", new_string);
            string_to_append = string_to_append + "\n"
            string_to_append = string_to_append + page.extract_text().replace("-\n","").replace("\n"," ")
        print(string_to_append);

        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
        tts.tts_to_file(
            text=string_to_append,
            file_path="output_lux_130_140.wav",
            speaker_wav="Lux_Elementalist_Fire_Move_10.ogg",
            speed=1.5,
            language="en")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


if __name__ == '__main__':
    Main(130, 140)
