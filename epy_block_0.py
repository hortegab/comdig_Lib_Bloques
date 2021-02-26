"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """convierte de bipolar a unipolar una senal tipo char"""

    def __init__(self,):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='e_bipolar2unipolar_bb',   # will show up in GRC
            in_sig=[np.int8],
            out_sig=[np.int8]
        )
    def work(self, input_items, output_items):
        output_items[0][:] = (input_items[0]+1)/2
        return len(output_items[0])

