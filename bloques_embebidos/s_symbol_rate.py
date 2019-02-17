import numpy as np
from gnuradio import gr

###########################################################################
##       lo de arriba era puro encabezado. Aqui comienza la clase        ##
###########################################################################
class blk(gr.sync_block):
import numpy as np
from gnuradio import gr

###########################################################################
##       lo de arriba era puro encabezado. Aqui comienza la clase        ##
###########################################################################
class mi_bloque_embebido(gr.sync_block):

    """
Este es el codigo embebido del bloque e_Symbol Rate
Hecho por: Homero Ortega Boada
Profesor de la Universidad Industrial de Santander

Funcionalidad:
Las entradas: son dos, para la senal transmitida y la recibida.

Salidas: 
out0: Entrega el numero de simbolos tenidos en cuenta
out1: Entrega el numero de errores identificado
out2: Entrega la SER (Symbol Error Ratio).
  
Es importante tener en cuenta que: 
- si en vez de tener simbolos a la entrada, se tienen bits, entonces lo que se calcula es la BER (Bit Error Ratio)

Parametros usados:
Nbmax: es el maximo numero de bits transmitidos a tener en cuenta para el calculo. Este numero depende de la resolucion que se pretenda alcanzar en la medicion. Si por ejemplo tu deseas que la BER llegue a valores tan pequenos como 1e-6, entonces debera elegir Nbmax=1e+6
Error Max: Es el numero maximo de errores a tener en cuenta. Este numero depende del grado de exactitud que se desee lograr, del grado de estabilidad que alcanza el calculo de la BER o la SER. Un buen valor puede ser Errors=100 o mas. La idea es que el sistema dejara de realizar calculos cuando el contador de simbolos procesados alcanza Nbmax o cuando el contador de simbolos erroneos alcanza Error_max
"""

    def __init__(self, Sym_max=1e6,Errors_max=1e4):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='e_Symbol Rate',
            in_sig=[np.int8,np.int8],
            out_sig=[np.float32,np.float32,np.float32]
        )
        self.Sym_max = Sym_max
        self.Errors_max=Errors_max
        self.errores = 0.
        self.count=0.
        self.BER=1.

    ###########################################################################
    ##  lo de arriba era puro iniciacion. Aqui comienza el verdadero codigo  ##
    ###########################################################################
    def work(self, input_items, output_items):
        in0=input_items[0]
        in1=input_items[1]
        out0=output_items[0]
        out1=output_items[1]
        out2=output_items[2]
        if self.errores<self.Errors_max:
            if self.count < self.Sym_max:
                self.count += len(in0)
                self.errores += np.count_nonzero(in0-in1)
                self.BER=self.errores/self.count
        out2[:]=self.BER
        out1[:]=self.errores
        out0[:]=self.count
        return len(output_items[0])
    def __init__(self, Sym_max=1e6,Errors_max=1e4):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='e_Symbol Rate',
            in_sig=[np.int8,np.int8],
            out_sig=[np.float32,np.float32,np.float32]
        )
        self.Sym_max = Sym_max
        self.Errors_max=Errors_max
        self.errores = 0.
        self.count=0.
        self.BER=1.

    ###########################################################################
    ##  lo de arriba era puro iniciacion. Aqui comienza el verdadero codigo  ##
    ###########################################################################
    def work(self, input_items, output_items):
        in0=input_items[0]
        in1=input_items[1]
        out0=output_items[0]
        out1=output_items[1]
        out2=output_items[2]
        if self.errores<self.Errors_max:
            if self.count < self.Sym_max:
                self.count += len(in0)
                self.errores += np.count_nonzero(in0-in1)
                self.BER=self.errores/self.count
        out2[:]=self.BER
        out1[:]=self.errores
        out0[:]=self.count
        return len(output_items[0])
