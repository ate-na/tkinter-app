from tkinter import *
from tkinter import ttk

from parent import root
import register_page
from menu import MebuBar

import sqlite3

try:
    connection = sqlite3.connect("Airport.db")
    cursor = connection.cursor()
    # Acquire flight list from database
    sql_query = """SELECT flight.flight_id, flight.origin, flight.destination, flight.date, flight.delay, airline.name, airplane.building_company FROM flight INNER JOIN 'Airplane' ON Airplane.plane_id = flight.plane_id 
    INNER JOIN 'Airline' ON Airline.airline_id = flight.airline_id
     LIMIT 5"""
    cursor.execute(sql_query)
    flight_list = cursor.fetchall()
    # Acquire airline list from database
    sql_query = """SELECT name, registered_date FROM airline"""
    cursor.execute(sql_query)
    airline_list = cursor.fetchall()
    # Acquire airplane list from database
    sql_query = """SELECT name, model, building_company FROM airplane"""
    cursor.execute(sql_query)
    airplane_list = cursor.fetchall()
    # Acquire passenger list from database
    sql_query = """SELECT ssn, fullname , age, country_of_citizenship FROM passenger LIMIT 5"""
    cursor.execute(sql_query)
    passenger_list = cursor.fetchall()
    # Acquire tour list from database
    sql_query = """SELECT company, tour_manager_full_name, origin, destination, number_of_booking FROM tour LIMIT 5"""
    cursor.execute(sql_query)
    tour_list = cursor.fetchall()

except sqlite3.Error as error:
    print("Error while working with SQLite", error)
finally:
    if connection:
        print("Total Rows affected since the database connection was opened: ", connection.total_changes)
        connection.close()
        print("sqlite connection is closed")

tour_list.insert(0, ['company','manager','origin','destination','booking'])
passenger_list.insert(0, ['ssn','fullname','age','country'])
airplane_list.insert(0, ['name','model','company'])
airline_list.insert(0, ['name','registered'])
flight_list.insert(0, ["flight", "origin", "destination", "date", "delay", "airline", "plane"])

# root = Tk()
# tkinter variable to trigger destroy func in order to destroy the page when "register" button pressed
register_flag = BooleanVar(value=False)

def render_root(root):
    root.geometry("1080x920")

    root.title("Main Page")
    root.config(bg="#ddd")


def render_menu(root):
    def register_btn_handler(*args):
        register_flag.set(True)

    MebuBar(root)
    register_btn = Button(root,  text="Register", background='white' ,foreground='black',font=('Arial', 10 ), relief='groove', command=register_btn_handler).pack(side='top',anchor='se')

    x = Frame(root)
    x.pack(padx=20, pady=50)
    tabControl = ttk.Notebook(x)
    s = ttk.Style()
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)

    s.configure('TNotebook.Tab', font=('Roboto','10') )
    tabControl.add(tab1, text ='Airplanes')
    tabControl.add(tab2, text ='Passengers')
    tabControl.add(tab3, text ='Airlines')
    tabControl.add(tab4, text ='Tours')
    tabControl.add(tab5, text ='Flights')
    tabControl.pack(expand = 1, fill ="both")

    return tab1, tab2, tab3, tab4, tab5


def render_tab1(root, tab1):
    total_rows = len(airplane_list)
    total_columns = len(airplane_list[0])

    main_frame = Frame(tab1)
    main_frame.pack(fill='both',expand=True)

    my_canvas = Canvas(main_frame,height=1200, width=800)
    my_canvas.pack(side=RIGHT)


    my_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL,
                             command=my_canvas.xview)

    my_scrollbar.pack(side=BOTTOM, fill=Y)


    my_scrollbar2 = Scrollbar(main_frame, orient=VERTICAL,
                              command=my_canvas.yview)
    my_scrollbar2.pack(side=RIGHT, fill=Y)

    my_canvas.configure(xscrollcommand=my_scrollbar.set,
                        yscrollcommand=my_scrollbar2.set)

    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


    y = Frame(second_frame)
    y.pack()

    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(y, width=27, fg='black',
                      font=('roboto', 12, 'roman'), justify="center", borderwidth=1, relief="flat", bg="#eee")
            e.grid(row=i, column=j, sticky="nw",
                   padx=2, pady=2, ipadx=5, ipady=10)
            e.insert(END, airplane_list[i][j])



