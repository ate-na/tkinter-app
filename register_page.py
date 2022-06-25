from __future__ import print_function
from sys import version_info


if version_info.major == 2:
    from Tkinter import *  # noqa
    import ttk
else:
    from tkinter import *  # noqa
    import tkinter.ttk as ttk

# Import main gui object
from parent import root
# passenger panel
import buy_ticket

class Wizard(Toplevel):
    def __init__(
            self,
            width=640,
            height=480,
            cancelcommand=None,
            finishcommand=None,
            default_button="finish",
            **kwargs):

        self.selected_pane = None
        self.pane_entry_cmds = {}
        self.pane_prev_cmds = {}
        self.pane_next_cmds = {}
        self.pane_names = []
        self.panes = {}
        self.font = kwargs.get('font', ('Helvetica', '10'))
        self.cancel_command = cancelcommand
        self.finish_command = finishcommand
        self.prev_enabled = True
        self.next_enabled = True
        self.finish_enabled = True
        self.cancel_enabled = True
        self.default_button = default_button
        Toplevel.__init__(
            self,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
            relief=FLAT,
        )
        self.holder = Frame(
            self,
            borderwidth=0,
            relief=FLAT,
        )
        self.btnsfr = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
        )
        self.prevbtn = ttk.Button(
            self.btnsfr,
            text="< Prev",
            width=6,
            command=self._prevpane,
        )
        self.nextbtn = ttk.Button(
            self.btnsfr,
            text="Next >",
            width=6,
            # command=self._nextpane,
            command=self._cancel
        )
        self.fnshbtn = ttk.Button(
            self.btnsfr,
            text="Finish",
            width=6,
            command=self._finish,
        )
        self.cnclbtn = ttk.Button(
            self.btnsfr,
            text="Cancel",
            width=6,
            command=self._cancel,
        )
        self.cnclbtn.pack(side=RIGHT, fill=Y, expand=0, padx=10, pady=10)
        self.fnshbtn.pack(side=RIGHT, fill=Y, expand=0, padx=20, pady=10)
        self.nextbtn.pack(side=RIGHT, fill=Y, expand=0, padx=10, pady=10)
        self.prevbtn.pack(side=RIGHT, fill=Y, expand=0, padx=0, pady=10)

        self.holder.pack(side=TOP, fill=BOTH, expand=1)
        self.btnsfr.pack(side=TOP, fill=X, expand=0)

        self.wm_geometry("{width:d}x{height:d}".format(width=width, height=height))
        self.protocol('WM_DELETE_WINDOW', self._cancel)

        self.title("Registration")

        self.MebuBar()

    def add_pane(
            self, name, label,
            entrycommand=None,
            prevcommand=None,
            nextcommand=None):
        newpane = Frame(
            self.holder,
            borderwidth=0,
            highlightthickness=0,
            takefocus=0,
        )
        if not self.panes:
            self.selected_pane = name
            if entrycommand:
                self.after(0, entrycommand)
        self.pane_names.append(name)
        self.panes[name] = newpane
        self.pane_entry_cmds[name] = entrycommand
        self.pane_prev_cmds[name] = prevcommand
        self.pane_next_cmds[name] = nextcommand
        self._update()
        return newpane

    def del_pane(self, name):
        if name == self.selected_pane:
            idx = self.pane_names.index(name)
            panecnt = len(self.pane_names)
            if panecnt == 1:
                self.selected_pane = None
            elif idx == panecnt - 1:
                self._prevpane()
            else:
                self._nextpane()
        del self.pane_entry_cmds[name]
        del self.pane_prev_cmds[name]
        del self.pane_next_cmds[name]
        del self.panes[name]
        self.pane_names.remove(name)

    def show_pane(self, newpane):
        if newpane not in self.pane_names:
            raise ValueError("No pane with the name '{}' exists.".format(newpane))
        self.selected_pane = newpane
        entrycmd = self.pane_entry_cmds[newpane]
        if entrycmd:
            entrycmd()
        self._update()

    def set_prev_enabled(self, enable=True):
        self.prev_enabled = enable
        self._update()

    def set_next_enabled(self, enable=True):
        self.next_enabled = enable
        self._update()

    def set_finish_enabled(self, enable=True):
        self.finish_enabled = enable
        self._update()

    def set_cancel_enabled(self, enable=True):
        self.cancel_enabled = enable
        self._update()

    def set_prev_text(self, text="< Prev"):
        self.prevbtn.config(text=text)
        self._update()

    def set_next_text(self, text="Next >"):
        self.nextbtn.config(text=text)
        self._update()

    def set_finish_text(self, text="Finish"):
        self.fnshbtn.config(text=text)
        self._update()

    def set_cancel_text(self, text="Cancel"):
        self.cnclbtn.config(text=text)
        self._update()

    def set_default_button(self, btn="finish"):
        self.default_button = btn
        self._update()

    def _update(self):
        selpane = self.selected_pane
        prev_state = 'normal'
        next_state = 'normal'
        finish_state = 'normal'
        cancel_state = 'normal'
        if not self.pane_names or selpane == self.pane_names[0]:
            prev_state = 'disabled'
        if not self.prev_enabled:
            prev_state = 'disabled'
        if not self.pane_names or selpane == self.pane_names[-1]:
            next_state = 'disabled'
        if not self.next_enabled:
            next_state = 'disabled'
        if not self.finish_command or not self.finish_enabled:
            finish_state = 'disabled'
        if not self.cancel_command or not self.cancel_enabled:
            cancel_state = 'disabled'
        self.prevbtn.config(state=prev_state)
        self.nextbtn.config(state=next_state)
        # self.nextbtn.config(state='active')
        self.fnshbtn.config(state=finish_state)
        self.cnclbtn.config(state=cancel_state)
        for child in self.holder.winfo_children():
            child.forget()
        if self.pane_names:
            newpane = self.panes[selpane]
            newpane.pack(side=TOP, fill=BOTH, expand=1)
        prev_def = "active" if self.default_button == "prev" else "normal"
        next_def = "active" if self.default_button == "next" else "normal"
        finish_def = "active" if self.default_button == "finish" else "normal"
        cancel_def = "active" if self.default_button == "cancel" else "normal"
        self.prevbtn.config(default=prev_def)
        self.nextbtn.config(default=next_def)
        self.fnshbtn.config(default=finish_def)
        self.cnclbtn.config(default=cancel_def)
        self.bind('<Return>', self._invoke_default)
        self.update_idletasks()
        self.update_idletasks()

    def _invoke_default(self, event=None):
        if self.default_button == "prev":
            self.prevbtn.invoke()
        elif self.default_button == "next":
            self.nextbtn.invoke()
        elif self.default_button == "finish":
            self.fnshbtn.invoke()
        elif self.default_button == "cancel":
            self.cnclbtn.invoke()
        return "break"

    def _prevpane(self, event=None):
        oldpane = self.selected_pane
        prevcmd = self.pane_prev_cmds[oldpane]
        if prevcmd:
            prevcmd()
        if oldpane != self.selected_pane:
            return
        pos = self.pane_names.index(oldpane)
        if pos > 0:
            pos -= 1
        self.show_pane(self.pane_names[pos])

    def _nextpane(self, event=None):
        oldpane = self.selected_pane
        nextcmd = self.pane_next_cmds[oldpane]
        if nextcmd:
            nextcmd()
        if oldpane != self.selected_pane:
            return
        pos = self.pane_names.index(oldpane)
        if pos < len(self.pane_names) - 1:
            pos += 1
        self.show_pane(self.pane_names[pos])

    def _finish(self, event=None):
        self.destroy()
        if self.finish_command:
            self.finish_command()

    def _cancel(self, event=None):
        self.destroy()
        if self.cancel_command:
            self.cancel_command()


    def MebuBar(self):
        def doNothing():
            pass

        menubar = Menu(self)

        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Back", command=doNothing)
        fileMenu.add_command(label="Close", command=self._cancel)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=doNothing)
        menubar.add_cascade(label="File", menu=fileMenu)

        helpMenu = Menu(menubar, tearoff=0)
        helpMenu.add_command(label="User Manual", command=doNothing)
        helpMenu.add_command(label="About", command=doNothing)
        menubar.add_cascade(label="Help", menu=helpMenu)
        self.config(menu=menubar)


