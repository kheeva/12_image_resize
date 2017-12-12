import os
import argparse
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
    elif args.width and args.height:
        output_file_width = args.width
        output_file_height = args.height
    else:
        img_width, img_height = image.size
        if args.width:
            output_file_width = args.width
            output_file_height = img_height*output_file_width//img_width
        else:
            output_file_height = args.height
            output_file_width = img_width*output_file_height//img_height

    image = image.resize((output_file_width, output_file_height),
                         Image.ANTIALIAS)

    if not path_to_result:
        output_file_name, output_file_extension = os.path.basename(
            path_to_original).split('.')
        path_to_result = '{}__{}x{}.{}'.format(
            output_file_name, output_file_width, output_file_height,
            output_file_extension)

    image.save(path_to_result)


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

    if args.width and args.height:
        print('warning: simultaneous using width and height may cause '
              'image disproportion.')

    resize_image(args.file, args.output)
