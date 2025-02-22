import os
import shutil
import random

image_dir = "../image_chips_native"
label_dir = "../labels/labels_native"
output_dir = "../dataset"

train_image_dir = os.path.join(output_dir, "images/train")
val_image_dir = os.path.join(output_dir, "images/val")
test_image_dir = os.path.join(output_dir, "images/test")

train_label_dir = os.path.join(output_dir, "labels/train")
val_label_dir = os.path.join(output_dir, "labels/val")
test_label_dir = os.path.join(output_dir, "labels/test")

for folder in [train_image_dir, val_image_dir, test_image_dir, train_label_dir, val_label_dir, test_label_dir]:
    os.makedirs(folder, exist_ok=True)

image_files = sorted([f for f in os.listdir(image_dir)])
random.seed(42)
random.shuffle(image_files)

train_split = int(0.8 * len(image_files)) 
test_split = len(image_files) - train_split
val_split = int(0.1 * train_split)

train_files = image_files[:train_split - val_split] 
val_files = image_files[train_split - val_split:train_split]  
test_files = image_files[train_split:]  

def move_files(files, src_img_dir, src_lbl_dir, dest_img_dir, dest_lbl_dir):
    for file in files:
        shutil.copy(os.path.join(src_img_dir, file), os.path.join(dest_img_dir, file))

        label_file = file.replace(".tif", ".txt")
        if os.path.exists(os.path.join(src_lbl_dir, label_file)):
            shutil.copy(os.path.join(src_lbl_dir, label_file), os.path.join(dest_lbl_dir, label_file))

move_files(train_files, image_dir, label_dir, train_image_dir, train_label_dir)
move_files(val_files, image_dir, label_dir, val_image_dir, val_label_dir)
move_files(test_files, image_dir, label_dir, test_image_dir, test_label_dir)

print(f"Dataset split completed!")
print(f"Train: {len(train_files)} images")
print(f"Validation: {len(val_files)} images")
print(f"Test: {len(test_files)} images")
