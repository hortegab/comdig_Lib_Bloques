import math
import numpy
#######################################################
##        Hecho por Homero Ortega Boada              ##
##        comdiguis@saber.uis.edu.co                 ##
##     Universidad Industrial de Santander           ##
#######################################################

#######################################################
##               Forma rectangular                   ##
#######################################################                       
def rect(Sps):
    return Sps*[1.,]

#######################################################
##               Forma de Nyquist                    ##
#######################################################                       
def nyq(Sps,ntaps):
    n=numpy.linspace(-int(ntaps/2), int(ntaps/2-1),ntaps)
    h=numpy.sinc(n/Sps)
#    return h/numpy.amax(h)
    return h
#######################################################
##               Forma Coseno Alzado                 ##
#######################################################                       
def rcos(Sps,ntaps,beta):
    if beta==0:
        h=nyq(Sps,ntaps)
    else:
        h=ntaps*[0,]
        for n in range(ntaps):
            k=n-ntaps/2. # esto es para que h[n] quede centrada en la mitad del vector
            if abs(k)==Sps/(2.*beta):
                h[n]=numpy.sinc(1./(2.*beta))*math.pi/4.
            else:
                h[n]=numpy.sinc(k/Sps)*math.cos(beta*k*math.pi/Sps)/(1.-(2.*beta*k/Sps)**2)                
    Amp=numpy.amax(h)
    return h/Amp
#######################################################
##            Forma Raiz de Coseno Alzado            ##
#######################################################                       

def rrcos(Sps,ntaps,beta):
    if beta==0:
        h=nyq(Sps,ntaps)
    else:
        h=ntaps*[0,]
        beta4=4.*beta
        for n in range(ntaps):
            k=n-ntaps/2. # esto es para que h[n] quede centrada en la mitad del vector
            if k==0:
                h[n]=1+beta*(4./math.pi-1.)
            elif abs(k)==Sps/beta4:
                ha=(1.+2./math.pi)*math.sin(math.pi/beta4)
                hb=(1.-2./math.pi)*math.cos(math.pi/beta4)
                h[n]=(ha+hb)*beta/math.sqrt(2.)
            else:
                ks=k/Sps
                kspi=math.pi*ks
                Num=math.sin(kspi*(1-beta))+beta4*ks*math.cos(kspi*(1+beta))
                Den=kspi*(1.-(beta4*ks)**2)
                h[n]=Num/Den                
    Amp=numpy.amax(h)
    return h/Amp
########################################################
##     Bipolar non return to zero level signal        ##
########################################################
def B_NRZ_L(Sps):
    return Sps*[1.,]

########################################################
##  Forma sinc . Es la misma nyq() que aparece arriba ##
########################################################
def sinc(Sps,ntaps):
    n=np.linspace(-int(ntaps/2), int(ntaps/2-1),ntaps)
    h=np.sinc(n/Sps)
    return h
########################################################
##              forma diente se sierra                ##
########################################################
def saw(Sps):
    return np.linspace(0,Sps-1,Sps)	
########################################################
#         Bipolar non return to zero signal           ##
########################################################
def RZ(Sps):
    h=Sps*[1.,]
    Sps_m=int(Sps/2)
    h[Sps_m+1:Sps:1]=np.zeros(Sps-Sps_m)
    return h
