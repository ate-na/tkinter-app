from tkinter import Menu


def MebuBar(self):
        def doNothing():
            pass

        menubar = Menu(self)

        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Back", command=doNothing)
        fileMenu.add_command(label="Close")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=doNothing)
        menubar.add_cascade(label="File", menu=fileMenu)

        helpMenu = Menu(menubar, tearoff=0)
        helpMenu.add_command(label="User Manual", command=doNothing)
        helpMenu.add_command(label="About", command=doNothing)
        menubar.add_cascade(label="Help", menu=helpMenu)
        self.config(menu=menubar)
