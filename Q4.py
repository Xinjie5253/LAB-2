import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
s = ctrl.TransferFunction.s

# Define constants
M=0.3
m=0.1
ell=0.35
g=9.81
a=4/(4*M+m)
b=3*m*g/(4*M+m)
c=3/ell/(4*M+m)
d=3*(M+m)*g/ell/(4*M+m)

t=sym.symbols('t')
#Define time inteval
n_points=500
t_final=0.02
t_span=np.linspace(0,t_final,n_points)
#Define input F(t)
input_t=np.sin(100*t_span**2)

# Define transfer functions G_theta_s and G_x_s symbolically:
G_theta_s = -c/(s**2-d)
G_x_s = (a-b*s*G_theta_s)/s**2
#plot the result
tf = ctrl.TransferFunction (1,1)
result_x = ctrl.forced_response(G_x_s, t_span , input_t)
result_theta= ctrl.forced_response(G_theta_s, t_span , input_t)

plt.grid()
plt.xlabel('t')
plt.ylabel('x(t), θ(t)')
plt.plot(result_x.time,result_x.outputs)
plt.plot(result_theta.time,result_theta.outputs)
plt.legend(('x(t)','θ(t)'))
plt.show()
