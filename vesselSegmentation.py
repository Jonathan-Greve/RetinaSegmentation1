import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

I = misc.imread('21_training.tif')
greenChannel = I[:,:,1]

def threshold_image(I,t):
    for j in range(0,len(I)):
        for i in range(0,len(I[0])):
            if (I[j][i] <= t):
                I[j][i] = 0
            else:
                I[j][i] = 1
    return I

def toOneAndZero(seg):
    for j in range(0,len(seg)):
        for i in range(0,len(seg[0])):
            if (seg[j][i] > 0):
                seg[j][i] = 1
    return seg

def reverseColors(img):
    for j in range(0,len(img)):
        for i in range(0,len(img[0])):
            if (img[j][i] == 0):
                img[j][i] = 1
            else:
                img[j][i] = 0
    return img

gtImg = reverseColors(misc.imread('21_manual1.gif'))
maskImg = toOneAndZero(misc.imread('21_training_mask.gif'))
segImg = threshold_image(greenChannel,104,)

plt.imshow(segImg, cmap="Greys")
plt.show()

def seg_eval(seg,gt,mask):
    TP = FN = TN = FP = Acc = Sens = Spec = 0
    for j in range(0,len(seg)):
        for i in range(0,len(seg[0])):
            if(mask[j][i] == 1):
                if (seg[j][i] == 1 and gt[j][i] == 1):
                    TP += 1
                elif (seg[j][i] == gt[j][i]):
                    TN +=1
                elif(seg[j][i] == 1 and gt[j][i] == 0):
                    FP +=1
                else:
                    FN +=1
    Acc = (TP + TN)*1.0 / (TP+TN+FP+FN)
    Sens = (TP)*1.0 / (TP + FN)
    Spec = (TN)*1.0 / (TN + FP)

    return (TP, FP, TN, FN, Acc, Sens, Spec)

output = seg_eval(segImg, gtImg, maskImg)
print(output)
