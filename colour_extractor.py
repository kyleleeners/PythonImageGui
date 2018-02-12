import argparse
import glob
from PIL import Image
import pickle
import numpy as np


def load_images_from_directory(directory):
    image_list = []
    for filename in glob.glob(directory + "*.jpg"):
        try:
            image = Image.open(filename)
            image_list.append(image)
        except Exception:
            continue
    return image_list


def average_rgb_of_images(image_list, colour):
    rgb_list = []
    for image in image_list:
        try:
            arr = np.array(image)
            r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
            r_mean = int(r.mean())
            g_mean = int(g.mean())
            b_mean = int(b.mean())
            rgb_list.append((r_mean, g_mean, b_mean, colour))
        except Exception:
            continue
    return np.array(rgb_list)


def save_object(rbg_matrix, colour):
    with open('Data/%s.pickle' % colour, 'wb') as handle:
        pickle.dump(rbg_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)


def run(load_directory, colour):
    colour = str(colour)
    print("Loading images")
    image_list = load_images_from_directory(load_directory)
    print("Averaging RGB of images")
    rbg_matrix = average_rgb_of_images(image_list, colour)
    print("Serializing and Saving RGB data to pickle file")
    save_object(rbg_matrix, colour)
    print("Finished")


def main():
    parser = argparse.ArgumentParser(description='Average rgb of images')
    parser.add_argument('-c', '--colour', required=True)
    parser.add_argument('-d', '--directory', default='D:\Kyle\Projects\Images\Red\\', type=str, help='Directory of images')
    args = parser.parse_args()
    run(args.directory, args.colour)


if __name__ == '__main__':
    main()