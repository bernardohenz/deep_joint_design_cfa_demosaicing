import numpy as np
import time
import math

def mse(predictions,targets):
    return np.sum(((predictions - targets) ** 2))/(predictions.shape[0]*predictions.shape[1]*predictions.shape[2])

def cpsnr(img1, img2):
    mse_tmp = mse(np.round(np.clip(img1,0,255)),np.round(np.clip(img2,0,255)))
    PIXEL_MAX = 255.0
    return 10 * math.log10(PIXEL_MAX**2 / mse_tmp)

def generateMaskForImg(img,pattern_CFA):
    fixing_size = pattern_CFA-np.array([img.shape[0]%pattern_CFA[0],img.shape[1]%pattern_CFA[1]])
    fixing_size[0]= fixing_size[0]%pattern_CFA[0]
    fixing_size[1]= fixing_size[1]%pattern_CFA[1]
    mask = np.zeros((1,pattern_CFA[0]*pattern_CFA[1],img.shape[0]+fixing_size[0],img.shape[1]+fixing_size[1]))
    mask = mask.astype('float32')
    for i in range(0,img.shape[0],pattern_CFA[0]):
        for j in range(0,img.shape[1],pattern_CFA[1]):
            mask[0,0,i,j] = 1

    lastYMask = mask[0,0]
    mask_i_counter=0
    for i in range(0,pattern_CFA[0]):
        mask[0,mask_i_counter] = lastYMask
        mask_i_counter = mask_i_counter+1
        lastXMask = lastYMask
        for j in range(1,pattern_CFA[1]):
            new_mask = np.roll(lastXMask,1,axis=1)
            mask[0,mask_i_counter] = new_mask
            mask_i_counter = mask_i_counter+1
            lastXMask = new_mask
        new_mask = np.roll(lastYMask,1,axis=0)
        lastYMask = new_mask

    mask = mask[:,:,:img.shape[0],:img.shape[1]]
    return mask

def predictImg(img,autoencoder,pattern_CFA,channels_first=True):
    mask = generateMaskForImg(img,pattern_CFA)
    #img2 = np.expand_dims(np.transpose(img.astype('float32')[:,:,:3],(2,0,1))/255.0,0)
    img2 = img.astype('float32')[:,:,:3]/255.0
    if channels_first:
      img2 = np.transpose(img2,(2,0,1))
    else:
      mask = np.transpose(mask,(0,2,3,1))
    img2 = np.expand_dims(img2,0)
    start = time.time()
    prediction = autoencoder.predict([img2,mask])
    end = time.time()
    out = np.round(np.clip(prediction[0]*255,0,255))
    if channels_first:
      out = np.transpose(out,(1,2,0))
    return out,end-start


def predictImgNoise(img,autoencoder,pattern_CFA,noise_std=4,channels_first=True):
    mask = generateMaskForImg(img,pattern_CFA)
    #img2 = np.expand_dims(np.transpose(img.astype('float32')[:,:,:3],(2,0,1))/255.0,0)
    img2 = img.astype('float32')[:,:,:3]/255.0
    if channels_first:
      img2 = np.transpose(img2,(2,0,1))
    else:
      mask = np.transpose(mask,(0,2,3,1))
    img2 = np.expand_dims(img2,0)
    img2 = img2+ np.random.normal(0,noise_std/255.0,img2.shape)
    start = time.time()
    prediction = autoencoder.predict([img2,mask])
    end = time.time()
    out = np.round(np.clip(prediction[0]*255,0,255))
    if channels_first:
      out = np.transpose(out,(1,2,0))
    return out,end-start
    
def reject_outliers(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)]