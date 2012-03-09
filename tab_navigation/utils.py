from gi.repository import Gtk, Gedit, Gdk, GObject

TAB_KEY = "Tab"
CTRL_SHIFT_TAB_KEY = "ISO_Left_Tab"

def ctrl_tab_key_pressed(event, key):
    state = event.state
    ctrl_mask = Gdk.ModifierType.CONTROL_MASK
    if state & ctrl_mask and key == TAB_KEY:
        return True
    else:
        return False
        
def ctrl_shift_tab_key_pressed(event, key):
    state = event.state
    ctrl_mask = Gdk.ModifierType.CONTROL_MASK
    if state & ctrl_mask and key == CTRL_SHIFT_TAB_KEY:
        return True
    else:
        return False
        
def set_up_variables(window, event):
    key = Gdk.keyval_name(event.keyval)
    active_tab = window.get_active_tab()
    list_all_tabs = active_tab.get_parent().get_children()
    return key, active_tab, list_all_tabs

def get_tab_position(list_all_tabs, active_tab):
    for i in xrange(len(list_all_tabs)):
        if list_all_tabs[i] == active_tab:
            tab_position = i
    return tab_position
        
def go_to_previous_tab(window, list_all_tabs, tab_position):
    active_tab = list_all_tabs[tab_position - 1]
    window.set_active_tab(active_tab)
    
def go_to_next_tab(window, list_all_tabs, tab_position):
    if is_last_tab(list_all_tabs, tab_position):
        active_tab = list_all_tabs[0]
    else:
        active_tab = list_all_tabs[tab_position + 1]
    window.set_active_tab(active_tab)

def is_last_tab(list_all_tabs, tab_position):
    if tab_position == len(list_all_tabs) - 1:
        return True
