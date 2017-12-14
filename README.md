# Image Resizer

Takes an image file, resize it according to user settings.

# How to Install

You just need to download and install python3 if you already haven't: http://python.org .
Also you need to install Pillow package. Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL.

```bash
pip install -r requirements.txt
```
or
```
pip install Pillow
```

# How to use

You can run image_resize.py with some arguments.
You need at least one of these below:
*`--scale (-s) INT` or
*`--width INT` or/and
*`--height INT` or/and
Obviously, path to original file is required..
*`--output(-o) path_to_result_file`
*`path_to_original_file`


There are some examples:

* Resizing to 555-width image (height will auto-fit without disproportion).
```
python image_resize.py --width 555 logo.png
```

* Double an image.
```
python image_resize.py -s 2 logo.png
```

* Setting manual parameters and save it to new_logo.png.
```
python image_resize.py --width 500 --height 700 -o new_logo.png logo.png
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
