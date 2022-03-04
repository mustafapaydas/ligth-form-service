import os
def exists_path(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)