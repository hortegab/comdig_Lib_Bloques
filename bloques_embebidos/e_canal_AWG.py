import numpy as np
import random
import math
from gnuradio import gr

class blk(gr.sync_block):
    """
Es un canal AWGN (Additive Whaite Gaussian Noise, en banda base). 
Solo pide la relacion senal a ruido en dB. Internamente mide la potencia de la senal entrante
despejar la potencia del ruido que cumpla con la SNR 
SNR-Db: es la relacion senal a ruido en dB
    """
    def __init__(self, SNR_dB=-40):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='e_Canal_AWGN',
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        self.SNR_dB = SNR_dB
     
    def work(self, input_items, output_items):
        L=len(input_items[0])
        Pin=np.mean(np.absolute(input_items[0])**2)  # calculo de la varianza (potencia promedio normalizada) del ruido
        output_items[0][:] = input_items[0]+noise_c(L, self.SNR_dB, Pin)
        return len(output_items[0])

def noise_c(N,SNR_dB,P_s):
# N: es el numero de elementos en el vector
# P_s: es la varianza (potencia promedio) de la senal entrante. 
# SNR_dB: es la relacion senal a ruido en dB del ruido respecto a P_signal
    SNR=pow(10.,SNR_dB/10.)   # traduccion a lineal
    P_n = P_s/SNR  # la potencia del ruido
    sigma = math.sqrt(P_n) # es porque la funcion random.normal() pide la desviacion standard
    n=np.random.normal(0.,sigma,N)+np.random.normal(0.,sigma,N)*1.j
    return n
