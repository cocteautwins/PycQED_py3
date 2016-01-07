'''
Module containing functions that wrap a QCodes parameter into a sweep or
detector function
'''
from modules.measurement import sweep_functions as swf
from modules.measurement import detector_functions as det


def wrap_par_to_swf(parameter):
    '''
     - only soft sweep_functions
    '''
    sweep_function = swf.Sweep_function()
    sweep_function.sweep_control = 'soft'
    sweep_function.name = parameter.name
    sweep_function.parameter_name = parameter.label
    sweep_function.unit = ''

    sweep_function.prepare = pass_function
    sweep_function.finish = pass_function
    sweep_function.set_parameter = parameter.set
    return sweep_function


def wrap_par_to_det(parameter):
    '''
    Todo:
     - only soft detector_functions
     - only single parameter
    '''
    detector_function = det.Detector_Function()
    detector_function.detector_control = 'soft'
    detector_function.name = parameter.name
    detector_function.value_names = [parameter.label]
    detector_function.value_units = ['']

    detector_function.prepare = pass_function
    detector_function.finish = pass_function
    detector_function.acquire_data_point = parameter.get
    return detector_function

def pass_function(**kw):
    pass