

import kagglehub
import os
import shutil

FASHION_MNIST_HANDLE = "zalando-research/fashion-mnist"
TARGET_RAW_DIR = "data/raw"

def download_and_move_data():
    
    os.makedirs(TARGET_RAW_DIR, exist_ok=True)
    

    cache_path = kagglehub.dataset_download(FASHION_MNIST_HANDLE)
    print(f"Dataset downloaded to cache: {cache_path}")
    

    for item in os.listdir(cache_path):
        source = os.path.join(cache_path, item)
        destination = os.path.join(TARGET_RAW_DIR, item)
        
        
        shutil.move(source, destination)
        
    print(f"Data files moved to project directory : {TARGET_RAW_DIR}")
    return TARGET_RAW_DIR

if __name__ == "__main__":
    downloaded_dir = download_and_move_data()