#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat May 12 04:26:24 2018
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
from b_selectorN import b_selectorN  # grc-generated hier_block
from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.f1 = f1 = 1000
        self.samp_rate = samp_rate = 32000
        self.f7 = f7 = 7*f1
        self.f6 = f6 = 6*f1
        self.f5 = f5 = 5*f1
        self.f4 = f4 = 4*f1
        self.f3 = f3 = 3*f1
        self.f2 = f2 = 2*f1
        self.f0 = f0 = 0
        self.a7 = a7 = 8
        self.a6 = a6 = 7
        self.a5 = a5 = 6
        self.a4 = a4 = 5
        self.a3 = a3 = 4
        self.a2 = a2 = 3
        self.a1 = a1 = 2
        self.a0 = a0 = 1

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-8.2, 8.2)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
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
        
        for i in xrange(2*4):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 1,0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-8.2, 8.2)
        
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
        
        for i in xrange(2*4):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 0,0)
        self.b_selectorN_0 = b_selectorN(
            o0=2,
            o1=1,
            o2=0,
            o3=3,
            o4=4,
            o5=5,
            o6=6,
            o7=7,
        )
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f5, a5, 0)
        self.analog_sig_source_x_0_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f6, a6, 0)
        self.analog_sig_source_x_0_0_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f7, a7, 0)
        self.analog_sig_source_x_0_0_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f4, a4, 0)
        self.analog_sig_source_x_0_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f3, a3, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f2, a2, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f1, a1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f0, a0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.b_selectorN_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.b_selectorN_0, 1))    
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.b_selectorN_0, 2))    
        self.connect((self.analog_sig_source_x_0_0_0_0, 0), (self.b_selectorN_0, 3))    
        self.connect((self.analog_sig_source_x_0_0_0_0_0, 0), (self.b_selectorN_0, 4))    
        self.connect((self.analog_sig_source_x_0_0_0_1, 0), (self.b_selectorN_0, 7))    
        self.connect((self.analog_sig_source_x_0_0_1, 0), (self.b_selectorN_0, 6))    
        self.connect((self.analog_sig_source_x_0_1, 0), (self.b_selectorN_0, 5))    
        self.connect((self.b_selectorN_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.b_selectorN_0, 1), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.b_selectorN_0, 2), (self.qtgui_time_sink_x_0, 2))    
        self.connect((self.b_selectorN_0, 3), (self.qtgui_time_sink_x_0, 3))    
        self.connect((self.b_selectorN_0, 4), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.b_selectorN_0, 5), (self.qtgui_time_sink_x_0_0, 1))    
        self.connect((self.b_selectorN_0, 6), (self.qtgui_time_sink_x_0_0, 2))    
        self.connect((self.b_selectorN_0, 7), (self.qtgui_time_sink_x_0_0, 3))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_f1(self):
        return self.f1

    def set_f1(self, f1):
        self.f1 = f1
        self.set_f2(2*self.f1)
        self.set_f3(3*self.f1)
        self.set_f4(4*self.f1)
        self.set_f5(5*self.f1)
        self.set_f6(6*self.f1)
        self.set_f7(7*self.f1)
        self.analog_sig_source_x_0_0.set_frequency(self.f1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)

    def get_f7(self):
        return self.f7

    def set_f7(self, f7):
        self.f7 = f7
        self.analog_sig_source_x_0_0_0_1.set_frequency(self.f7)

    def get_f6(self):
        return self.f6

    def set_f6(self, f6):
        self.f6 = f6
        self.analog_sig_source_x_0_0_1.set_frequency(self.f6)

    def get_f5(self):
        return self.f5

    def set_f5(self, f5):
        self.f5 = f5
        self.analog_sig_source_x_0_1.set_frequency(self.f5)

    def get_f4(self):
        return self.f4

    def set_f4(self, f4):
        self.f4 = f4
        self.analog_sig_source_x_0_0_0_0_0.set_frequency(self.f4)

    def get_f3(self):
        return self.f3

    def set_f3(self, f3):
        self.f3 = f3
        self.analog_sig_source_x_0_0_0_0.set_frequency(self.f3)

    def get_f2(self):
        return self.f2

    def set_f2(self, f2):
        self.f2 = f2
        self.analog_sig_source_x_0_0_0.set_frequency(self.f2)

    def get_f0(self):
        return self.f0

    def set_f0(self, f0):
        self.f0 = f0
        self.analog_sig_source_x_0.set_frequency(self.f0)

    def get_a7(self):
        return self.a7

    def set_a7(self, a7):
        self.a7 = a7
        self.analog_sig_source_x_0_0_0_1.set_amplitude(self.a7)

    def get_a6(self):
        return self.a6

    def set_a6(self, a6):
        self.a6 = a6
        self.analog_sig_source_x_0_0_1.set_amplitude(self.a6)

    def get_a5(self):
        return self.a5

    def set_a5(self, a5):
        self.a5 = a5
        self.analog_sig_source_x_0_1.set_amplitude(self.a5)

    def get_a4(self):
        return self.a4

    def set_a4(self, a4):
        self.a4 = a4
        self.analog_sig_source_x_0_0_0_0_0.set_amplitude(self.a4)

    def get_a3(self):
        return self.a3

    def set_a3(self, a3):
        self.a3 = a3
        self.analog_sig_source_x_0_0_0_0.set_amplitude(self.a3)

    def get_a2(self):
        return self.a2

    def set_a2(self, a2):
        self.a2 = a2
        self.analog_sig_source_x_0_0_0.set_amplitude(self.a2)

    def get_a1(self):
        return self.a1

    def set_a1(self, a1):
        self.a1 = a1
        self.analog_sig_source_x_0_0.set_amplitude(self.a1)

    def get_a0(self):
        return self.a0

    def set_a0(self, a0):
        self.a0 = a0
        self.analog_sig_source_x_0.set_amplitude(self.a0)


def main(top_block_cls=top_block, options=None):

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
