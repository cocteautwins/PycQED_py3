#!/usr/bin/python

import os
import logging
import numpy as np

from pycqed.instrument_drivers.physical_instruments.Transport import IPTransport
from pycqed.instrument_drivers.physical_instruments.QuTechCC import QuTechCC

from pycqed.measurement.openql_experiments import single_qubit_oql as sqo
import pycqed.measurement.openql_experiments.multi_qubit_oql as mqo


# constants
ip = '192.168.0.241'
qubit_idx = 10
curdir = os.path.dirname(__file__)
cfg_openql_platform_fn = os.path.join(curdir, 'demo1_cfg.json')


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

if 0:
    # based on CCL_Transmon.py::measure_allxy()
    log.debug('compiling allxy')
    p = sqo.AllXY(qubit_idx=qubit_idx, double_points=True, platf_cfg=cfg_openql_platform_fn)
    print(p.filename)

if 1:
    # based on CCL_Transmon.py::measure_ramsey()
    # funny default is because there is no real time sideband
    # modulation
    log.debug('compiling Ramsey')
    T2_star = 20e-6
    cfg_cycle_time = 20e-9
    stepsize = (T2_star * 4 / 61) // (abs(cfg_cycle_time)) \
               * abs(cfg_cycle_time)
    times = np.arange(0, T2_star * 4, stepsize)
    p = sqo.Ramsey(times, qubit_idx=qubit_idx, platf_cfg=cfg_openql_platform_fn)
    print(p.filename)

if 0:
    # based on CCL_Transmon.py::measure_rabi_channel_amp()
    log.debug('compiling Rabi')
    p = sqo.off_on(
        qubit_idx=qubit_idx, pulse_comb='on',
        initialize=False,
        platf_cfg=cfg_openql_platform_fn)
    print(p.filename)


if 1:
    log.debug('connecting to CC')
    cc = QuTechCC('cc', IPTransport(ip))
    cc.reset()
    cc.clear_status()
    cc.set_status_questionable_frequency_enable(0x7FFF)

    log.debug('uploading {}'.format(p.filename))
    if 0:
        cc.eqasm_program = p.filename
    else:
        with open(p.filename, 'r') as f:
            prog = f.read()
        cc.sequence_program(prog)

    err_cnt = cc.get_system_error_count()
    for i in range(err_cnt):
        print(cc.get_error())

    log.debug('starting CC')
    cc.start()
