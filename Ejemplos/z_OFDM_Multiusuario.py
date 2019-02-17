#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Z Ofdm Multiusuario
# Generated: Sat May 12 07:43:53 2018
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_meter_power_cc import b_meter_power_cc  # grc-generated hier_block
from gnuradio import analog
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import cmath
import numpy
import sip


class z_OFDM_Multiusuario(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Z Ofdm Multiusuario")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Z Ofdm Multiusuario")
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

        self.settings = Qt.QSettings("GNU Radio", "z_OFDM_Multiusuario")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 4000
        self.run_stop = run_stop = True
        self.f = f = 1000
        self.Rs = Rs = samp_rate
        self.N = N = 32
        self.Constelacion4 = Constelacion4 = digital.constellation_16qam().points()

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
        self.qtgui_number_sink_0_2 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_2.set_update_time(0.10)
        self.qtgui_number_sink_0_2.set_title("Pontencia dB")
        
        labels = ["Pr", "", "", "", "",
                  "", "", "", "", ""]
        units = ["dB", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_2.set_min(i, -50)
            self.qtgui_number_sink_0_2.set_max(i, 20)
            self.qtgui_number_sink_0_2.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_2.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_2.set_label(i, labels[i])
            self.qtgui_number_sink_0_2.set_unit(i, units[i])
            self.qtgui_number_sink_0_2.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_2.enable_autoscale(False)
        self._qtgui_number_sink_0_2_win = sip.wrapinstance(self.qtgui_number_sink_0_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_2_win, 1,0)
        self.qtgui_number_sink_0_1_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_1_0.set_update_time(0.10)
        self.qtgui_number_sink_0_1_0.set_title("Pontencia")
        
        labels = ["Pr", "", "", "", "",
                  "", "", "", "", ""]
        units = ["Watts", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_1_0.set_min(i, -50)
            self.qtgui_number_sink_0_1_0.set_max(i, 20)
            self.qtgui_number_sink_0_1_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_1_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_1_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_1_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_1_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_1_0.enable_autoscale(False)
        self._qtgui_number_sink_0_1_0_win = sip.wrapinstance(self.qtgui_number_sink_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_1_0_win, 2,0)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0.set_title("Valor RMS")
        
        labels = ["VRMS", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0.set_min(i, -50)
            self.qtgui_number_sink_0_0_0.set_max(i, 20)
            self.qtgui_number_sink_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_win, 0,0)
        self._f_range = Range(0, samp_rate*4, samp_rate/N, 1000, 200)
        self._f_win = RangeWidget(self._f_range, self.set_f, "frecuencia", "counter_slider", float)
        self.top_grid_layout.addWidget(self._f_win, 1,0,1,1)
        self.b_meter_power_cc_0 = b_meter_power_cc(
            G_prom=0.0001,
        )
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.b_meter_power_cc_0, 0))    
        self.connect((self.b_meter_power_cc_0, 2), (self.qtgui_number_sink_0_0_0, 0))    
        self.connect((self.b_meter_power_cc_0, 0), (self.qtgui_number_sink_0_1_0, 0))    
        self.connect((self.b_meter_power_cc_0, 1), (self.qtgui_number_sink_0_2, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "z_OFDM_Multiusuario")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Rs(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

    def get_Constelacion4(self):
        return self.Constelacion4

    def set_Constelacion4(self, Constelacion4):
        self.Constelacion4 = Constelacion4


def main(top_block_cls=z_OFDM_Multiusuario, options=None):

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
