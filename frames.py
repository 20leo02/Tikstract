import os, subprocess, pytesseract, cv2

try:
    from PIL import Image
except ImportError:
    import Image

pytesseract.pytesseract.tesseract_cmd = \
    'C:/Users/leora/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'



def get_num_frames(video='final.mp4'):
    """Obtain the number of frames in the final video.

    :param video: Edited (reversed, trimmed, muted, cropped) video.
    :type video: String
    :return num_frames: The number of frames in the video.
    """

    cap = cv2.VideoCapture(video)
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return num_frames





def save_frames():
    frames = get_num_frames()
    """Saves frames from the final video into the image_frames folder in the
    directory.
    """
    if not os.path.exists('image_frames'):
        os.makedirs('image_frames')

    cap = cv2.VideoCapture('final.mp4')
    idx = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        name = f'./image_frames/frame {idx}.jpg'
        cv2.imwrite(name, frame)
        idx += 1
        if idx == frames:
            break


whitelist = \
    "' 'abcdefghijklmnopqrtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ91234567890()-?!+\\'"


def get_tracks(playlist, idx=0):
    """Reads artist and song name from each frame using Tesseract and plugs
     into a playlist dictionary.

     :param playlist: Dictionary holding song as key and artist as value.
     :type playlist: dict
     :param idx: Integer representing frame index, starting from 0.
     :type idx: int
     """
    frames = get_num_frames()
    if idx > frames - 1:
        return playlist

    img = f'C:/Users/leora/PycharmProjects/spotifyReader/image_frames/frame {idx}.jpg'

    text=pytesseract.image_to_string(img, config=f"-c tessedit_char_whitelist={whitelist}")
    text = text_cleanup(text)
    li = text.splitlines()
    if '' in li:
        li.remove('')

    if len(li) < 2:
        if idx <= frames - 1:
            return get_tracks(playlist, idx=idx + 1)
        elif len(li) < 1:
            return playlist

    playlist[li[0]] = li[1]
    # print(playlist)

    return get_tracks(playlist, idx=idx + 1)


def text_cleanup(text):
    """Removes extraneous information from song and artist names.

    :param text: Text obtained from read_frames.
    :type text: String
    """

    if ' (' or ' -' in text:
        r1 = text[text.find(' ('):text.find('\n')]
        r2 = text[text.find('-'):text.find('\n')]
        text = text.replace(r1, '')
        text = text.replace(r2, '')

    text = text.strip()
    # text = text[:text.rfind('\n')]
    return text


# img = "./image_frames/frame 17.jpg"
# t = (pytesseract.image_to_string(img,
#                                  config=f"-c tessedit_char_whitelist={whitelist}")).strip()
# t = text_cleanup(t)
# print(t)
#
# ply = {}
# play = get_tracks(ply)
# print(play)
# #
