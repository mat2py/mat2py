import numpy as np

pi = np.pi
eps = np.finfo(float)

mtimes = np.dot
mrdivide = np.linalg.solve
mldivide = np.linalg.solve

clc = None
clear = None
disp = print
error = print
exp = np.exp
linspace = np.linspace
ndgrid = np.meshgrid

numel = np.size
randn = np.random.randn
rng = np.random.default_rng
sinc = np.sinc
size = np.shape
