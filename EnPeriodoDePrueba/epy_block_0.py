"""
Embedded Python Blocks:

aEach this file is saved, GRC will instantiate the first class it finds to get
ports and parameters of your block. The arguments to __init__  will be the
parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, factor=1000):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        self.factor = factor
        self.errores = 0.
        self.count=0.


    def work(self, input_items, output_items):
        in0=input_items[0]
        out=output_items[0]
        count += len(in0)
        s_tx=numpy.real(in0) # senal transmitida
        s_rx=numpy.imag(in0) # senal recibida con errores
        errores += numpy.sum(abs(xr-xi))
        BER=errores/count
        out[:]=BER+errores*1j
        return len(output_items[0])