def authentication_page(root, login_flag):
    def show_password():
        e2.configure(show='')
        c1.configure(command=hide_password)

    def hide_password():
        e2.configure(show='*')
        c1.configure(command=show_password)

    def authentication():
        print("> authentication method changed.")
        username = e1.get()
        password = e2.get()

        if username == "root" and password == "toor":
            login_flag.set(True)
        else:
            login_flag.set(False)
        master.destroy()

    def cancel():
        master.destroy()
        login_flag.set(False)

    # creating main tkinter window/toplevel
    master = Toplevel(root)

    master.grab_set()

    # this will create a label widget
    l1 = Label(master, text="Username")
    l2 = Label(master, text="Password")

    # grid method to arrange labels in respective
    # rows and columns as specified
    l1.grid(row=0, column=0, sticky=W, pady=2)
    l2.grid(row=1, column=0, sticky=W, pady=2)

    # entry widgets, used to take entry from user
    e1 = Entry(master)
    e2 = Entry(master)
    e2.configure(show='*')

    # this will arrange entry widgets
    e1.grid(row=0, column=1, pady=2)
    e2.grid(row=1, column=1, pady=2)

    # checkbutton widget
    c1 = Checkbutton(master, text="Show password", command=show_password)
    c1.grid(row=2, column=0, sticky=W, columnspan=2)

    # adding image (remember image should be PNG and not JPG)
    img = PhotoImage(file=r"/home/hm/Templates/pycharm-community-2022.1/bin/pycharm.png")
    img1 = img.subsample(2, 2)

    # setting image with the help of label
    Label(master, image=img1).grid(row=0, column=2,
                                   columnspan=2, rowspan=2, padx=5, pady=5)

    # button widget
    b1 = Button(master, text="Login", command=authentication)
    b2 = Button(master, text="Cancel", command=cancel)

    # arranging button widgets
    b1.grid(row=2, column=2, sticky=E)
    b2.grid(row=2, column=3, sticky=W)

    # infinite loop which can be terminated
    # by keyboard or mouse interrupt
    mainloop()


