# template_sample

attempt at removing horizontal line at the top of the page using template matching. this border was confusing the line segmentation in kraken, and I thought removing it might improve accuracy. 
The code was adapted from different tutorials online, especially from pyimagesearch. 
template matching is applied with a mask containing coordinates of the region (top of the page) where I wanted to match the template.

set_1 directory contains three sub-directory. 
1. removed_bottom has the odd case where the template was wrongly applied at the bottom despite the mask. 
2. template_removed has cases where the template was correctly applied (at the top)
3. final_process has sample pre-processed images that I pass to kraken, the ocr engine I've been training for early print in hi, bn, ur.
4. template_1.png is the template I applied on set_1. 

set_2 is another example of the same process from a different book.
1. 28.png is the image where template was matched at the bottom despite the mask.
2. 28_original.png is the original image on which the tempalte was applied.
3. template_1.png is the template.

all images have bengali text. 

template.py is how I applied the template. I defined the mask at line 47. it has coordinates of the top region of the page where I wanted to detect the template. 
