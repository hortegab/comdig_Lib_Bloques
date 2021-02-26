import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
#    """convierte de bipolar a unipolar una senal tipo char"""
    def __init__(self,):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='e_bipolar_to_unipolar_bb',   # will show up in GRC
            in_sig=[np.int8],
            out_sig=[np.int8]
        )

    def work(self, input_items, output_items):

        output_items[0][:] = (input_items[0]+1)/2
        return len(output_items[0])
