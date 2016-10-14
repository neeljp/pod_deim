import numpy as np
import numpy.linalg as la
import petsc_io as io
import model
import class_pod
import util
import cProfile
import time
np.set_printoptions(threshold=np.nan)
np.set_printoptions(precision=20)


n_model = class_pod.ReducedModel("reduced_basis/full_trajectory/3_snapshots_per_month/POD_100_DEIM_50/option.txt")
n_model.Init()
cProfile.run("n_model.simulate()","simulation/reduced/full_trajectory/3_snapshots_per_month/cProfile.txt") 
