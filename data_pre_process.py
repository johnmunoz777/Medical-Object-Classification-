import os
import shutil
import glob
import pathlib
ls
pwd
faceshield= os.listdir("face_shield")
faceshield[0:5]
len(faceshield)
folder_path = 'face_shield'
clean_folder_path = 'face_shield_clean'
os.makedirs(clean_folder_path, exist_ok=True)
files = os.listdir(folder_path)
image_files = [file for file in files if file.lower().endswith(('.jpg', '.png','.jpeg'))]
len(image_files)
image_files.sort()
image_files[0:5]
for row, file_name in enumerate(image_files):
     new_file_name = f'faceshield.{row}.jpg'
     old_file_path = os.path.join(folder_path, file_name)
     new_file_path = os.path.join(clean_folder_path, new_file_name)
     os.rename(old_file_path, new_file_path)
     shutil.move(new_file_path, os.path.join(clean_folder_path, new_file_name))
print("Files renamed and moved to 'face_shield_clean' folder.")

def rename_files(folder_name="facemask",folder_clean="facemask_clean"):
    folder_path = folder_name
    print(folder_path)
    clean_folder_path = folder_clean
    os.makedirs(clean_folder_path, exist_ok=True)
    files = os.listdir(folder_path)
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.png','.jpeg'))]
    print(len(image_files))
    image_files.sort()
    for row, file_name in enumerate(image_files):
        new_file_name = f'{folder_name}.{row}.jpg'
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(clean_folder_path, new_file_name)
        os.rename(old_file_path, new_file_path)
        shutil.move(new_file_path, os.path.join(clean_folder_path, new_file_name))
    print(f" Files renamed and moved to {clean_folder_path} folder.")
    amount_fil=os.listdir(clean_folder_path)
    print(len(amount_fil))
    return True
face_mask_done=rename_files(folder_name="facemask",folder_clean="facemask_clean")
glasses_done=rename_files(folder_name="glasses",folder_clean="glasses_clean")
gloves_done=rename_files(folder_name="gloves",folder_clean="gloves_clean")
hair_done=rename_files(folder_name="hairnet",folder_clean="hairnet_clean")
bed_done=rename_files(folder_name="hospital_bed",folder_clean="hospital_bed_clean")
operating_room_done=rename_files(folder_name="operatinglights",folder_clean="operatinglights_clean")
monitor_done=rename_files(folder_name="monitor",folder_clean="monitor_clean")
scrubs_done=rename_files(folder_name="scrubs",folder_clean="scrubs_clean")
faceshield_done=rename_files(folder_name="faceshield",folder_clean="faceshield_clean")
medical_inst=rename_files(folder_name="medical_instrument",folder_clean="medical_instrument_clean")


main_directory_path = 'c:\\Users\\johnm\\images_project'
subdirectories = [d for d in os.listdir(main_directory_path) if os.path.isdir(os.path.join(main_directory_path, d))]
for subdirectory in subdirectories:
    subdirectory_path = os.path.join(main_directory_path, subdirectory)
    files_in_subdirectory = os.listdir(subdirectory_path)
    print(f"Folder: {subdirectory}, Number of Files: {len(files_in_subdirectory)}")

folders = [
    'face_shield_clean',
    'facemask_clean',
    'glasses_clean',
    'gloves_clean',
    'hairnet_clean',
    'hospital_bed_clean',
    'medical_instrument_clean',
    'monitor_clean',
    'operatinglights_clean'
]

dp = 'all_data'
os.makedirs(dp, exist_ok=True)
for row in folders:
    sp = os.path.join(os.getcwd(), folders)
    files = os.listdir(sp)
    for file in files:
        source_file_path = os.path.join(sp, file)
        destination_file = os.path.join(dp, file)
        shutil.move(source_file_path, destination_file)

all_categories =[
'faceshield',
'facemask',
'glasses',
'gloves',
'hairnet',
'hospital_bed',
'medical_instrument',
'monitor',
'operatinglights',
'scrubs']

for row in all_categories: 
    print(row)
    
class_mapping = {category: index for index, category in enumerate(sorted(all_categories))}
numeric_labels = list(range(len(all_categories)))
class_mapping

df="all_data"
df=os.listdir(df)
len(df)
ds="all_data"
search_pattern="scrubs*"
scrub_files=glob.glob(f'{ds}/{search_pattern}') 
scrub_files[0:5]


original_dir = pathlib.Path("all_data")
new_base_dir = pathlib.Path("project_data")

def make_subset(subset_name, start_index, end_index):
    for category in all_categories:
        dir = new_base_dir / subset_name / category
        os.makedirs(dir, exist_ok=True)
        for i in range(start_index, end_index):
            fname = f"{category}.{i}.jpg"
            shutil.copyfile(src=os.path.join(original_dir, fname),
                            dst=os.path.join(dir, fname))

make_subset("train", start_index=0, end_index=700)
make_subset("validation", start_index=700, end_index=900)
make_subset("test", start_index=900, end_index=1000)



