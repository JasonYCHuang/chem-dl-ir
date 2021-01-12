from chem_ir.lib.nn_ir.ir_brain import IrBrain


class InfraredModel:
    def __init__(self, fgs, ys):
        self.fgs = fgs
        self.ys = ys

    def infer(self):
        results = IrBrain(self.fgs, self.ys).infer()
        results = sorted(results, key=lambda r: -r['confidence'])

        return {
            'outline': {
                'code': 200,
                'text': 'IR inference success.'
            },
            'output': {
                'result': [
                    {
                        'type': 'ir',
                        'fgs': results,
                    }
                ],
            },
        }
