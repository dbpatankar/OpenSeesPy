
##################################################################
## 2D steel frame example.
## 3 story steel building with rigid beam-column connections.  
## This script uses W-section command inOpensees to create steel.. 
## .. beam-column fiber sections. 
##
## By - Anurag Upadhyay, PhD Student, University of Utah.
## Date - 08/06/2018
##################################################################

import openseespy.opensees as ops
import openseespy.postprocessing.Get_Rendering as opp

import numpy as np
import matplotlib.pyplot as plt
import os
from math import asin, sqrt

from SteelFrame2D import RunAnalysis

# =============================================================================
# Plot outputs
# =============================================================================

def test_animation_2D(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)

    Model = 'test'
    LoadCase = 'Pushover'
    dt = 0.2
    RunAnalysis()
    ops.wipe()
    ani = opp.animate_deformedshape( Model, LoadCase, dt, scale=10)
    plt.close()
