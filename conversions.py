"""
Useful functions for annotation conversions
Author: Bernardo Silva (https://github.com/bpmsilva)
"""
import cv2
import numpy as np

# tooth index to string (e.g. 1 -> '11', 2 -> '12', etc.)
idx = 0
IDX2STR = {}
for i in range(1, 9):
    for j in range(1, 9):
        if i > 4 and j > 5:
            continue
        idx += 1
        IDX2STR[idx] = str(i*10 + j)

# Custom color code used in the paper
COLOR_CODE = {
    'permanents': {
        '1': '#0000FF', '2': '#007FFF',
        '3': '#00FFFF', '4': '#00FF7F',
        '5': '#00FF00', '6': '#7FFF00',
        '7': '#FFFF00', '8': '#FF7F00',
    },
    'deciduous': {
        '1': '#FF0000', '2': '#FF007F',
        '3': '#FF00FF', '4': '#FF7FFF',
        '5': '#FFFFFF'
    }
}

def hex_to_decimal(hex: str) -> int:
    """Convert hexadecimal number to decimal. Useful for color conversions.

    Args:
        hex (str): hex decimal number

    Returns:
        int: decimal number
    """
    if hex[0] == '#':
        hex = hex[1:]

    return int(hex, 16)

def get_tooth_color(tooth_num: str) -> list:
    """Return the channel intensity color for the given tooth number.

    Args:
        tooth_num (str): tooth number (e.g. '11', '12', etc.)

    Returns:
        list: list of integers (channel intensities)
    """
    assert len(tooth_num) == 2, f'Invalid tooth number: {tooth_num}'

    first_digit, second_digit = tooth_num[0], tooth_num[1]
    if first_digit in ['1', '2', '3', '4']:
        hex_color = COLOR_CODE['permanents'][second_digit]
    else:
        hex_color = COLOR_CODE['deciduous'][second_digit]

    if hex_color[0] == '#':
        hex_color = hex_color[1:]

    uint8_colors = [hex_to_decimal(hex_color[2*i:2*(i+1)]) for i in range(3)] 

    return uint8_colors

def decode_segm(
    segmentation: list,
    shape: tuple,
    colors: list,
    alpha: int=127
):
    """Decode the COCO Annotator segmentation format to colored masks

    Args:
        segmentation (list): a list of list of ints for segmentation as used in the COCO format
        shape (tuple): shape of the mask in (height, width) format
        colors (list): list of three integers (range 0-255) for the channel intensity
        alpha (int, optional): int value (range 0-255). Defaults to 127.

    Returns:
        np.array: colored mask with a constant alpha channel
    """
    pts = [
        np
            .array(seg)
            .reshape(-1, 2)
            .round()
            .astype(int)
        for seg in segmentation
    ]

    colors = colors + [alpha]
    color_mask = np.zeros((shape[0], shape[1], 4), dtype=np.uint8)
    for idx, fill_color in enumerate(colors):
        mask = np.zeros(shape, dtype=np.uint8)
        color_mask[:, :, idx] = cv2.fillPoly(
            mask,
            pts,
            fill_color
        )

    return color_mask

def anns2mask(
    annotations: list,
    height: int,
    width: int,
    color_code: dict=None,
    alpha: int=127
) -> np.array:
    """Convert a image tooth annotations in the COCO format to a single colored mask

    Args:
        annotations (list): a list of annotations in the COCO format
        height (int): image/mask height
        width (int): image/mask width
        color_code (dict, optional): color code for each tooth number in the format:
            COLOR_CODE = {
                'permanents', {'SECOND_DIGIT': color '#HEX_COLOR'},
                'deciduous',  {'SECOND_DIGIT': color '#HEX_COLOR'}
            }.
            Defaults to None.
        alpha (int, optional): [description]. Defaults to 127.

    Returns:
        np.array: colored mask with a constant alpha channel
    """    
    if color_code is None:
        color_code = COLOR_CODE

    for ann in annotations:
        segmentation = ann['segmentation']
        tooth_num = IDX2STR[ann['category_id']]
        color = get_tooth_color(tooth_num)
        shape = (height, width)
        mask = decode_segm(segmentation, shape, color, alpha=alpha)

    return mask
