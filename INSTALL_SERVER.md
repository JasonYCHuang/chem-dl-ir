# INSTALL FLASK SERVER

## 1. Installation

### 1.1. Install Anaconda

Please refer to `https://www.anaconda.com/`.

You can follow our [unofficial Anaconda installations for Dummies](INSTALL_BASIC.md) for a test installation.

However, it is highly recommended to refer to official websites.

### 1.2. Create env

_Logout & login to load installations._

```
$ conda create --name chem-dl-ir python=3.7
$ source activate chem-dl-ir
```

```
$ conda install -c rdkit rdkit=2020.09.1.0
$ sudo apt-get install gcc libxrender1 libxext-dev pkg-config
```

```
$ git clone https://github.com/JasonYCHuang/chem-dl-ir.git
$ cd ~/chem-dl-ir
$ pip install -r requirements.txt --ignore-installed
```

### 1.3. Start server

Go to the project folder.

```
$ cd ~/chem-dl-ir
```

Using only "one" of following commands.

##### 1.3.1 run on the production server
```
$ gunicorn -w 1 -t 600 -b 0.0.0.0:3008 server:app --daemon
```

##### 1.3.2 for local development only
```
$ export FLASK_APP=chem_ir && export FLASK_ENV=development && python -m flask run --eager-loading --host=0.0.0.0 --port=3008
```

### 1.4. Quick test

You should receive `pong` when executing the following command from another machine.

```
$ curl xxx.xxx.xxx.xxx:3008/ping
```
