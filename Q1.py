import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
M, m, ell , g, x1, x2, x3, x4, F =\
sym.symbols('M, m, ell , g, x1, x2, x3, x4, F')
phi = (4 * m * ell * x4**2 * sym.sin(x3)+4*F-3*m*g*sym.sin(x3)*sym.cos(x3))/ \
(4*(M+m)-3*m*(sym.cos(x3))**2)

psi=-3*(m*ell*x4**2*sym.sin(x3)*sym.cos(x3)+F*sym.cos(x3)-(M+m)*g*sym.sin(x3))/ \
((4*(M+m)-3*m*(sym.cos(x3))**2)*ell)     
# at F=0, x3=0 and x4=0
def evaluate_at_equilibrium(f):
    return f.subs ([(F, 0), (x3, 0), (x4, 0)])
# Compute the derivatives of phi at the equilibrium point
dphi_F_eq = evaluate_at_equilibrium(phi.diff(F))
dpsi_F_eq = evaluate_at_equilibrium(psi.diff(F))
dphi_x3_eq = evaluate_at_equilibrium(phi.diff(x3))
dpsi_x3_eq = evaluate_at_equilibrium(psi.diff(x3))
dphi_x4_eq = evaluate_at_equilibrium(phi.diff(x4))
dpsi_x4_eq = evaluate_at_equilibrium(psi.diff(x4))

print(f" derivatives of phi respect to F is:  \n")
sym.pprint(dphi_F_eq)
print(f" derivatives of psi respect to F is: \n")
sym.pprint(dphi_F_eq)
print(f" derivatives of phi respect to x3 is:  \n")
sym.pprint(dphi_x3_eq)
print(f" derivatives of psi respect to x3 is:  \n")
sym.pprint(dphi_x3_eq)
print(f" derivatives of phi respect to x4 is:   \n")
sym.pprint(dphi_x4_eq)
print(f" derivatives of psi respect to x4 is:  \n")
sym.pprint(dphi_x4_eq)


