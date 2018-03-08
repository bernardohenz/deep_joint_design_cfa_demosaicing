# Deep Joint Design of Color Filter Arrays and Demosaicing

This is our Keras implementation for reconstructing test images of known datasets using our trained models.

## Prerequisites
- Python 2 or 3
- Keras (tested for both Theano and Tensorflow backends)

## Getting Started

### Installation
- Install Keras along with your preferred backend
- Clone this repository

### Testing our models
- Download test datasets
```bash
cd datasets/
bash ./datasets/download_datasets.sh
cd ..
```
- Download trained models
```bash
cd trained_models/
bash ./trained_models/download_trained_models.sh
cd ..
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
