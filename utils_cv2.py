import cv2
import numpy as np

def ScaleAndCropImage(img,factor_scale=1):
    
    # Crop is done in the center of the image
    h, w = img.shape[:2]
    img_resized = cv2.resize(img, (int(factor_scale*w), int(factor_scale*h)),interpolation=cv2.INTER_CUBIC)
    h_resized, w_resized = img_resized.shape[:2]
    
    if factor_scale > 1:
        b_left = (w_resized - w)/2
        b_up = (h_resized - h)/2
        img_resized = img_resized[int(b_up):int(b_up) + h, int(b_left):int(b_left) + w]
        return img_resized
    
    elif factor_scale < 1:
        background = np.zeros((img.shape), dtype = "uint8")
        b_left = (w - w_resized)/2
        b_up = (h - h_resized)/2
        background[int(b_up):int(b_up) + h_resized, int(b_left):int(b_left) + w_resized] = img_resized
        return background
    
    else:
        return img