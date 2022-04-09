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
t_final=2
t_span=np.linspace(0,t_final,n_points)
#Define input F(t)
input_t=np.sin(100*t_span**2)
# Define transfer functions G_theta_s and G_x_s symbolically:
G_theta_s = -c/(s**2-d)
G_x_s = (a-b*s*G_theta_s)/s**2

def pid(kp , ki , kd):
# This function constructs the transfer function of a PID
# controller with given parameters
    diff = ctrl.TransferFunction ([1, 0], 1)
    intgr = ctrl.TransferFunction (1, [1, 0])
    pid_tf = -(kp + kd * diff + ki * intgr)
    return pid_tf


controller = pid(kp=50 , ki=100 , kd=100)
closed_loop_tf = ctrl.feedback(G_theta_s , controller)

result_theta= ctrl.forced_response(closed_loop_tf, t_span , input_t)

plt.xlabel('t')
plt.ylabel('θ(t)')
plt.grid()
plt.plot(result_theta.time, np.rad2deg(result_theta.outputs))
plt.show()
