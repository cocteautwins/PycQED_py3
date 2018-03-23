"""
This is the file one imports for daily use.
This file should only contain import statements to import functions
from other files in the analysis_v2 module.
"""

# This snippet ensures all submodules get reloaded properly
from importlib import reload
import pycqed.analysis_v2.base_analysis as ba
import pycqed.analysis_v2.simple_analysis as sa
import pycqed.analysis_v2.timedomain_analysis as ta
import pycqed.analysis_v2.readout_analysis as ra
import pycqed.analysis_v2.syndrome_analysis as synda
# only one of these two files should exist in the end
import pycqed.analysis_v2.cryo_scope_analysis as csa
import pycqed.analysis_v2.distortions_analysis as da
import pycqed.analysis_v2.optimization_analysis as oa

reload(ba)
reload(sa)
reload(synda)
reload(ta)
reload(da)
reload(ra)
reload(csa)
reload(oa)

from pycqed.analysis_v2.base_analysis import *
from pycqed.analysis_v2.simple_analysis import (
    Basic1DAnalysis, Basic2DAnalysis)
from pycqed.analysis_v2.timedomain_analysis import (
    FlippingAnalysis, Intersect_Analysis, CZ_1QPhaseCal_Analysis,
    Conditional_Oscillation_Analysis, Idling_Error_Rate_Analyisis,
    Grovers_TwoQubitAllStates_Analysis)
from pycqed.analysis_v2.readout_analysis import Singleshot_Readout_Analysis, \
    Multiplexed_Readout_Analysis
from pycqed.analysis_v2.syndrome_analysis import (
    Single_Qubit_RoundsToEvent_Analysis, One_Qubit_Paritycheck_Analysis)


from pycqed.analysis_v2.cryo_scope_analysis import RamZFluxArc, SlidingPulses_Analysis
from pycqed.analysis_v2.distortions_analysis import Scope_Trace_analysis

from pycqed.analysis_v2.optimization_analysis import OptimizationAnalysis
