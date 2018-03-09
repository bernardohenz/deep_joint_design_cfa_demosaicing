from keras.models import Model,model_from_json
from PIL import Image
import scipy
import numpy as np
import glob, os, time, random, math, sys
import argparse
from keras import backend as K

from utils_test import *


parser = argparse.ArgumentParser()
parser.add_argument('--img_name',required=True, help='specify the image you would like to reconstruct')
parser.add_argument('--model',default='our_4x4_noise-free', help='select which model to load [our_4x4_noise-free | our_4x4_noise | bayer ]')
parser.add_argument('--noise_std',default=0,type=int,help='the noise std used (use 0 for no noise)')
parser.add_argument('--output_name',default=None,help='specify the name to export the reconstructed images (if None, the image will not be exported)')
parser.add_argument('--dim_order',default=None,help='specify the dim order [channels_first | channels_last ](if None, the dim order will be selected automatically)')

opt = parser.parse_args()

if opt.dim_order is None:
   if (K.backend() == 'tensorflow'):
      last_channel = True
   elif (K.backend() == 'theano'):
      last_channel = False
   else:
      sys.exit('Error: unable to automatically set dim order. Please, specify one manually.')
elif opt.dim_order == 'channels_first':
   last_channel = False
elif opt.dim_order == 'channels_last':
   last_channel = True
else:
   sys.exit('Error: invalid dim_order. Choose a valid one.')


if (opt.model == 'our_4x4_noise-free'):
   pattern_CFA = (4,4)
   if (last_channel):
      json_file = open('trained_models/4x4_noise-free_tf.json','r')
   else:
      json_file = open('trained_models/4x4_noise-free_th.json','r')
   weights_path = 'trained_models/4x4_noise-free.h5'
   loaded_model_json = json_file.read()
   json_file.close()
   
elif (opt.model == 'our_4x4_noise'):
   pattern_CFA = (4,4)
   if (last_channel):
      json_file = open('trained_models/4x4_noise_tf.json','r')
   else:
      json_file = open('trained_models/4x4_noise_th.json','r')
   loaded_model_json = json_file.read()
   json_file.close()
   weights_path = 'trained_models/4x4_noise.h5'
elif (opt.model == 'bayer'):
   pattern_CFA = (2,2)
   if (last_channel):
      json_file = open('trained_models/2x2_bayer_tf.json','r')
   else:
      json_file = open('trained_models/2x2_bayer_th.json','r')
   loaded_model_json = json_file.read()
   json_file.close()
   weights_path = 'trained_models/2x2_bayer.h5'
else:
   sys.exit('Error: invalid model. Choose a valid model')
    

autoencoder = model_from_json(loaded_model_json)
autoencoder.load_weights(weights_path)
print('Loaded model: ',os.path.splitext(os.path.basename(weights_path))[0])


print('Starting prediction on img: ',opt.img_name)

img = np.asarray(Image.open(opt.img_name)).astype('float32')
if ( opt.noise_std >0):
   predicted,time = predictImgNoise(img,autoencoder,pattern_CFA,opt.noise_std,not last_channel)
else:
   predicted,time = predictImg(img,autoencoder,pattern_CFA,not last_channel)
psnr = cpsnr(img,predicted)

print("{:s} - psnr: {:.2f} time : {:.2f} seg".format(opt.img_name,psnr,time))

if (opt.output_name is not None):
      scipy.misc.toimage(predicted,cmin=0,cmax=255).save(opt.output_name)


