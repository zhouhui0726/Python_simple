#!/usr/bin/env python 
# coding=utf-8
from serial import Serial
import serial.tools.list_ports
import wx
from wx.lib.pubsub import pub
from time import sleep, ctime
from atexit import register
import threading
import codecs

import SerialUI




class SerialFrame(SerialUI.SerialFrameUI):
	def __init__(self, parent=None):
		super(SerialFrame, self).__init__(parent)
		self.Ser = Serial()
		self.serialThread = SerialThread(self.Ser)

		pub.subscribe(self.on_txtMain_update, 'update')
		self.serialPortInit()

		# fill in ports and select current setting
	def serialPortInit(self):
		preferred_index = 0
		self.m_cmbCOMX.Clear()
		self.ports = []
		for n, (portname, desc, hwid) in enumerate(sorted(serial.tools.list_ports.comports())):
			self.m_cmbCOMX.Append(u'{}'.format(portname))
			self.ports.append(portname)
			if self.Ser.name == portname:
				preferred_index = n
		self.m_cmbCOMX.SetSelection(preferred_index)
		self.Ser.port = self.ports[self.m_cmbCOMX.GetSelection()]

	def on_txtMain_update(self, msg):
		if self.m_chkHEXShow.IsChecked():
			msg = ''.join('%02X' % i for i in msg)
		self.m_txtMain.AppendText(msg)

	def on_btnSend_clicked(self, event):
		if self.Ser.is_open:
			self.Ser.write(self.m_txtInput.GetValue().encode())
		else:
			wx.MessageBox(u"串口未打开", "Error" ,wx.OK | wx.ICON_ERROR)  

	def on_btnClear_clicked(self, event):
		self.m_txtMain.Clear()

	def on_chkHEXShow_changed(self, event):
		s = self.m_txtMain.GetValue()
		if self.m_chkHEXShow.IsChecked():
			s = ''.join('%02X' % i for i in [ord(c) for c in s])
		else:
			s = ''.join([chr(int(i, 16)) for i in [s[i*2:i*2+2] for i in range(0, (len(s)/2).__int__())]])
		self.m_txtMain.Clear()
		self.m_txtMain.SetValue(s)

	def on_cmbBaud_changled(self, event):
		if self.Ser.isOpen():
			self.Ser.close()
			while self.Ser.isOpen(): pass
			self.Ser.baudrate = int(self.m_cmbBaud.GetValue())
			self.Ser.open()
		else:
			self.Ser.baudrate = int(self.m_cmbBaud.GetValue())

	def on_btnOpen_clicked(self, event):
		if not self.Ser.is_open:
			try:
				self.Ser.timeout = 1
				self.Ser.xonxoff = 0
				self.Ser.port = self.ports[self.m_cmbCOMX.GetSelection()]
				self.Ser.parity = self.m_cmbChek.GetValue()[0]
				self.Ser.baudrate = int(self.m_cmbBaud.GetValue())
				self.Ser.bytesize = int(self.m_cmbData.GetValue())
				self.Ser.stopbits = int(self.m_cmbStop.GetValue())
				self.Ser.open()
			except Exception as e:
				wx.MessageBox(u"串口错误", "Error" ,wx.OK | wx.ICON_ERROR)  
				# print('COMM Open Fail!!!', e)
				self.serialPortInit()
			else:
				self.m_btnOpen.SetLabel(u'关闭串口')
		else:
			self.Ser.close()
			while self.Ser.isOpen(): pass

			self.m_btnOpen.SetLabel(u'打开串口')

	def on_btnExtn_clicked(self, event):
		event.Skip()

class SerialThread(threading.Thread):
	def __init__(self, Ser):
		super(SerialThread, self).__init__(daemon=True)
		self.Ser = Ser
		self.start()

	def run(self):
		while True:
			if self.Ser.isOpen() and self.Ser.inWaiting():
				text = self.Ser.read(self.Ser.inWaiting())
				# text = str(text, "gbk")
				pub.sendMessage('update', msg=text.decode('gbk', 'ignore'))
			sleep(0.01)

if __name__ == '__main__':
	app = wx.App(False)
	frame = SerialFrame()
	frame.Show()
	app.MainLoop()
	
@register
def _atexit():
	print('all DONE at:', ctime())