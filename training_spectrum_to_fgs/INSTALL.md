# INSTALL

This guidance is tested on Linux Ubuntu 18.04.

## 1. Installation

### 1.1. Install Anaconda

Please refer to `https://www.anaconda.com/`.

You can follow [unofficial Anaconda installations for Dummies](INSTALL_BASIC.md) for a test installation.

However, it is highly recommended to refer to official websites.

### 1.2. Create env

_Logout & login to load installations._

```
$ conda create --name deep-ir-01 python=3.7
$ source activate deep-ir-01
```

```
$ conda install -c rdkit rdkit=2020.09.1.0
$ conda install -c anaconda ipykernel
```

```
$ sudo apt-get install gcc libxrender1 libxext-dev pkg-config
```

```
# install pytorch version, here we use cpu version, please refer to `https://pytorch.org/`
$ conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

```
$ pip install numpy pandas matplotlib scikit-learn scipy Flask git+https://github.com/ComPlat/nmrglue.git@be0990cf066d9264945747e67e76d24d0b866000#egg=nmrglue
```

##### Add conda to jupyter

```
$ python -m ipykernel install --user --name=deep-ir-01
```


# 2. Training and Validation

1. To get nist data, you should buy it from `https://www.nist.gov/srd/nist-standard-reference-database-35`, and put & rename the folder to `./data/nist/`.

![nist data](https://github.com/JasonYCHuang/chem-dl-ir/blob/master/training_spectrum_to_fgs/assets/nist.jpg)


2. run following files one-by-one


```
01_load_data.ipynb
02_train_model.ipynb
03_verify_model_and_save_acc.ipynb

04_count_spectra.ipynb
```

