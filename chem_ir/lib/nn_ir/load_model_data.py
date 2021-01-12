from __future__ import print_function
from pathlib import Path
import torch
import pickle

import chem_ir.lib.nn_ir.model_definition
from chem_ir.lib.nn_ir.model_definition import Net


fn_dict_fg_acc_results = f'{Path().absolute()}/training_spectrum_to_fgs/checkpoints/dict_fg_acc_results.pk'
model_state_dict_path = f'{Path().absolute()}/training_spectrum_to_fgs/checkpoints/ir-model_state_dict-01.pt'


def ir_model():
    print('Loading the model...')
    m = Net()
    m.load_state_dict(torch.load(model_state_dict_path), strict=False)
    m.eval()

    print('The model is loaded!')
    return m


def fg_infers():
    load_fg_to_accs = None
    with open(fn_dict_fg_acc_results, 'rb') as file:
        load_fg_to_accs = pickle.load(file)

    return load_fg_to_accs
