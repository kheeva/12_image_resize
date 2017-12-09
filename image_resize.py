import argparse


def resize_image(path_to_original, path_to_result):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resize an image.')

    parser.add_argument('file', metavar='image file',
                        help='path to an image file')
    parser.add_argument('--scale', '-s', type=float,
                        help='scale an image in s times')
    parser.add_argument('--width', type=float, help='image width',
                        )
    parser.add_argument('--height', type=float, help='image height',
                        )
    parser.add_argument('--output', '-o', help='path to an output image')

    args = parser.parse_args()

    if not (args.scale or args.width or args.height):
        parser.error(
            'one of resize parameters must be given:'
            ' [-s | {--width and/or --height}]')

    if args.scale and (args.width or args.height):
        parser.error('error: --width or --height not allowed with --scale.')
