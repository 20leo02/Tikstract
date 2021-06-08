import subprocess
import os


def apply_edits(video):
    """Applies all edits to the video.

    :param video: Original TikTok video
    :type video: String
    """

    apply_filters(video)
    crop_video('output.mp4')
    remove_frames('output2.mp4')
    remove_intermediates()


def apply_filters(video):
    """Mutes and reverses the video.

    :param video: Original TikTok video
    :type video: String
    """

    command = f'ffmpeg -i {video} -af volume=0 -vf reverse output.mp4'
    subprocess.call(command, shell=True)


def remove_frames(video):
    """Removes similar frames from the video.

    :param video: Intermediate video fed by crop_video.
    :type video: String
    """

    command = f'ffmpeg -i {video} -vf mpdecimate,setpts=N/FRAME_RATE/TB' \
              f' -map 0:v final.mp4'
    subprocess.call(command, shell=True)


def crop_video(video):
    """Crops the video such that only artist and song names are visible.

    :param video (str): Intermediate video fed by apply_filters
    """

    command = f'ffmpeg -i {video} -vf crop=520:145:0:570 output2.mp4'
    subprocess.call(command, shell=True)

def remove_intermediates():
    """Removes intermediate videos.
    """

    os.remove('output.mp4')
    os.remove('output2.mp4')

video = 'tiktok1.mp4'
apply_edits(video)