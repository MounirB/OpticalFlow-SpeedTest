import cv2
import os
import argparse


def create_flow_video(subfolder, axis):
    """
    Creates a flow video following the mentioned axis
    :param subfolder: path to the subfolder containing the optical flow images
    :param axis: x or y axis
    :return: writes video in the opticalflows folder
    """
    
    flow_frames = sorted([os.path.join(subfolder, frame) for frame in os.listdir(subfolder) if frame.startswith("flow_"+axis)])
    flow_frames_list.append(flow_frames)

    video_name = subfolder + '_' + axis+ '.avi'
    frame = cv2.imread(flow_frames[0])
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    for flow_frame in flow_frames:
        video.write(cv2.imread(flow_frame))

    cv2.destroyAllWindows()
    video.release()

def video_outta_frames(opticalflows_folder):
    """
    Assembles the optical flow frames within each OF folder extracted using denseflow.py into videos
    :param opticalflows_folder: the OF folder containing the optical flows of each video clip
    """
    subfolders_list = [os.path.join(opticalflows_folder, subfolder) for subfolder in os.listdir(opticalflows_folder)]

    of_frames_list = list()
    axes = ['x', 'y']
    for axis in axes:
        for subfolder in subfolders_list:
            create_flow_video(subfolder, axis)


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