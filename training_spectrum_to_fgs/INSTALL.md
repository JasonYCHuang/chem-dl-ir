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

##### TBD

```
$ pip install numpy pandas matplotlib scikit-learn scipy Flask
$ pip install git+https://github.com/ComPlat/nmrglue.git@be0990cf066d9264945747e67e76d24d0b866000
```

##### >> make sure you are in `chem-dl-ir/training_spectrum_to_fgs`.


```
$ pip install -r requirements.txt
```

##### Add conda to jupyter

```
$ python -m ipykernel install --user --name=deep-ir-01
```


# 2. Training and Validation

run following files one-by-one


```
01_load_data.ipynb
02_train_model.ipynb
03_verify_model_and_save_acc.ipynb
```

