import os
import cv2
import glob
import numpy as np
from numpy.lib.shape_base import get_array_prepare
p
ath = "clean"
if not os.path.exists(path):
    os.makedirs(path)

def  maintain_aspect_ratio_resize(image,  width=None,  height=None,  inter=cv2.INTER_AREA):
    dim =  None
    (h, w)  = image.shape[:2]
    if width is  None  and height is  None:
        return image

    if width is  None:
        r = height /  float(h)
        dim =  (int(w * r), height)
    else:
          r = width /  float(w)
          dim =  (width,  int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

for t in sorted(glob.glob(r'template/*.png')):
    print(t)
    template = cv2.imread(t, cv2.IMREAD_GRAYSCALE)
    template = cv2.Canny(template, 50, 200)
    (tH, tW)  = template.shape[:2]
    #cv2.imshow("template", template)
for filename in sorted(glob.glob('*.png')):
    print(filename)
    original_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    gray = original_image.copy()
    height, width = original_image.shape
    print(height, width)
    #gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    found =  None

    for scale in np.linspace(0.2,  1.0,  20)[::-1]:
        resized = maintain_aspect_ratio_resize(gray,  width=int(gray.shape[1]  * scale))
        r = gray.shape[1]  /  float(resized.shape[1])
        if resized.shape[0]  < tH or resized.shape[1]  < tW:
            break
        canny = cv2.Canny(resized,  50,  200)
        mask = canny[100:300, 0:2067]
        detected = cv2.matchTemplate(canny, template, cv2.TM_CCOEFF, mask)
        (_, max_val, _, max_loc)  = cv2.minMaxLoc(detected)

        if found is  None  or max_val > found[0]:
            found =  (max_val, max_loc, r)

    (_, max_loc, r)  = found
    (start_x, start_y)  =  (int(max_loc[0]  * r),  int(max_loc[1]  * r))
    (end_x, end_y)  =  (int((max_loc[0]  + tW)  * r),  int((max_loc[1]  + tH)  * r))


    cv2.rectangle(original_image,  (start_x, start_y),  (end_x, end_y),  (0,255,0),  2)
    #cv2.imshow('detected', original_image)

    cv2.rectangle(gray,  (start_x, start_y),  (end_x, end_y),  (255,255,255),  -1)
    cv2.imwrite('{}{}{}'.format(path,'/',os.path.split(filename)[1]), gray)
#cv2.waitKey(0)

