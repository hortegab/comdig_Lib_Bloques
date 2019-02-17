import numpy as np
import cmath
from gnuradio import gr

###########################################################################
##                    Constructor del bloque                             ##
###########################################################################
class mi_bloque_embebido(gr.sync_block):

    """
Aqui debe ir la documentacion del bloque.

Como aun no se sabe como va a quedar la version definitiva. Estamos poniendo las explicaciones 
dentro del texto del codigo
"""
    ############################################################################################
    ##  Constructor del bloque                                                                ##
    ############################################################################################

    def __init__(self, N=17):  
        gr.sync_block.__init__(
            self,
            name='e_BER_Tool',
            in_sig=[np.int8, np.int8],
            out_sig=[np.float32]
        )

        self.N=N # es el numero de puntos de la curva de SER a calcular
#        self.SNR=np.linspace(SNRmin,SNRmax,self.N) # es la relacin senal a ruido en dB
#        self.potencia=potencia # es la potencia de la senal que entra al canal. Sirve para despejar
                               # del SNR la potencia del ruido
        self.k=N # es la identificacin de la muesta actual del vector SNR
        self.errores = np.zeros(self.N)
        # count: cuenta el numero de muestras que ya han sido procesadas para cada punto de la BER
        # es el mismo para cualquier punto.
        self.count=0. 
        # SER: es la memoria de la ultima curva calculada
        self.SER=np.ones(self.N) 

    ############################################################################################
    ##  Lo de arriba es solo el constructor del bloque). Aqui comienza el verdadero cdigo     ##
    ############################################################################################

    def work(self, input_items, output_items):
        in0=input_items[0]
        in1=input_items[1]
        

        # L: es el tamano del vector de entrada. 
          
        L=len(in0) 
        
        # count: cuenta el numero de muestras o simbolos usados para calcular cada punto i de la
        # la curva de SER. Esto teniendo en cuenta que:
        # * La curva de SER tiene N puntos
        # * cada punto i esta numerado de 0 a N-1
        # * el canal_BER funciona asi: a cada muestra entrante le asigna un nuevo valor de SNR
        #   asi, SNR[0],SNR[1],..., SNR[N-1], SNR[0], SNR[1], ... 
        # * La idea que se implementa mas abajo es: con cada muestra entrante se recalcula
        #   un punto de la SER asi: SER[0],SER[1],..., SER[N-1], SER[0], SER[1], ...
        #   El recalculo se repite infinitamente, ajustando cada vez mejor la curva.
 
        for i in range(0,L):
 
            # reseteo de k e incremento el contador de muestras procesadas por punto de SER
            if self.k > self.N-1:
                self.k=0
                self.count += 1  # Solo escala cada vez que todo el vector SNR ha sido procesado

            # incremento el contador de errores
            if in0[i]<>in1[i]:
                self.errores[self.k] += 1

            # calculo la SER
            self.SER[self.k]=self.errores[self.k]/self.count
            output_items[0][i]=self.SER[self.k]

            # paso al siguiente punto de SER
            self.k += 1  

        return len(output_items[0])
