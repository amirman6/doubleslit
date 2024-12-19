# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:46:42 2024

@author: T430s
"""



import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image



def Double_slit_intensity(a,d,theta,lamda):
    I_o = 1  # maximum intensity
    theta_range = np.linspace(-theta,theta,500)
    theta1 = (3.14/180)*theta # to radians
    angle = np.linspace(-theta1,theta1,500) # angle scan
    alpha = (3.14/lamda)*a*np.sin(angle)
    gamma = (3.14/lamda)*d*np.sin(angle)
    I = I_o*np.cos(gamma)**2*(np.sin(alpha)/alpha)**2 # intensity scan
    #plt.plot(theta_range, I)
    fig,ax = plt.subplots()
    ax.plot(theta_range,I)
    plt.xlabel('Angle (Degrees)')
    plt.ylabel('Relative Intinsity')
    plt.show()
    st.pyplot(fig)
    
# running the function  
#Double_slit_intensity(0.04E-4,0.25E-3,3,650E-9)  # double slit with single slit effect

#Double_slit_intensity(0.02E-4,0.00002E-3,60,650E-9) # making d versy small, just a single slit effect

#Double_slit_intensity(0.00002E-4,0.02E-3,10,650E-9) # making a very small, just a double slit effect


image = Image.open('double_slit.jpg')
st.image(image)

st.write("""
##### Double Slit Experiment Fringe Intensity Calculation
-- by A. Maharjan
##### 
""")
st.sidebar.write("Change the variables from the slider")
a = st.sidebar.slider("Slit Width 'a' (mm):", 0.001,0.1,0.04)
a = a*1E-3
d = st.sidebar.slider("Slit Spacing 'd' (mm):", 0.01,1.0,0.25)
d = d*1E-3
theta = st.sidebar.slider("Viewing Angle '𝜃' (+/-degrees):", 1,10,2)
lamda = st.sidebar.slider("Wavelength of Light 'λ' (nm):", 400,750,700)
lamda = lamda*1E-9
Double_slit_intensity(a,d,theta,lamda) # does instant update of the result
#if st.button('Press here to calculate and simulate'):
    #Double_slit_intensity(a,d,theta,lamda)
    
  
