#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Mpsk
# Generated: Sun Mar 19 05:43:12 2017
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
from b_Eye_Diagram import b_Eye_Diagram  # grc-generated hier_block
from b_RRaised_cosine_cc import b_RRaised_cosine_cc  # grc-generated hier_block
from b_sampler_cc import b_sampler_cc  # grc-generated hier_block
from b_tunner import b_tunner  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import E3TRadio
import math
import numpy
import random
import sip


class MPSK(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Mpsk")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Mpsk")
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

        self.settings = Qt.QSettings("GNU Radio", "MPSK")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.Constelacion = Constelacion = [1.+0.j,   0.+1.j,   -1.+0.j,  0.-1.j ]
        self.M = M = len(Constelacion)
        self.samp_rate = samp_rate = 250E3*3
        self.Sps = Sps = 8
        self.Nbsym = Nbsym = int(math.log(M,2))
        self.Rs = Rs = samp_rate/Sps
        self.Np = Np = 8/Nbsym
        self.run_stop = run_stop = True
        self.rolloff = rolloff = 1.5
        self.ntaps = ntaps = Sps*16
        self.Tmax_scope = Tmax_scope = 64./Rs
        self.Rb = Rb = Rs*Nbsym
        self.Phioffset = Phioffset = 0
        self.Ndelay = Ndelay = 0
        self.Kruido = Kruido = 0.
        self.Fs_rs = Fs_rs = Rs/Np
        self.Foffset = Foffset = 0
        self.DelayOjo = DelayOjo = 0
        self.DelayDiez = DelayDiez = int(Sps/2)

        ##################################################
        # Blocks
        ##################################################
        self.pestana = Qt.QTabWidget()
        self.pestana_widget_0 = Qt.QWidget()
        self.pestana_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_0)
        self.pestana_grid_layout_0 = Qt.QGridLayout()
        self.pestana_layout_0.addLayout(self.pestana_grid_layout_0)
        self.pestana.addTab(self.pestana_widget_0, "Tx Envolvente compleja")
        self.pestana_widget_1 = Qt.QWidget()
        self.pestana_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_1)
        self.pestana_grid_layout_1 = Qt.QGridLayout()
        self.pestana_layout_1.addLayout(self.pestana_grid_layout_1)
        self.pestana.addTab(self.pestana_widget_1, "Tx Source vs Packeto to Unpacked")
        self.pestana_widget_2 = Qt.QWidget()
        self.pestana_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_2)
        self.pestana_grid_layout_2 = Qt.QGridLayout()
        self.pestana_layout_2.addLayout(self.pestana_grid_layout_2)
        self.pestana.addTab(self.pestana_widget_2, "RX Ojo versus senal en tiempo")
        self.pestana_widget_3 = Qt.QWidget()
        self.pestana_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_3)
        self.pestana_grid_layout_3 = Qt.QGridLayout()
        self.pestana_layout_3.addLayout(self.pestana_grid_layout_3)
        self.pestana.addTab(self.pestana_widget_3, "PSD")
        self.pestana_widget_4 = Qt.QWidget()
        self.pestana_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_4)
        self.pestana_grid_layout_4 = Qt.QGridLayout()
        self.pestana_layout_4.addLayout(self.pestana_grid_layout_4)
        self.pestana.addTab(self.pestana_widget_4, "Constelaciones")
        self.pestana_widget_5 = Qt.QWidget()
        self.pestana_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_5)
        self.pestana_grid_layout_5 = Qt.QGridLayout()
        self.pestana_layout_5.addLayout(self.pestana_grid_layout_5)
        self.pestana.addTab(self.pestana_widget_5, "Tx Source vs Bits")
        self.pestana_widget_6 = Qt.QWidget()
        self.pestana_layout_6 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_6)
        self.pestana_grid_layout_6 = Qt.QGridLayout()
        self.pestana_layout_6.addLayout(self.pestana_grid_layout_6)
        self.pestana.addTab(self.pestana_widget_6, "pruebaa")
        self.top_grid_layout.addWidget(self.pestana, 0,0,1,5)
        self._Phioffset_range = Range(-3.1415, 3.1415, 0.1, 0, 200)
        self._Phioffset_win = RangeWidget(self._Phioffset_range, self.set_Phioffset, "Offset ang.", "counter_slider", float)
        self.top_grid_layout.addWidget(self._Phioffset_win, 1,2,1,1)
        self._Kruido_range = Range(0, 1, 0.001, 0., 200)
        self._Kruido_win = RangeWidget(self._Kruido_range, self.set_Kruido, "Nivel del Ruido", "counter_slider", float)
        self.top_grid_layout.addWidget(self._Kruido_win, 1,3,1,1)
        self._Foffset_range = Range(0, 5, 0.01, 0, 200)
        self._Foffset_win = RangeWidget(self._Foffset_range, self.set_Foffset, "Offset frec.", "counter_slider", float)
        self.top_grid_layout.addWidget(self._Foffset_win, 1,1,1,1)
        self._DelayOjo_range = Range(0, Sps, 1, 0, 200)
        self._DelayOjo_win = RangeWidget(self._DelayOjo_range, self.set_DelayOjo, "varie aqui el retrazo de la senal para centrar el ojo", "counter_slider", int)
        self.pestana_grid_layout_2.addWidget(self._DelayOjo_win, 2,0,1,1)
        self._DelayDiez_range = Range(0, Sps-1, 1, int(Sps/2), 200)
        self._DelayDiez_win = RangeWidget(self._DelayDiez_range, self.set_DelayDiez, "Offsett muest.", "counter_slider", int)
        self.top_grid_layout.addWidget(self._DelayDiez_win, 1,4,1,1)
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 1,0,1,1)
        self.qtgui_time_sink_x_1_1_0_1 = qtgui.time_sink_c(
        	int(Tmax_scope*Fs_rs*Np), #size
        	Rs, #samp_rate
        	"Envolvente compleja en Chunk to Symbols", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_1.set_y_axis(-1.5, 1.5)
        
        self.qtgui_time_sink_x_1_1_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_1.enable_grid(False)
        self.qtgui_time_sink_x_1_1_0_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_1.disable_legend()
        
        labels = ["RRC", "Q", "RC", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_1_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_1_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_1_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_1.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_6.addWidget(self._qtgui_time_sink_x_1_1_0_1_win, 0,0,1,1)
        self.qtgui_time_sink_x_1_1_0_0_1 = qtgui.time_sink_f(
        	int(Tmax_scope*Fs_rs*8), #size
        	Rb, #samp_rate
        	"Tx Bits", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0_1.set_y_axis(-1.5, 1.5)
        
        self.qtgui_time_sink_x_1_1_0_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_1_1_0_0_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_0_1.disable_legend()
        
        labels = ["I", "Q", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_1.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_5.addWidget(self._qtgui_time_sink_x_1_1_0_0_1_win, 0,0,1,1)
        self.qtgui_time_sink_x_1_1_0_0_0_0 = qtgui.time_sink_f(
        	int(Tmax_scope*Fs_rs), #size
        	Fs_rs, #samp_rate
        	"Salida del Source", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0_0_0.set_y_axis(-128, 128)
        
        self.qtgui_time_sink_x_1_1_0_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_1_0_0_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_0_0_0.disable_legend()
        
        labels = ["I", "Q", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_5.addWidget(self._qtgui_time_sink_x_1_1_0_0_0_0_win, 1,0,1,1)
        self.qtgui_time_sink_x_1_1_0_0_0 = qtgui.time_sink_f(
        	int(Tmax_scope*Fs_rs), #size
        	Fs_rs, #samp_rate
        	"Salida del Source", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0_0.set_y_axis(-128, 128)
        
        self.qtgui_time_sink_x_1_1_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_0_0.disable_legend()
        
        labels = ["I", "Q", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_1.addWidget(self._qtgui_time_sink_x_1_1_0_0_0_win, 1,0,1,1)
        self.qtgui_time_sink_x_1_1_0_0 = qtgui.time_sink_f(
        	int(Tmax_scope*Fs_rs*Np), #size
        	Rs, #samp_rate
        	"Salida de Packed to Unpacked", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0.set_y_axis(-1, M+1)
        
        self.qtgui_time_sink_x_1_1_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_1_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_0.disable_legend()
        
        labels = ["I", "Q", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_1.addWidget(self._qtgui_time_sink_x_1_1_0_0_win, 0,0,1,1)
        self.qtgui_time_sink_x_1_1_0 = qtgui.time_sink_c(
        	int(Tmax_scope*Fs_rs*Np), #size
        	Rs, #samp_rate
        	"Envolvente compleja en Chunk to Symbols", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0.set_y_axis(-1.5, 1.5)
        
        self.qtgui_time_sink_x_1_1_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_1_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0.disable_legend()
        
        labels = ["I", "Q", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_0.addWidget(self._qtgui_time_sink_x_1_1_0_win, 1,0,1,1)
        self.qtgui_time_sink_x_1_1 = qtgui.time_sink_c(
        	int(Tmax_scope*Fs_rs*Np*Sps), #size
        	samp_rate, #samp_rate
        	"Envolvente compleja filtrada", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1.enable_grid(False)
        self.qtgui_time_sink_x_1_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_1.disable_legend()
        
        labels = ["I", "Q", "", "", "",
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_0.addWidget(self._qtgui_time_sink_x_1_1_win, 0,0,1,1)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_c(
        	Sps*64, #size
        	samp_rate, #samp_rate
        	"Rx Envolvente compleja en USRP Source", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-0.1, 0.1)
        
        self.qtgui_time_sink_x_1_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()
        
        labels = ["I", "Q", "", "", "",
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_2.addWidget(self._qtgui_time_sink_x_1_0_win, 0,0,1,2)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Rx PSD en USRP Source", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_3.addWidget(self._qtgui_freq_sink_x_0_0_win, 1,0,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Tx. PSD entrada de USRP Sink", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_3.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.qtgui_const_sink_x_0_2 = qtgui.const_sink_c(
        	1024, #size
        	"Tx - bloque Chunks to Symbols", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_2.set_update_time(0.10)
        self.qtgui_const_sink_x_0_2.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_2.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_2.enable_autoscale(False)
        self.qtgui_const_sink_x_0_2.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_2.disable_legend()
        
        labels = ["Conste", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_2_win = sip.wrapinstance(self.qtgui_const_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_4.addWidget(self._qtgui_const_sink_x_0_2_win, 0,0,1,1)
        self.qtgui_const_sink_x_0_1_0 = qtgui.const_sink_c(
        	1024, #size
        	"Rx - Muestreador", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_0.set_y_axis(-.15, .15)
        self.qtgui_const_sink_x_0_1_0.set_x_axis(-.15, .15)
        self.qtgui_const_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_1_0.disable_legend()
        
        labels = ["Conste", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_4.addWidget(self._qtgui_const_sink_x_0_1_0_win, 1,1,1,1)
        self.qtgui_const_sink_x_0_1 = qtgui.const_sink_c(
        	4000, #size
        	"Rx - Tunner versus muestreador", #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1.set_y_axis(-.1, .1)
        self.qtgui_const_sink_x_0_1.set_x_axis(-.1, .1)
        self.qtgui_const_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_1.disable_legend()
        
        labels = ["Rx Tunner", "Rx Muestreador", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [-1, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_4.addWidget(self._qtgui_const_sink_x_0_1_win, 1,0,1,1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"Tx - Filtro RC o Zehoh", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-1.5, 1.5)
        self.qtgui_const_sink_x_0.set_x_axis(-1.5, 1.5)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ["Conste", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_4.addWidget(self._qtgui_const_sink_x_0_win, 0,1,1,1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((Constelacion), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_packed_to_unpacked_xx_0_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(Nbsym, gr.GR_MSB_FIRST)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, DelayOjo)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_char_to_float_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.b_tunner_0 = b_tunner(
            NDelay=0,
            fdesv=-Foffset,
            phi=Phioffset,
            samp_rate=samp_rate,
        )
        self.b_sampler_cc_0 = b_sampler_cc(
            DelayDiez=DelayDiez,
            Sps=Sps,
        )
        self.b_RRaised_cosine_cc_0_0 = b_RRaised_cosine_cc(
            Interpolation=1,
            ntaps=ntaps,
            rolloff=rolloff,
            sps=Sps,
        )
        self.b_RRaised_cosine_cc_0 = b_RRaised_cosine_cc(
            Interpolation=Sps,
            ntaps=ntaps,
            rolloff=rolloff,
            sps=Sps,
        )
        self.b_Eye_Diagram_0 = b_Eye_Diagram(
            AlphaLineas=0.5,
            Delay=DelayOjo,
            GrosorLineas=20,
            N_eyes=2,
            Samprate=samp_rate,
            Sps=Sps,
            Title="Eye Diagramm",
            Ymax=1,
            Ymin=-1,
        )
        self.pestana_grid_layout_2.addWidget(self.b_Eye_Diagram_0, 1,0,1,2)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000)), True)
        self._Ndelay_range = Range(0, ntaps*2, 1, 0, 200)
        self._Ndelay_win = RangeWidget(self._Ndelay_range, self.set_Ndelay, "Retardo RRC", "counter_slider", int)
        self.top_grid_layout.addWidget(self._Ndelay_win, 2,0,1,1)
        self.E3TRadio_usrp2usrp1_cc_0 = E3TRadio.usrp2usrp1_cc(samp_rate, 0.8, int(Sps*random.random()), 0.04*random.random(), Kruido, 10., 2*numpy.pi*random.random(), samp_rate/(2*1.2))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_usrp2usrp1_cc_0, 0), (self.b_tunner_0, 0))    
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_char_to_float_0_0, 0))    
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_char_to_float_0_1, 0))    
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))    
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_packed_to_unpacked_xx_0_0, 0))    
        self.connect((self.b_RRaised_cosine_cc_0, 0), (self.b_RRaised_cosine_cc_0_0, 0))    
        self.connect((self.b_RRaised_cosine_cc_0_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.b_RRaised_cosine_cc_0_0, 1), (self.qtgui_time_sink_x_1_1_0_1, 0))    
        self.connect((self.b_sampler_cc_0, 0), (self.qtgui_const_sink_x_0_1, 1))    
        self.connect((self.b_sampler_cc_0, 1), (self.qtgui_const_sink_x_0_1_0, 0))    
        self.connect((self.b_tunner_0, 0), (self.b_sampler_cc_0, 0))    
        self.connect((self.b_tunner_0, 0), (self.qtgui_const_sink_x_0_1, 0))    
        self.connect((self.b_tunner_0, 0), (self.qtgui_freq_sink_x_0_0, 0))    
        self.connect((self.b_tunner_0, 0), (self.qtgui_time_sink_x_1_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_1_1_0_0, 0))    
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_1_1_0_0_0, 0))    
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_time_sink_x_1_1_0_0_1, 0))    
        self.connect((self.blocks_char_to_float_0_1, 0), (self.qtgui_time_sink_x_1_1_0_0_0_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.b_Eye_Diagram_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.b_Eye_Diagram_0, 1))    
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.blocks_packed_to_unpacked_xx_0_0, 0), (self.blocks_char_to_float_0_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.E3TRadio_usrp2usrp1_cc_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_1_1, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.b_RRaised_cosine_cc_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_const_sink_x_0_2, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_time_sink_x_1_1_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "MPSK")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.Constelacion))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Nbsym(int(math.log(self.M,2)))
        self.qtgui_time_sink_x_1_1_0_0.set_y_axis(-1, self.M+1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Rs(self.samp_rate/self.Sps)
        self.E3TRadio_usrp2usrp1_cc_0.set_BW(self.samp_rate/(2*1.2))
        self.b_Eye_Diagram_0.set_Samprate(self.samp_rate)
        self.b_tunner_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_1.set_samp_rate(self.samp_rate)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_DelayDiez(int(self.Sps/2))
        self.set_Rs(self.samp_rate/self.Sps)
        self.set_ntaps(self.Sps*16)
        self.E3TRadio_usrp2usrp1_cc_0.set_Toffset(int(self.Sps*random.random()))
        self.b_Eye_Diagram_0.set_Sps(self.Sps)
        self.b_RRaised_cosine_cc_0.set_Interpolation(self.Sps)
        self.b_RRaised_cosine_cc_0.set_sps(self.Sps)
        self.b_RRaised_cosine_cc_0_0.set_sps(self.Sps)
        self.b_sampler_cc_0.set_Sps(self.Sps)

    def get_Nbsym(self):
        return self.Nbsym

    def set_Nbsym(self, Nbsym):
        self.Nbsym = Nbsym
        self.set_Np(8/self.Nbsym)
        self.set_Rb(self.Rs*self.Nbsym)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Fs_rs(self.Rs/self.Np)
        self.set_Rb(self.Rs*self.Nbsym)
        self.set_Tmax_scope(64./self.Rs)
        self.qtgui_time_sink_x_1_1_0.set_samp_rate(self.Rs)
        self.qtgui_time_sink_x_1_1_0_0.set_samp_rate(self.Rs)
        self.qtgui_time_sink_x_1_1_0_1.set_samp_rate(self.Rs)

    def get_Np(self):
        return self.Np

    def set_Np(self, Np):
        self.Np = Np
        self.set_Fs_rs(self.Rs/self.Np)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.b_RRaised_cosine_cc_0.set_rolloff(self.rolloff)
        self.b_RRaised_cosine_cc_0_0.set_rolloff(self.rolloff)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.b_RRaised_cosine_cc_0.set_ntaps(self.ntaps)
        self.b_RRaised_cosine_cc_0_0.set_ntaps(self.ntaps)

    def get_Tmax_scope(self):
        return self.Tmax_scope

    def set_Tmax_scope(self, Tmax_scope):
        self.Tmax_scope = Tmax_scope

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.qtgui_time_sink_x_1_1_0_0_1.set_samp_rate(self.Rb)

    def get_Phioffset(self):
        return self.Phioffset

    def set_Phioffset(self, Phioffset):
        self.Phioffset = Phioffset
        self.b_tunner_0.set_phi(self.Phioffset)

    def get_Ndelay(self):
        return self.Ndelay

    def set_Ndelay(self, Ndelay):
        self.Ndelay = Ndelay

    def get_Kruido(self):
        return self.Kruido

    def set_Kruido(self, Kruido):
        self.Kruido = Kruido
        self.E3TRadio_usrp2usrp1_cc_0.set_Vruido(self.Kruido)

    def get_Fs_rs(self):
        return self.Fs_rs

    def set_Fs_rs(self, Fs_rs):
        self.Fs_rs = Fs_rs
        self.qtgui_time_sink_x_1_1_0_0_0.set_samp_rate(self.Fs_rs)
        self.qtgui_time_sink_x_1_1_0_0_0_0.set_samp_rate(self.Fs_rs)

    def get_Foffset(self):
        return self.Foffset

    def set_Foffset(self, Foffset):
        self.Foffset = Foffset
        self.b_tunner_0.set_fdesv(-self.Foffset)

    def get_DelayOjo(self):
        return self.DelayOjo

    def set_DelayOjo(self, DelayOjo):
        self.DelayOjo = DelayOjo
        self.b_Eye_Diagram_0.set_Delay(self.DelayOjo)
        self.blocks_delay_0.set_dly(self.DelayOjo)

    def get_DelayDiez(self):
        return self.DelayDiez

    def set_DelayDiez(self, DelayDiez):
        self.DelayDiez = DelayDiez
        self.b_sampler_cc_0.set_DelayDiez(self.DelayDiez)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = MPSK()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
