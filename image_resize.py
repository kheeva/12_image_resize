import os
import argparse
from PIL import Image


def get_arguments():
    parser = argparse.ArgumentParser(description='Resize an image.')
    parser.add_argument(
        'file',
        metavar='image file',
        help='path to an image file'
    )
    parser.add_argument(
        '--scale',
        '-s',
        type=int,
        help='scale by a factor of s'
    )
    parser.add_argument(
        '--width',
        type=int,
        help='image width'
    )
    parser.add_argument(
        '--height',
        type=int,
        help='image height'
    )
    parser.add_argument(
        '--output',
        '-o',
        help='path to an output image'
    )
    return parser.parse_args()


def get_output_file_width_and_height(path_to_original, scale, width, height):
    image = Image.open(path_to_original)
    if scale:
        if scale > 0:
            output_file_width, output_file_height = map(
                lambda x: x * scale,
                image.size
            )
        else:
            output_file_width, output_file_height = map(
                lambda x: -1 * x // scale, image.size)
    elif width and height:
        output_file_width = width
        output_file_height = height
    else:
        img_width, img_height = image.size
        if width:
            output_file_width = width
            output_file_height = img_height * output_file_width // img_width
        else:
            output_file_height = args.height
            output_file_width = img_width * output_file_height // img_height

    return output_file_width, output_file_height


def make_output_filename(path_to_file, file_width, file_height):
    file_name, file_extension = os.path.basename(
        path_to_file).split('.')

    return '{}__{}x{}.{}'.format(
        file_name,
        file_width,
        file_height,
        file_extension
    )


def resize_image(path_to_original, path_to_result, image_width, image_height):
    image = Image.open(path_to_original)
    image = image.resize(
        (image_width, image_height),
        Image.ANTIALIAS
    )
    image.save(path_to_result)


if __name__ == '__main__':
    args = get_arguments()
    if not (args.scale or args.width or args.height):
        parser.error(
            'one of resize parameters must be given:'
            ' [-s | {--width and/or --height}]')

    if args.scale and (args.width or args.height):
        parser.error('error: --width or --height not allowed with --scale.')

    if args.width and args.height:
        print('warning: simultaneous using width and height may cause '
              'image disproportion.')

    output_image_width, output_image_height = get_output_file_width_and_height(
        args.file,
        args.scale,
        args.width,
        args.height
    )

    if not args.output:
        result_file_path = make_output_filename(
            args.file,
            output_image_width,
            output_image_height
        )
    else:
        result_file_path = args.output

    resize_image(
        args.file,
        result_file_path,
        output_image_width,
        output_image_height
    )
