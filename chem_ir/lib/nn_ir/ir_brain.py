from flask import current_app
import torch


from chem_ir.lib.nn_ir.model_definition import make_data_loader


device = 'cpu'


class IrBrain:
    def __init__(self, fgs, ys):
        self.fgs = fgs
        self.data_loader = make_data_loader(ys)

    def infer(self):
        with torch.no_grad():
            for data in self.data_loader:
                xs = data['xs'].to(device)
                output = current_app.ir_model(xs)
                output = output.cpu().numpy()

        fg_infers = current_app.fg_infers
        results = []
        for fg in self.fgs:
            info = fg_infers.get(fg)
            if info:
                is_exist = output[0][info['output_idx']] >= 0.5
                result = {
                    'sma': fg,
                    'status': 'accept' if is_exist else 'reject',
                    'confidence': info['bacc'],
                }
            else:
                result = {
                    'sma': fg,
                    'status': 'unknown',
                    'confidence': 0,
                }
            results.append(result)
        return results
