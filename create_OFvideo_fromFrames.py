import cv2
import os
import argparse


def video_outta_frames(opticalflows_folder):
    """
    Assembles the optical flow frames within each OF folder extracted using denseflow.py into videos
    :param opticalflows_folder: the OF folder containing the optical flows of each video clip
    """
    subfolders_list = [os.path.join(opticalflows_folder, subfolder) for subfolder in os.listdir(opticalflows_folder)]

    of_frames_list = list()
    for subfolder in subfolders_list:
        of_frames = sorted([os.path.join(subfolder, frame) for frame in os.listdir(subfolder) if frame.startswith("flow_x")])
        of_frames_list.append(of_frames)

        video_name = subfolder + '.avi'
        frame = cv2.imread(of_frames[0])
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, 0, 1, (width, height))

        for of_frame in of_frames:
            video.write(cv2.imread(of_frame))

        cv2.destroyAllWindows()
        video.release()


def main(args):
    video_outta_frames(args.opticalflows_folder)


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--opticalflows_folder',
                        help='Specify the relative path of the folder containing the subfolders of Optical Flow images.',
                        type=str,
                        required=True)

    args = parser.parse_args()
    main(args)