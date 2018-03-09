# Deep Joint Design of Color Filter Arrays and Demosaicing

This is our Keras implementation for reconstructing test images of known datasets using our trained models.

## Prerequisites
- Python 2 or 3
- Keras (tested for both Theano and Tensorflow backends)

## Getting Started

### Installation
- Install Keras along with your preferred backend
- Clone this repository

### Downloading our trained models
- Download trained models
```bash
bash ./trained_models/download_trained_models.sh
```

### Replicating the results from our paper
- Download test datasets
```bash
bash ./datasets/download_datasets.sh
```
- Run the test script
```bash
python test.py
```
- You can specify desired parameters like the following example
```bash
python test.py --datasets kodak --model our_4x4_noise --noise_std 4 --output_dir results_noise_std4
```
Parameter ```--datasets``` specifies the test dataset you want to evaluate (```[all | kodak | mcm | hdrvdp | moire]```)

Parameter ```--model``` specifies the trained model to be loaded (```[our_4x4_noise-free | our_4x4_noise | bayer ]```)

Parameter ```--noise_std``` specifies the noise std to be added to the original image (in the scale ```[0,255]```)

Parameter ```--output_dir``` specifies the folder where the reconstructions will be saved (the script will not save the reconstructions if this is not specified)

### Running our models in images
- Running the specified model on a particular image
```bash
python reconstruct_image.py --img_name datasets/kodak/kodim01.png --model our_4x4_noise-free --output_name out.png
```
- Running the specified model on directory
```bash
python reconstruct_images_from_dir.py --dir datasets/kodak --model our_4x4_noise-free --output_dir results_kodak
```

## Training code
Soon. The original code was in Keras v1, we are preparing the script.


## Citation
If you use this code, please cite our paper
```
@article{HenzGastalOliveira_2018,
    author = {Bernardo Henz and Eduardo S. L. Gastal and Manuel M. Oliveira},
    title   = {Deep Joint Design of Color Filter Arrays and Demosaicing},
    journal = {Computer Graphics Forum},
    volume = {37},
    year    = {2018},
    }
```
