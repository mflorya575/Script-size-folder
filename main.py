import os
import scandir


def get_size(start_path='C:/ваш/путь/к_папке'):
    total_size = 0
    for dirpath, dirnames, filenames in scandir.walk(start_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size


print(get_size(), 'bytes')
