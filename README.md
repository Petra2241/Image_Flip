# Image_Flip

Flips all images in a folder vertically.  Output is in _flipped folder within the original that contained the images.

_flipped folder cannot exist on subsequent runs.

Requires Pillow
```
pip install --upgrade pil
pip install --upgrade pillow
```


Usage
```
python .\imageflip.py "[path to folder containing images to be flipped]"
```
Quotation marks are needed if the above path has spaces