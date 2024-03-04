import numpy as np
from TTS.api import TTS
import pdfplumber
import re


class Main:
    the_set: set = {"init"}

    def __init__(self, from_page, to_page):
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
        concat = None
        with pdfplumber.open('Spring_Microservices.pdf') as pdf:
            for x in range(from_page, to_page):
                text = pdf.pages[x]
                clean_text = text.filter(lambda obj: self.filter(obj))
                print(self.the_set)
                string = clean_text.extract_text().replace("-\n", "").replace("\n", " ")
                # string = re.sub("[^a-zA-Z1-9. \\(\\)]", "", string)
                print(string)
                wav: np.ndarray = tts.tts(
                    text=string,
                    speaker_wav="Lux_Elementalist_Fire_Move_10.ogg",
                    speed=1.5,
                    language="en")
                print("Page: " + str(x) + " done!")
                if concat is None:
                    concat = wav
                else:
                    np.concatenate([concat, wav])
        tts.synthesizer.save_wav(wav=concat, path="output_" + str(from_page) + "_" + str(to_page) + ".wav")
        print(self.the_set)

    def filter(self, obj) -> bool:
        #if "fontname" in obj:
        #    self.the_set.add(obj["fontname"])
        return obj["object_type"] == "char" and not (
                "Bold" in obj["fontname"] or "Courier" in obj["fontname"])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == '__main__':
    Main(130, 135)
