# Install Manually

```bash
$ conda create --name chem-dl-ir python=3.7
$ source activate chem-dl-ir

$ pip install numpy pandas torch torchvision torchaudio matplotlib scikit-learn scipy Flask git+https://github.com/ComPlat/nmrglue.git@be0990cf066d9264945747e67e76d24d0b866000#egg=nmrglue

$ conda install -c rdkit rdkit=2020.09.1.0
$ conda install -c anaconda ipykernel
```
