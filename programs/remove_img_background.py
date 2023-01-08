from rembg import remove
from PIL import Image
from pathlib import Path


def remove_bg(input_dir: str, output_dir: str):
    extensions_list = ['*.png', '*.jpg']    # добавить нужные расширения
    all_images = []

    for ext in extensions_list:
        all_images.extend(Path(input_dir).glob(ext))

    for index, image in enumerate(all_images, 1):
        input_path = Path(image)
        file_name = input_path.stem
        output_path = f'{output_dir}/{file_name}_out.png'

        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f'Complete: {index}/{len(all_images)}')


def main():
    input_dir = 'programs/input_for_remove_bg'
    output_dir = 'programs/output_for_remove_bg'
    remove_bg(input_dir, output_dir)


if __name__ == '__main__':
    main()
