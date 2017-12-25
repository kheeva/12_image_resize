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
        type=float,
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
    return parser


def get_scaled_width_height(image_object, scale):
    return map(lambda x: int(x*scale), image_object.size)


def get_second_output_side(width, height, out_width, out_height):
    if out_width:
        return height * out_width // width
    return width * out_height // height


def make_output_filename(path_to_file, file_width, file_height):
    file_name, file_extension = os.path.splitext(path_to_file)
    return '{}__{}x{}.{}'.format(
        file_name,
        file_width,
        file_height,
        file_extension
    )


def resize_image(image_object, path_to_result, width, height):
    output_image = image_object.resize(
        (width, height),
        Image.ANTIALIAS)
    output_image.save(path_to_result)


if __name__ == '__main__':
    argparse_parser = get_arguments()
    args = argparse_parser.parse_args()

    if not (args.scale or args.width or args.height):
        argparse_parser.error(
            'one of resize parameters must be given:'
            ' [-s | {--width and/or --height}]')

    if args.scale and (args.width or args.height):
        argparse_parser.error('error: --width or --height not allowed'
                              'with --scale.')

    for argument in [args.scale, args.width, args.height]:
        if argument and argument < 0:
            argparse_parser.error('scale/width/height must be positive INT')

    image = Image.open(args.file)
    image_width, image_height = image.size

    if args.scale and args.scale > 0:
        output_image_width, output_image_height = get_scaled_width_height(
            image,
            args.scale
        )
    elif args.width and args.height:
        print('warning: simultaneous using width and height may cause '
              'image disproportion.')
        output_image_width = args.width
        output_image_height = args.height
    elif args.width:
        output_image_width = args.width
        output_image_height = get_second_output_side(
            image_width,
            image_height,
            output_image_width,
            None
        )
    else:
        output_image_height = args.height
        output_image_width = get_second_output_side(
            image_width,
            image_height,
            None,
            output_image_height
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
        image,
        result_file_path,
        output_image_width,
        output_image_height
    )
