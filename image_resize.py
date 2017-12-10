import argparse
import os
from PIL import Image


def resize_image(path_to_original, path_to_result):
    image = Image.open(path_to_original)
    if args.scale:
        if args.scale > 0:
            output_file_width, output_file_height = map(lambda x: x*args.scale,
                                                        image.size)
        else:
            output_file_width, output_file_height = map(
                                            lambda x: -1*x//args.scale,
                                            image.size)

        image = image.resize((output_file_width, output_file_height),
                             Image.ANTIALIAS)

    if args.output:
        image.save(args.output)
    else:
        output_file_name, output_file_extension = os.path.basename(
            file_name).split('.')
        output_file = '{}__{}x{}.{}'.format(output_file_name, output_file_width,
                                    output_file_height, output_file_extension)
        image.save(output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resize an image.')

    parser.add_argument('file', metavar='image file',
                        help='path to an image file')
    parser.add_argument('--scale', '-s', type=int,
                        help='scale by a factor of s')
    parser.add_argument('--width', type=int, help='image width')
    parser.add_argument('--height', type=int, help='image height')
    parser.add_argument('--output', '-o', help='path to an output image')

    args = parser.parse_args()

    if not (args.scale or args.width or args.height):
        parser.error(
            'one of resize parameters must be given:'
            ' [-s | {--width and/or --height}]')

    if args.scale and (args.width or args.height):
        parser.error('error: --width or --height not allowed with --scale.')

    resize_image(args.file, args.output)