def render_tab2(root, tab2):
    total_rows = len(passenger_list)
    total_columns = len(passenger_list[0])

    main_frame = Frame(tab2)
    main_frame.pack(fill='both',expand=True)

    my_canvas = Canvas(main_frame,height=1200, width=800)
    my_canvas.pack(side=RIGHT)


    my_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL,
                             command=my_canvas.xview)

    my_scrollbar.pack(side=BOTTOM, fill=Y)


    my_scrollbar2 = Scrollbar(main_frame, orient=VERTICAL,
                              command=my_canvas.yview)
    my_scrollbar2.pack(side=RIGHT, fill=Y)

    my_canvas.configure(xscrollcommand=my_scrollbar.set,
                        yscrollcommand=my_scrollbar2.set)

    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


    y = Frame(second_frame)
    y.pack()

    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(y, width=20, fg='black',
                      font=('roboto', 12, 'roman'), justify="center", borderwidth=1, relief="flat", bg="#eee")
            e.grid(row=i, column=j, sticky="nw",
                   padx=2, pady=2, ipadx=5, ipady=10)
            e.insert(END, passenger_list[i][j])



def render_tab3(root, tab3):
    total_rows = len(airline_list)
    total_columns = len(airline_list[0])

    main_frame = Frame(tab3)
    main_frame.pack(fill='both',expand=True)

    my_canvas = Canvas(main_frame,height=1200, width=800)
    my_canvas.pack(side=RIGHT)


    my_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL,
                             command=my_canvas.xview)

    my_scrollbar.pack(side=BOTTOM, fill=Y)


    my_scrollbar2 = Scrollbar(main_frame, orient=VERTICAL,
                              command=my_canvas.yview)
    my_scrollbar2.pack(side=RIGHT, fill=Y)

    my_canvas.configure(xscrollcommand=my_scrollbar.set,
                        yscrollcommand=my_scrollbar2.set)

    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


    y = Frame(second_frame)
    y.pack()

    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(y, width=45, fg='black',
                      font=('roboto', 12, 'roman'), justify="center", borderwidth=1, relief="flat", bg="#eee")
            e.grid(row=i, column=j, sticky="nw",
                   padx=2, pady=2, ipadx=5, ipady=10)
            e.insert(END, airline_list[i][j])




def render_tab4(root, tab4):
    total_rows = len(tour_list)
    total_columns = len(tour_list[0])

    main_frame = Frame(tab4)
    main_frame.pack(fill='both',expand=True)

    my_canvas = Canvas(main_frame,height=1200, width=800)
    my_canvas.pack(side=RIGHT)


    my_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL,
                             command=my_canvas.xview)

    my_scrollbar.pack(side=BOTTOM, fill=Y)


    my_scrollbar2 = Scrollbar(main_frame, orient=VERTICAL,
                              command=my_canvas.yview)
    my_scrollbar2.pack(side=RIGHT, fill=Y)

    my_canvas.configure(xscrollcommand=my_scrollbar.set,
                        yscrollcommand=my_scrollbar2.set)

    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


    y = Frame(second_frame)
    y.pack()

    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(y, width=16, fg='black',
                      font=('roboto', 12, 'roman'), justify="center", borderwidth=1, relief="flat", bg="#eee")
            e.grid(row=i, column=j, sticky="nw",
                   padx=2, pady=2, ipadx=5, ipady=10)
            e.insert(END, tour_list[i][j])




def render_tab5(root, tab5):
    total_rows = len(flight_list)
    total_columns = len(flight_list[0])

    main_frame = Frame(tab5)
    main_frame.pack(fill='both',expand=True)

    my_canvas = Canvas(main_frame,height=1200, width=800)
    my_canvas.pack(side=RIGHT)


    my_scrollbar = Scrollbar(main_frame, orient=HORIZONTAL,
                             command=my_canvas.xview)

    my_scrollbar.pack(side=BOTTOM, fill=Y)


    my_scrollbar2 = Scrollbar(main_frame, orient=VERTICAL,
                              command=my_canvas.yview)
    my_scrollbar2.pack(side=RIGHT, fill=Y)

    my_canvas.configure(xscrollcommand=my_scrollbar.set,
                        yscrollcommand=my_scrollbar2.set)

    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


    y = Frame(second_frame)
    y.pack()

    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(y, width=20, fg='black',
                      font=('roboto', 12, 'roman'), justify="center", borderwidth=1, relief="flat", bg="#eee")
            e.grid(row=i, column=j, sticky="nw",
                   padx=2, pady=2, ipadx=5, ipady=10)
            e.insert(END, flight_list[i][j])



def run(root=root):
    register_flag.trace_add('write', register_handler)
    render_root(root)
    tab1, tab2, tab3, tab4, tab5 = render_menu(root)
    render_tab1(root, tab1)
    render_tab2(root, tab2)
    render_tab3(root, tab3)
    render_tab4(root, tab4)
    render_tab5(root, tab5)
    root.mainloop()


def register_handler(*args, root=root):
    if register_flag.get() == True:
        root.withdraw()
        register_page.run()
        root.deiconify()
