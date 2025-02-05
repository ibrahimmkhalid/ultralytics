#!/bin/bash
# SFDT_Ibrahim YOLO 🚀, AGPL-3.0 license
# Download COCO128 dataset https://www.kaggle.com/sfdt_ibrahim/coco128 (first 128 images from COCO train2017)
# Example usage: bash data/scripts/get_coco128.sh
# parent
# ├── sfdt_ibrahim
# └── datasets
#     └── coco128  ← downloads here

# Download/unzip images and labels
d='../datasets' # unzip directory
url=https://github.com/sfdt_ibrahim/assets/releases/download/v0.0.0/
f='coco128.zip' # or 'coco128-segments.zip', 68 MB
echo 'Downloading' $url$f ' ...'
curl -L $url$f -o $f -# && unzip -q $f -d $d && rm $f &

wait # finish background tasks
