import io
import numpy as np
import json
from flask import (
    Blueprint, request, jsonify
)
from chem_ir.controller.helper.settings import get_ip_white_list
from chem_ir.model.infrared_model import InfraredModel

ctrl = Blueprint('api', __name__)


@ctrl.before_app_request
def filter_remote_ip():
    trusted_servers = get_ip_white_list()
    # if request.remote_addr not in trusted_servers:
    #     abort(403)


@ctrl.route('/infer_ir', methods=['POST'])
def infer_ir():
    fgs = json.loads(request.form.get('fgs', default='{}'))

    content = request.files['file'].read()
    data = np.load(io.BytesIO(content))
    ys = data['ys']

    rsp = InfraredModel(fgs, ys).infer()
    return jsonify(rsp)
