import numpy as np
import matplotlib.pyplot as plt



RHO = 1 # kg/m^3 Density
v = 0.01 # m/s^2 Kinematic Viscosity
GRID_SIZE = (41,41)
DOMAIN_SIZE = (1,1) #m


def main():
    grid, ux, uy, px, py = initialize_mesh()



def mesh():
    pass

def initialize_mesh(grid: np.array):
    (x,y) = np.meshgrid(GRID_SIZE)
    ux = np.zeros_like(grid)
    uy = np.zeros_like(grid)
    px = np.zeros_like(grid)
    py = np.zeros_like(grid)
    
    return grid, ux, uy, px, py
    
    
def enforce_boundary_conditions():
    pass

def enforce_u_boundary_condition():
    #rlu dirichlet 0 in x, 0 in y direction
    #o dirchtlet 1m/s in x, 0 in y direction
    pass

def enforce_p_boundary_condition():
    # rlu Neumann 0
    # o Dirichlet 0 Pa
    pass



def du_dx():
    pass
def du_dy():
    pass

def dv_dx():
    pass
def dv_dy():
    pass

def laplace():
    pass

