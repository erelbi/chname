#!/usr/bin/env python3

import gi, os, socket
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class HostnameChange(Gtk.Window):
     
  
    def __init__(self):
        self.giris = """Alan Adı Değiştirir"""
        self.grid = Gtk.Grid(column_homogeneous=True,
                         column_spacing=10,
                         row_spacing=30)
        self.hostname_string = Gtk.Entry()
        self.hostname_string.set_text(socket.gethostname())
        self.hostname_string.get_placeholder_text()
        self.giris_label = Gtk.Label.new(self.giris)
        self.hostname = ""
        self.status= True
    
        
        super(HostnameChange,self).__init__()
        self.init_ui()
        
    
    def init_ui(self):
        
        button = Gtk.Button.new_with_label("Değiştir!")
        button.connect("clicked",self.on_click_button)
        self.add(self.grid)
        self.set_border_width(15)
        
        self.grid.attach(self.giris_label,1,0,2,1)
        
        self.grid.attach(self.hostname_string,1,2,2,1)
        self.grid.attach(button,1,5,2,1)
        self.hostname_string.connect("key-release-event", self.hostname_get)
        self.set_title("Hostname Değiştir")
        self.set_default_size(400,200)
        self.connect("destroy",Gtk.main_quit)

    def hostname_get(self, widget, event):
        self.hostname = widget.get_text()
    
    def is_not_blank(self,s):
        return bool(s and not s.isspace())
    
    def on_click_button(self, button):
        try:
            if self.is_not_blank(self.hostname) and   self.hostname != socket.gethostname() :
                print('içerde {}'.format(self.hostname))
                with open('/etc/hosts') as file:
                    data = file.read()
                os.system('sed -i "/127.0.1.1/d" /etc/hosts')
                with open('/etc/hosts', 'a') as file:
                    if not data.endswith('\n'):
                        file.write('\n')
                    file.write('127.0.1.1    {}'.format(self.hostname))
                with open('/etc/hostname', 'w') as file:
                    data = file.write(self.hostname)
            else:
                self.error = "Boş veya Aynı Alan Adı"
                self.status = False 
        except Exception as err:
            self.error = err
            self.status = False 
        finally:
            self.dialog_gtk()

    def dialog_gtk(self):
        dialog = Gtk.Dialog()
        dialog.set_title("Bilgilendirici")
        dialog.set_transient_for(self)
        dialog.set_modal(True)
        dialog.add_button(button_text="OK", response_id=Gtk.ResponseType.OK) 
        dialog.connect("response", self.on_response)
        content_area = dialog.get_content_area()
        if self.status:
            label = Gtk.Label("İşlem Başarılı")
        else:
            label = Gtk.Label("İşlem Başarısız! \nHata Kodu: {}".format(self.error))
        content_area.add(label)
        dialog.show_all()
    def on_response(self, widget, response_id):
        print("response_id is", response_id)
        widget.destroy()
        win.destroy()

win = HostnameChange()
win.show_all()
Gtk.main()