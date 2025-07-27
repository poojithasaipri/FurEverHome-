import os

migration_files = [
    "adoption/migrations/0002_remove_pet_breed.py",
    "adoption/migrations/0003_pet_image_alter.py"
]

for file_path in migration_files:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    else:
        print(f"File not found: {file_path}")
