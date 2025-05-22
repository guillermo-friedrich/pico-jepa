import os
import csv

def get_video_paths(root, video_extensions):
    video_paths = []
    for root_directory, subdirectory, files in os.walk(root):
        for file_n in files:
            if file_n.endswith(video_extensions): #Solo archivos .mp4
                complete_path = os.path.join(root_directory, file_n)
                video_paths.append(complete_path)

    return video_paths

def save_csv_paths(paths, file_csv):
    with open(file_csv, mode='w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=' ')
        for count, path in enumerate(paths, start=0):
            csv_writer.writerow([path, count])


root = os.path.dirname(os.path.abspath(__file__))
csv_file = 'nano-k400_train.csv'
video_extensions = '.mp4'

if __name__ == '__main__':
    video_paths = get_video_paths(root, video_extensions)
    save_csv_paths(video_paths, csv_file)