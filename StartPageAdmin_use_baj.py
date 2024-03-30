from customtkinter import *
from CTkTable import CTkTable
from PIL import Image  #

import date_li_user
from date_li_user import *
from CTkXYFrame import *
import os
import StartPageAdmin_baj as sa
import StartPageAdmin_invoice_baj as sai
import StartPageAdmin_reservation_baj as sar
import StartPageAdmin_Service_baj as sas

class StartPageAdmin_use(CTkFrame):
    def __init__(self, master):
        self.master = master
        CTkFrame.__init__(self, master)
        master.pack_propagate(0)
        master.geometry("856x645")
        master.resizable(0, 0)

        self.sidebar_frame = CTkFrame(master=self, width=176, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//cogwheel.png"), size=(20, 20))
        CTkButton(master=self.sidebar_frame, width=5, image=button_image, text="", font=("Arial Bold", 14), anchor="w",
                  command=self.open_toplevelSett).pack(anchor="sw", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//receptionniste.png"), size=(100, 100))
        CTkLabel(self.sidebar_frame, text="", image=button_image).pack(anchor="center", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//hotel.png"), size=(16, 16))

        CTkButton(master=self.sidebar_frame, image=button_image, text="Rooms", font=("Arial Bold", 14), anchor="w",
                  command=self.to_Room).pack(anchor="center", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//profil.png"), size=(16, 16))

        CTkButton(master=self.sidebar_frame, text="Clients", image=button_image, font=("Arial Bold", 14), anchor="w",
                  command=self.to_user).pack(anchor="center", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//service.png"), size=(20, 20))

        CTkButton(master=self.sidebar_frame, text="Services", image=button_image, font=("Arial Bold", 14), anchor="w",
                  command=self.to_servise).pack(anchor="center", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//reservation.png"), size=(20, 20))

        CTkButton(master=self.sidebar_frame, text="Consumptions", image=button_image, font=("Arial Bold", 14), anchor="w",
                  command=self.to_invoice).pack(anchor="center", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//facture.png"), size=(20, 20))
        CTkButton(master=self.sidebar_frame, text="Reservations", image=button_image, font=("Arial Bold", 14),
                  anchor="w", command=self.to_reservation).pack(anchor="center", padx=5, pady=(16, 0))

        self.sidebar_frame.pack(anchor="w", side="left", fill="y", expand=True)

        self.main_view = CTkFrame(master=self, corner_radius=0, width=680, height=650)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.title_frame = CTkFrame(master=self.main_view)
        self.title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        CTkLabel(master=self.title_frame, text="Clients", font=("Arial Black", 25)).pack(anchor="nw", side="left")
        CTkButton(master=self.title_frame, text="New", font=("Arial Black", 15), command=self.open_toplevel).pack(
            anchor="ne", side="right")
        CTkButton(master=self.title_frame, text="Delete", font=("Arial Black", 15),
                  command=self.open_toplevelDel).pack(anchor="ne", side="right", padx=12)
        CTkButton(master=self.title_frame, text="Update", font=("Arial Black", 15),
                  command=self.open_toplevelUp).pack(anchor="ne", side="right", padx=8)
        self.search_container = CTkFrame(master=self.main_view, height=50)
        self.search_container.pack(fill="x", pady=(45, 0), padx=27)
        self.entry = CTkEntry(master=self.search_container, width=305, border_width=2, placeholder_text="Search for a user")
        self.entry.pack(side="left", padx=(13, 0), pady=15)
        self.text = self.entry.get()
        print(self.text)
        CTkButton(master=self.search_container, text="Search", font=("Arial Black", 15), command=self.to_search).pack(
            anchor="ne", padx=13, pady=15)
        connection=create_connection()
        self.table_data = date_li_user.select_all_clients(connection)
        self.table_frame = CTkXYFrame(master=self.main_view)
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame,
                              values=self.table_data, )  # header_color="#765827", hover_color="#B4B4B4"

        self.table.edit_row(0)
        self.table.pack(expand=True)
        self.main_view.pack(side="left", fill="both", expand=True)
        self.toplevel_window = None

    def change_appearance_mode_event(self):
        global new_mode
        if new_mode == "Light":
            new_mode = "Dark"
            set_appearance_mode(f"{new_mode}")
        else:
            new_mode = "Light"
            set_appearance_mode(f"{new_mode}")

    def to_Room(self):
        self.master.switch_frame(sa.StartPageAdmin)

    def to_user(self):
        self.master.switch_frame(StartPageAdmin_use)

    def to_servise(self):
        self.master.switch_frame(sas.StartPageAdmin_Servise)

    def to_invoice(self):
        self.master.switch_frame(sai.StartPageAdmin_invoice)

    def to_reservation(self):
        self.master.switch_frame(sar.StartPageAdmin_reservation)

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self, self.master)
        else:
            self.toplevel_window.focus()

    def open_toplevelUp(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowUp(self, self.master)
        else:
            self.toplevel_window.focus()

    def open_toplevelDel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowDel(self, self.master)
        else:
            self.toplevel_window.focus()

    def to_search(self):
        pass
        connection=create_connection()
        self.tab=self.entry.get()
        self.args=search_client(connection,self.tab)
        self.args2=select_all_clients(connection)
        index=[]
        for value in  self.args2:
            if not value in  self.args:
               index.append( self.args2.index(value))
        self.table.delete_rows(index)

    def open_toplevelSett(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelSettings(self, self.master)
        else:
            self.toplevel_window.focus()


class ToplevelSettings(CTkToplevel):

    def __init__(self, frame, master, *args, **kwargs):
        self.master = master
        super().__init__(*args, **kwargs)
        self.title("Client")
        self.geometry("200x160")
        self.resizable(width=False, height=False)
        self.configure(bg='#fff')
        self.appearance_mode_optionemenu = CTkOptionMenu(self,
                                                         values=["Light", "Dark", "System"],
                                                         command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.pack(side="top", padx=20, pady=10)
        self.scaling_optionemenu = CTkOptionMenu(self,
                                                 values=["100%", "110%", "120%", "130%", "140%"],
                                                 command=self.change_scaling_event)
        self.scaling_optionemenu.pack(side="top", padx=20, pady=10)

        self.color = CTkOptionMenu(self,
                                   values=["blue", "green", "dark-blue"],
                                   command=self.change_color_event)
        self.color.pack(side="top", padx=20, pady=10)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        set_widget_scaling(new_scaling_float)

    def change_color_event(self, new_color: str):
        set_default_color_theme(f"{new_color}")
        self.destroy()
        self.master.switch_frame(StartPageAdmin_use)


class ToplevelWindowDel(CTkToplevel):

    def __init__(self, master, *args, **kwargs):
        self.master = master

        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Client")
        self.geometry("550x160")
        self.resizable(width=False, height=False)
        self.configure(bg='#fff')


        self.title = CTkEntry(
            master=self,

            placeholder_text='User ID',
            width=200,
            height=35,
        )

        Button = CTkButton(
            master=self,
            text="Delete",
            font=("Arial Black", 15),
            text_color="white",
            hover=True,

            height=35,
            width=200,
            border_width=2,
            corner_radius=4,

            command=self.user_del
        )

        self.title.place(x=18, y=20)

        Button.place(x=236, y=20)

    def user_del(self):
        pass
        self.texit = self.title.get()
        connection=create_connection()
        delete_user(connection,self.texit)
        self.destroy()
        self.master.switch_frame(StartPageAdmin_use)


class ToplevelWindowUp(CTkToplevel):

    def __init__(self, master, *args, **kwargs):
        self.master = master
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Client")
        self.geometry("550x160")
        self.resizable(width=False, height=False)
        self.configure(bg='#fff')

        self.title = CTkEntry(
            master=self,

            placeholder_text='Client ID',
            width=200,
            height=35,
        )
        self.kentry1 = CTkEntry(
            master=self,

            placeholder_text='Identification number',
            width=200,
            height=35,
        )
        self.kentry2 = CTkEntry(
            master=self,

            placeholder_text='Name',
            width=200,
            height=35,
        )
        self.kentry3 = CTkEntry(
            master=self,

            placeholder_text='Phone number',
            width=200,
            height=35,
        )
        #self.kentry4 = CTkEntry(
        #    master=self,

        #    placeholder_text='ID',
        #    width=200,
        #    height=35,
        #)
        # exitPath = CTkEntry(
        #     master=self,
        #     border_color=765827",
        #     placeholder_text='File exit path',
        #     width= 200,
        #     height=35,
        # )

        button = CTkButton(
            master=self,
            text="Update",
            font=("Arial Black", 15),
            text_color="white",
            hover=True,

            height=35,
            width=200,
            border_width=2,
            corner_radius=4,

            command=self.user_NEW

        )
        self.title.place(x=18, y=20)
        self.kentry1.place(x=236, y=20)
        self.kentry2.place(x=18, y=65)
        self.kentry3.place(x=236, y=65)
        #self.kentry4.place(x=18, y=110)

        button.place(x=236, y=110)

    def user_NEW(self):
        pass

        self.texit = self.title.get()
        self.texit1 = self.kentry1.get()
        self.texit2 = self.kentry2.get()
        self.texit3 = self.kentry3.get()
        #self.texit4 = int(self.kentry4.get())
        connection=create_connection()
        update_client(connection,self.texit,self.texit1,self.texit2,self.texit3)
        self.destroy()
        self.master.switch_frame(StartPageAdmin_use)


class ToplevelWindow(CTkToplevel):

    def __init__(self, master, *args, **kwargs):
        self.master = master
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Client")
        self.geometry("550x160")
        self.resizable(width=False, height=False)
        self.configure(bg='#fff')


        self.title = CTkEntry(
            master=self,
            placeholder_text='Identification number',
            width=200,
            height=35,
        )
        self.kentry1 = CTkEntry(
            master=self,

            placeholder_text='Name',
            width=200,
            height=35,
        )
        self.kentry2 = CTkEntry(
            master=self,
            placeholder_text='Phone Number',
            width=200,
            height=35,
        )

        button = CTkButton(
            master=self,
            text="Add",
            font=("Arial Black", 15),
            text_color="white",
            hover=True,

            height=35,
            width=200,
            border_width=2,
            corner_radius=4,

            command=self.user_NEW

        )
        self.title.place(x=18, y=20)
        self.kentry1.place(x=236, y=20)
        self.kentry2.place(x=18, y=65)

        button.place(x=236, y=110)

    def user_NEW(self):
        pass

        self.texit = self.title.get()
        self.texit1 = self.kentry1.get()
        self.texit2 = self.kentry2.get()
        # self.texit3 = self.kentry3.get()
        #self.texit4 = int(self.kentry4.get())
        connection=create_connection()
        insert_client(connection,self.texit,self.texit1,self.texit2)
        self.destroy()
        self.master.switch_frame(StartPageAdmin_use)
