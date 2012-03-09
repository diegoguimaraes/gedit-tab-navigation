# -*- coding: utf-8 -*-
#
# Gedit 3 plugin to make easy navigate through opened tabs 
# using <Cttrl>Tab or <Shift><Ctrl>Tab.
#
# Copyright (C) 2012 Diego Guimaraes To <diegobr.sistemas@gmail.com>
# https://github.com/diegoguimaraes/gedit-tab-navigation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, Gedit, GObject
from utils import *

class TabNavigation(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "TabNavigation"
    window = GObject.property(type=Gedit.Window)
    
    def __init__(self):
        GObject.Object.__init__(self)
        
    def do_activate(self):
        handlers = []
        handler_id = self.window.connect('key-press-event', self.on_ctrl_tab_key_pressed_event)
        handler_id = self.window.connect('key-press-event', self.on_ctrl_shift_tab_key_pressed_event)
        handlers.append(handler_id)
        self.window.set_data(self.__gtype_name__+"Handlers", handlers)

    def on_ctrl_tab_key_pressed_event(self, window, event):
        key, active_tab, list_all_tabs = set_up_variables(window, event)

        if ctrl_tab_key_pressed(event, key):
            tab_position = get_tab_position(list_all_tabs, active_tab)
            go_to_next_tab(window, list_all_tabs, tab_position)
            return True
            
    def on_ctrl_shift_tab_key_pressed_event(self, window, event):
        key, active_tab, list_all_tabs = set_up_variables(window, event)

        if ctrl_shift_tab_key_pressed(event, key):
            tab_position = get_tab_position(list_all_tabs, active_tab)
            go_to_previous_tab(window, list_all_tabs, tab_position)
            return True
    
    def do_deactivate(self):
        handlers = self.window.get_data(self.__gtype_name__+"Handlers")
        for handler_id in handlers:
            self.window.disconnect(handler_id)
    
    def do_update_state(self):
        pass
