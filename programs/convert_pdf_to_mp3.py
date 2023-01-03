from gtts import gTTS, gTTSError
from gtts.lang import tts_langs
import pdfplumber
from pdfminer.psparser import PSException
from pathlib import Path


ALLOWED_LANGS = tts_langs()


def convert_pdf_to_mp3(file_path: str, lang: str = 'en'):
    if not Path(file_path).is_file():
        return 'File does not exist.'
    if Path(file_path).suffix != '.pdf':
        return 'Selected file is not in pdf format.'
    if lang not in ALLOWED_LANGS:
        return 'This language is not supported.'
    try:
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages).replace('\n', '')

        audio = gTTS(text=text, lang=lang)
        file_name = Path(file_path).stem
        audio.save(f'{file_name}.mp3')
        return 'Done ✔'
    except PSException as pse:
        return f'An error occurred while reading the PDF file: {pse}'
    except gTTSError as ge:
        return f'An error occurred during the conversion: {ge}'


if __name__ == '__main__':
    file_path = input('Enter a path to the pdf file: ')
    lang = input('Enter a language for example "en" or "ru": ')
    print(convert_pdf_to_mp3(file_path, lang))
