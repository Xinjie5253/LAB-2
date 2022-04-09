import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

a, b, c, d = sym.symbols('a:d', real=True , positive=True)
s = sym.symbols('s')
t=sym.symbols('t')
# Define G_theta symbolically:
G_theta = -c/(s**2-d)
G_x = (a-b*s*G_theta)/s**2

# step response for theta
theta_s_step = G_theta/s # response in s−domain
theta_t_step = sym.inverse_laplace_transform(theta_s_step,s,t)

# impulse response for theta
theta_s_impulse = G_theta # response in s−domain
theta_t_impulse = sym.inverse_laplace_transform(theta_s_impulse,s,t)

# step response for x
x_s_step = G_x/s # response in s−domain
x_t_step = sym.inverse_laplace_transform(x_s_step,s,t)

# impulse response for x
x_s_impulse = G_x 
x_t_impulse = sym.inverse_laplace_transform(x_s_impulse,s,t)


sym.pprint(theta_t_step)
sym.pprint(theta_t_impulse)
sym.pprint(x_t_step )
sym.pprint(x_t_impulse)

# Bode plot
s=ctrl.TransferFunction.s
M=0.3
m=0.1
ell=0.35
g=9.81
a=4/(4*M+m)
b=3*m*g/(4*M+m)
c=3/ell/(4*M+m)
d=3*(M+m)*g/ell/(4*M+m)
G_theta = -c/(s**2-d)
G_x = (a-b*s*G_theta)/s**2
mag, phase, omega = ctrl.bode(G_theta)
mag, phase, omega = ctrl.bode(G_x)

plt.show()
