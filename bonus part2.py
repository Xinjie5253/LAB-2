# We start by importing some necessary libraries (modules)
import numpy as np # this one is to do manipulate arrays 
import scipy as sp
import scipy.integrate as spi
import matplotlib.pyplot as plt  # this one is to produce nice graphs and plots
import sympy as sym

M=0.3
m=0.1
ell=0.35
g=9.81
class PidController:

  def __init__(self, kp, ki, kd, ts):
      # TODO: initialise all attributes of this class
      # The arguments kp, ki, kd are the continuous-time 
      # gains of the PID controller and ts is the sampling
      # time
      self.__kp = kp
      self.__ki = ki * ts
      self.__kd = kd / ts
      self.__sum_errors = 0
      self.__previous_error = None
     

  def control(self, y, set_point=0):
      # P for Proportional
      error = set_point - y
      u = self.__kp * error

      # I for Integral
      self.__sum_errors += error
      u += self.__ki * self.__sum_errors

      # D for Derivatives
      if self.__previous_error is not None:
          diff_errors = error - self.__previous_error
          u += self.__kd * diff_errors
      
      self.__previous_error = error
      return u




class ball:

    def __init__(self,
                 x1_ini=0,
                 x2_ini=0,
                 x3_ini=0,
                 x4_ini=0):
        self.__x = x1_ini
        self.__theta = x3_ini
        self.__x2=x2_ini
        self.__x4=x4_ini

    def theta(self):
        return self.__theta


    def move(self, F, dt):
        # This method computes the position and orientation (pose) 
        # of the car after time `dt` starting from its current 
        # position and orientation by solving an IVP
        #
        def bicycle_model(_t, z):
                x4=z[3]
                x3=z[2]
                x2=z[1]
                x1=z[0]
                return [x2,
                        (4 * m * ell * x4**2 * np.sin(x3)+4*F-3*m*g*np.sin(x3)*np.cos(x3))/(4*(M+m)-3*m*(np.cos(x3))**2),
                        x4,
                        -3*(m*ell*x4**2*np.sin(x3)*np.cos(x3)+F*np.cos(x3)-(M+m)*g*np.sin(x3))/((4*(M+m)-3*m*(np.cos(x3))**2)*ell)]
        sol = spi.solve_ivp(bicycle_model, 
                            [0, dt],
                            [self.__x,self.__x2,self.__theta,self.__x4], 
                            t_eval=np.linspace(0, dt, 2))
        new_state = sol.y[:, -1]
        self.__x = new_state[0]
        self.__x2 = new_state[1]
        self.__theta = new_state[2]
        self.__x4 = new_state[3]

   
    def state(self):
        return [self.__x, self.__theta]

henry=ball(0,0,0,0)
a = 0
b = 1
n_points = 500
# build array to store data
x_data = np.zeros((n_points+1, ))  
theta_data = np.zeros((n_points+1, ))
t_data = np.zeros((n_points+1, ))
h = (b-a)/n_points
brain = PidController(kp=20, kd=100, ki=10, ts=0.025)
# simulate for dt for each loop
for i in range(n_points+1):
    z=henry.state()
    u=brain.control(y=z[1])
    henry.move(F=np.sin(100*(a+i*h)**2)-u, dt=h)  
    x = a + i*h
    t_data[i] = x
    x_data[i] = z[0]
    theta_data[i] = np.rad2deg(z[1])
    
plt.rcParams['font.size'] = '14'
# Creating 3 subplots
plt.plot(t_data,theta_data)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()