# if __name__ == "__main__":
def panel_selection_page(root):

    #  Instantiate custom toplevel (wizard) object that is designed to hold multiple pages (frames)
    # which are related by next/prev buttons.
    wiz = Wizard(
        # width=640,
        # height=480,
        width=400,
        height=140,
        cancelcommand=lambda: print("Cancel"),
        finishcommand=lambda: print("Finish"),
    )
    # TK special variable to hold "panel type" value
    panel = StringVar()
    # TK label object
    error_label = None

    def disable_finish():
        # Disable finish button
        wiz.set_finish_enabled(False)

    def enable_finish():
        # Enable finish button
        wiz.set_finish_enabled(True)

    def enable_next(panel_type):
        # Enable next button
        wiz.nextbtn.config(state='active')
        # Delete error message (label object) if it exists
        if error_label:
            error_label.destroy()

    def panel_error(pane_name, message):
        # Handle panel type not supported values
        pane = wiz.panes[pane_name]
        # Delete error message (label object) if it exists
        nonlocal error_label
        if error_label:
            error_label.destroy()
        # Generate a new error
        error_label = Label(pane, text=message, fg="red")
        error_label.pack()

    def admin_authentication(var_type, second_arg, trigger_type):

        #  In case of successful admin authentication forwards to admin panel,
        # otherwise launches error handler.
        if login_flag.get():
            print("[+] Login Successful.")
        else:
            # Popup "panel selection" window, when failing to authenticate
            wiz.deiconify()

            print("[-] Login failed.")
            panel_error("panel", "[-] Wrong credentials, \n You don't have authorization to access admin panel.")
        print("> I got executed.")

    def admin_authentication(var_type, second_arg, trigger_type):

        #  In case of successful admin authentication forwards to admin panel,
        # otherwise launches error handler.
        if login_flag.get():
            print("[+] Login Successful.")
        else:
            # Popup "panel selection" window, when failing to authenticate
            wiz.deiconify()

            print("[-] Login failed.")
            panel_error("panel", "[-] Wrong credentials, \n You don't have authorization to access admin panel.")
        print("> I got executed.")

    def panel_launcher():

        # Forward user to selected panel
        if panel.get() == 'Admin Panel':
            # Hide "panel selection" window
            wiz.withdraw()
            # Authentication page
            authentication_page(root, login_flag)

        elif panel.get() == 'Manager Panel':
            # Hide "panel selection" window
            wiz.withdraw()
            # Authentication page
            authentication_page(root, login_flag)

        elif panel.get() == 'Passenger Panel':
            wiz.withdraw()
            buy_ticket.run()
            print(">>>> Afterwards")
        else:
            panel_error("panel", "You have to select a panel!")

    def pane1():

        # Register first layer/page of panel
        pane1 = wiz.add_pane('panel', 'Panel selection page', entrycommand=disable_finish)
        # Label
        lbl1 = Label(pane1, text="Select Panel Type to proceed registration.")
        lbl1.pack(side=TOP, fill=BOTH, expand=1)

        # Register values/options for "panel selection" dropdown menu
        panel_type = [
            "Admin Panel",
            "Manager Panel",
            "Passenger Panel",
        ]

        # Setup tk variable to hold selected panel type
        nonlocal panel
        panel.set("Click Here")

        # Create "panel selection" dropdown manu
        dropdown_panel_type = OptionMenu(pane1, panel, command=enable_next, *panel_type)
        # dropdown_functionality.pack(fill="both")
        dropdown_panel_type.pack(side=TOP, fill=X)

    # Run corresponding code to register and decorate "panel selection" page layout
    wiz.set_default_button('next')
    pane1()
    # Map "next" button to responsible function
    wiz.nextbtn.configure(command=panel_launcher)
    # Set-up tk variable trigger
    login_flag = BooleanVar()
    login_flag.trace_add('write', admin_authentication)

    root.wm_withdraw()
    root.wait_window(wiz)


def run():
    # Run Function to launch "panel page"
    panel_selection_page(root)


if __name__ == "__main__":
    # Run Function to launch "panel page"
    panel_selection_page(root)


# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap


"""

            # pane2 = wiz.add_pane('two', 'Second')
            # lbl2 = Label(pane2, text="This is the second pane.")
            # lbl2.pack(side=TOP, fill=BOTH, expand=1)


    #
    # pane3 = wiz.add_pane(
    #     'three', 'Third',
    #     entrycommand=enable_finish,
    #     prevcommand=disable_finish
    # )
    # lbl3 = Label(pane3, text="This is the third pane.")
    # lbl3.pack(side=TOP, fill=BOTH, expand=1)

    # wiz.show_pane('two')
    # wiz.del_pane('two')
    # wiz.set_prev_enabled(True)
    # wiz.set_next_enabled(True)

"""

"""
    This Modules includes the structure and information flow for all registration processes of application.
    ## `Page Functions`
    This page provides three functionality:
        1. Admin section - Process to register airport assets eg. airplanes.
        2. Managerial section - Process for registration of airlines (ie. middle companies that rent airplanes), and
         newly acquired airplanes.  
        3. User section - Process to reserve seats either individually  by passengers or in groups by tour company.
"""

