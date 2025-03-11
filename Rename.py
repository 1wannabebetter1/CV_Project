import os

def rename_subfolders(base_path, translate):
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path) and folder in translate:
            new_name = translate[folder]
            new_path = os.path.join(base_path, new_name)
            if not os.path.exists(new_path):
                os.rename(folder_path, new_path)
                print(f'Renamed "{folder}" to "{new_name}"')
            else:
                print(f'Skipping "{folder}" as "{new_name}" already exists')

if __name__ == "__main__":
    base_directory = "./data/raw-img/"
    translate = {
        "cane": "dog",
        "cavallo": "horse",
        "elefante": "elephant",
        "farfalla": "butterfly",
        "gallina": "chicken",
        "gatto": "cat",
        "mucca": "cow",
        "pecora": "sheep",
        "scoiattolo": "squirrel",
        "dog": "cane",
        "cavallo": "horse",
        "ragno": "spider"
    }

    rename_subfolders(base_directory, translate)