#!/usr/bin/env python3

import os
import shutil

# Default path for the Downloads directory in macOS
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads') # add your downloads path
images_path = '/Users/NAME/Documents/Images' # add your images path here

# Checking whether an item is in the set is more efficient than in a list, especially as the size of the collection grows, because sets in Python are implemented as hash tables.

image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

def move_images(src_path, dst_path, extensions):
    for item in os.listdir(src_path):
        # Create tuple b/c it's more efficient to perform a single method call than to loop through each possible extension in set and check individually
        if item.lower().endswith(tuple(extensions)):
            src_item = os.path.join(src_path, item)
            dst_item = os.path.join(dst_path, item)
            shutil.move(src_item, dst_item)
            print(f'Moved: {item}')

#Print for testing
print(f"Downloads path: {downloads_path}")
print(f"Images path: {images_path}")

# Move the images
move_images(downloads_path, images_path, image_extensions)

if __name__ == '__main__':
    move_images(downloads_path, images_path, image_extensions)



