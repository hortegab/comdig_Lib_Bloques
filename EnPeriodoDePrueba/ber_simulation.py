#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BER Simulation
# Author: Example
# Description: Adjust the noise and constellation... see what happens!
# Generated: Sun Jun  4 20:23:52 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import E3TRadio
import math
import numpy
import sip
import sys


class ber_simulation(gr.top_block, Qt.QWidget):

    def __init__(self, Constelacion=[1.+0.j,   0.+1.j,   -1.+0.j,  0.-1.j ]):
        gr.top_block.__init__(self, "BER Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BER Simulation")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ber_simulation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.Constelacion = Constelacion

        ##################################################
        # Variables
        ##################################################
        self.M = M = len(Constelacion)
        self.N = N = 9000000
        self.EbNo_dB_min = EbNo_dB_min = -4
        self.EbNo_dB_max = EbNo_dB_max = 10.
        self.Bps = Bps = int(math.log(M,2))
        self.samp_rate = samp_rate = N
        self.run_stop = run_stop = True
        self.Noise_puntos = Noise_puntos = 20
        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((Constelacion), (), 4, 1).base()
        self.Anoise_min = Anoise_min = 1.0 / math.sqrt(2.0 * Bps* 10**(EbNo_dB_max/10.))
        self.Anoise_max = Anoise_max = 1.0 / math.sqrt(2.0 * Bps* 10**(EbNo_dB_min/10.))

        ##################################################
        # Blocks
        ##################################################
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0,0,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	Noise_puntos*2*N, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(Anoise_min, Anoise_max)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_vector_source_x_0 = blocks.vector_source_f(numpy.linspace(Anoise_min,Anoise_max,Noise_puntos), False, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.E3TRadio_Zero_Order_Hold_0 = E3TRadio.Zero_Order_Hold(N)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.E3TRadio_Zero_Order_Hold_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ber_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.E3TRadio_Zero_Order_Hold_0.set_retardo(self.N)
        self.set_samp_rate(self.N)

    def get_EbNo_dB_min(self):
        return self.EbNo_dB_min

    def set_EbNo_dB_min(self, EbNo_dB_min):
        self.EbNo_dB_min = EbNo_dB_min
        self.set_Anoise_max(1.0 / math.sqrt(2.0 * self.Bps* 10**(self.EbNo_dB_min/10.)))

    def get_EbNo_dB_max(self):
        return self.EbNo_dB_max

    def set_EbNo_dB_max(self, EbNo_dB_max):
        self.EbNo_dB_max = EbNo_dB_max
        self.set_Anoise_min(1.0 / math.sqrt(2.0 * self.Bps* 10**(self.EbNo_dB_max/10.)))

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Anoise_max(1.0 / math.sqrt(2.0 * self.Bps* 10**(self.EbNo_dB_min/10.)))
        self.set_Anoise_min(1.0 / math.sqrt(2.0 * self.Bps* 10**(self.EbNo_dB_max/10.)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_Noise_puntos(self):
        return self.Noise_puntos

    def set_Noise_puntos(self, Noise_puntos):
        self.Noise_puntos = Noise_puntos
        self.blocks_vector_source_x_0.set_data(numpy.linspace(self.Anoise_min,self.Anoise_max,self.Noise_puntos), [])

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_Anoise_min(self):
        return self.Anoise_min

    def set_Anoise_min(self, Anoise_min):
        self.Anoise_min = Anoise_min
        self.qtgui_time_sink_x_0.set_y_axis(self.Anoise_min, self.Anoise_max)
        self.blocks_vector_source_x_0.set_data(numpy.linspace(self.Anoise_min,self.Anoise_max,self.Noise_puntos), [])

    def get_Anoise_max(self):
        return self.Anoise_max

    def set_Anoise_max(self, Anoise_max):
        self.Anoise_max = Anoise_max
        self.qtgui_time_sink_x_0.set_y_axis(self.Anoise_min, self.Anoise_max)
        self.blocks_vector_source_x_0.set_data(numpy.linspace(self.Anoise_min,self.Anoise_max,self.Noise_puntos), [])


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    return parser


def main(top_block_cls=ber_simulation, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
