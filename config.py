ACTION_DIM = 2
STOP_DIM = 1
IMAGE_WIDTH = 200
IMAGE_HEIGHT = 88
IMAGE_TENSOR_HEIGHT = 3
IMAGE_TENSOR_WIDTH = 10

EVAL_FRAMERATE_SCALE = 1
DATASET_FRAMERATE = 10
SCALE = 6

CAMERA_KEYWORDS = ['left', 'center', 'right', 'extra']
STEER_OFFSET_ABS = 0.1
CAMERA_STEER_OFFSET_DICT = {
    'left': STEER_OFFSET_ABS,
    'center': 0.0,
    'right': -STEER_OFFSET_ABS,
    'extra': 0.0}
