# Waveshare Image Loader

## Installation

On Raspbian Lite install this:
`apt install -y libjpeg-dev zlib1g-dev wiringpi`

You need to have virtualenv installed. See the [virtualenv installation guide](https://virtualenv.pypa.io/en/latest/installation)

```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

`python3 imageloader.py <black_image_path> <color_image_path>`

Example:
`python3 imageloader.py img/leon.bmp img/leon_red.bmp`


