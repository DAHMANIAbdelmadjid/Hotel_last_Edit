from tkinter import messagebox
from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
# from date_li import *
from CTkXYFrame import *
from  CTkMessagebox import CTkMessagebox

import StartPageAdmin_baj as sa
import StartPageAdmin_invoice_baj as sai
import StartPageAdmin_Service_baj as sas
import StartPageAdmin_use_baj as sau


set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("blue.json")  # Themes: "blue" (standard), "green", "dark-blue"

class StartPageAdmin_reservation(CTkFrame):
    def __init__(self, master):
        # self.new_appearance_mode=new_appearance_mode
        self.master=master
        CTkFrame.__init__(self, master)
        master.pack_propagate(0)
        master.geometry("856x645") 
        master.resizable(0,0)
        set_default_color_theme("dark-blue")
        self.mode="light"

        self.sidebar_frame = CTkFrame(master=self, width=176, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//mode.png"), size=(20,20))
        CTkButton(master=self.sidebar_frame, width=5,image=button_image,text="", font=("Arial Bold", 14),  anchor="w",command=self.change_appearance_mode_event).pack(anchor="sw", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//receptionniste.png"), size=(100,100))
        CTkLabel(self.sidebar_frame,text="",image=button_image).pack(anchor="center", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//hotel.png"), size=(16, 16))

        CTkButton(master=self.sidebar_frame, image=button_image, text="Rooms", font=("Arial Bold", 14), anchor="w",
                  command=self.to_Room).pack(anchor="center", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//profil.png"), size=(16, 16))

        CTkButton(master=self.sidebar_frame, text="Users", image=button_image, font=("Arial Bold", 14), anchor="w",
                  command=self.to_user).pack(anchor="center", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//service.png"), size=(20, 20))

        CTkButton(master=self.sidebar_frame, text="Servise", image=button_image, font=("Arial Bold", 14), anchor="w",
                  command=self.to_servise).pack(anchor="center", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//reservation.png"), size=(20, 20))

        CTkButton(master=self.sidebar_frame, text="Invoice", image=button_image, font=("Arial Bold", 14), anchor="w",
                  command=self.to_invoice).pack(anchor="center", padx=5, pady=(16, 0))

        button_image = CTkImage(Image.open(f"{os.path.dirname(__file__)}//facture.png"), size=(20, 20))
        CTkButton(master=self.sidebar_frame, text="Reservation", image=button_image, font=("Arial Bold", 14),
                  anchor="w", command=self.to_reservation).pack(anchor="center", padx=5, pady=(16, 0))

        self.sidebar_frame.pack(anchor="w", side="left", fill="y", expand=True)

        self.main_view = CTkFrame(master=self, corner_radius=0, width=680, height=650)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.title_frame = CTkFrame(master=self.main_view)
        self.title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        CTkLabel(master=self.title_frame, text="Services", font=("Arial Black", 25)).pack(anchor="nw", side="left")
        CTkButton(master=self.title_frame, text="New Service", font=("Arial Black", 15), command=self.open_toplevel).pack(anchor="ne", side="right")
        CTkButton(master=self.title_frame, text="Delete Service", font=("Arial Black", 15),command=self.open_toplevelDel).pack(anchor="ne", side="right",padx=12)
        CTkButton(master=self.title_frame, text="Updat Service", font=("Arial Black", 15),command=self.open_toplevelUp).pack(anchor="ne", side="right",padx=8)

        self.search_container = CTkFrame(master=self.main_view, height=50)
        self.search_container.pack(fill="x", pady=(45, 0), padx=27)
        self.entry=CTkEntry(master=self.search_container, width=305, border_width=2, placeholder_text="Search Service")
        self.entry.pack(side="left", padx=(13, 0), pady=15)
    
        CTkButton(master=self.search_container, text="Search", font=("Arial Black", 15),command=self.to_search).pack(anchor="ne",padx=13, pady=15)
        # connection=create_connection()
        self.table_data=[["Title","Service ID", "Author", "Publisher", "category"],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]
        self.table_frame = CTkXYFrame(master=self.main_view)
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data)

        self.table.edit_row(0)
        self.table.pack(expand=True)
        self.main_view.pack(side="left", fill="both", expand=True)
        self.toplevel_window = None

            
        
    def change_appearance_mode_event(self):
        new_mode=get_appearance_mode()
        if new_mode=="Light":
            # LoginPage.newMode("Dark")
            set_appearance_mode("Dark")
        else:
            set_appearance_mode("Light")
            # LoginPage.newMode("Light")

    def to_Room(self):
        self.master.switch_frame(sa.StartPageAdmin)

    def to_user(self):
        self.master.switch_frame(sau.StartPageAdmin_use)

    def to_servise(self):
        self.master.switch_frame(sas.StartPageAdmin_Servise)

    def to_invoice(self):
        self.master.switch_frame(sai.StartPageAdmin_invoice)

    def to_reservation(self):
        self.master.switch_frame(StartPageAdmin_reservation)
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow_(self,self.master)
        else:
            self.toplevel_window.focus()
    def open_toplevelUp(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowUp_(self,self.master)
        else:
            self.toplevel_window.focus()
    def open_toplevelDel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowDel_(self,self.master)
        else:
            self.toplevel_window.focus()
    def to_search(self):
        pass
    #     # connection=create_connection()
    #     self.tab=self.entry.get()
    #     self.args=search_book(connection,self.tab)
    #     self.args2=select_all_books(connection)
    #     index=[]
    #     for value in  self.args2:
    #         if not value in  self.args:
    #             index.append( self.args2.index(value))
    #     self.table.delete_rows(index)
class ToplevelWindow_(CTkToplevel):

    def __init__(self, master,*args, **kwargs):
        self.master=master
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Services")
        self.geometry("550x160")
        self.resizable(width = False ,height = False)
        self.configure(bg='#fff')
        set_appearance_mode("light")
# [["Title","Service ID", "Author", "Publisher", "category"],]
        self.title = CTkEntry(
            master=self,

            placeholder_text='Title',
            width= 200,
            height=35,
        )
        self.kentry1 = CTkEntry(
            master=self,

            placeholder_text='Author',
            width= 200,
            height=35,
        )
        self.kentry2 = CTkEntry(
            master=self,

            placeholder_text='Publisher',
            width= 200,
            height=35,
        )
        self.kentry3 = CTkEntry(
            master=self,

            placeholder_text='category',
            width= 200,
            height=35,
        )
        self.kentry4 = CTkEntry(
            master=self,

            placeholder_text='ID',
            width= 200,
            height=35,
        )

        button = CTkButton(
            master=self,
            text="New",
            font=("Arial Black", 15),
            text_color="white",
            hover= True,

            height=35,
            width= 200,
            border_width=2,
            corner_radius=4,



    command=self.Service_NEW

        )
        self.title.place(x= 18, y= 20)
        self.kentry1.place(x= 236, y= 20)
        self.kentry2.place(x= 18, y=65 )
        self.kentry3.place(x= 236, y=65 )
        self.kentry4.place(x= 18, y=110 )

        button.place(x= 236, y= 110)

    def Service_NEW(self):
        pass
            
    #     self.texit = self.title.get()
    #     self.texit1 = self.kentry1.get()
    #     self.texit2 = self.kentry2.get()
    #     self.texit3 = self.kentry3.get()
    #     self.texit4 = int(self.kentry4.get())
    #     connection=create_connection()
    #     insert_book(connection,self.texit4,self.texit,self.texit1,self.texit2,self.texit3)
    #     self.destroy()
    #     self.master.switch_frame(StartPageAdmin)


class ToplevelWindowDel_(CTkToplevel):

    def __init__(self,master ,*args, **kwargs):
        self.master=master
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Services")
        self.geometry("550x160")
        self.resizable(width = False ,height = False)
        self.configure(bg='#fff')

        set_appearance_mode("light")

        self.title = CTkEntry(
            master=self,

            placeholder_text='Service ID',
            width= 200,
            height=35,
        )


        Button = CTkButton(
            master=self,
            text="Delet",
            font=("Arial Black", 15),
            text_color="white",
            hover= True,

            height=35,
            width= 200,
            border_width=2,
            corner_radius=4,



            command=self.user_del
        )

        self.title.place(x= 18, y= 20)
        Button.place(x= 236, y= 20)
    def user_del(self):
        pass
    #     self.texit = self.title.get()
    #     connection=create_connection()
    #     delete_book(connection,self.texit)
    #     self.destroy()
    #     self.master.switch_frame(StartPageAdmin)
class ToplevelWindowUp_(CTkToplevel,):

    def __init__(self,master, *args, **kwargs):
        self.master=master
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Services")
        self.geometry("550x160")
        self.resizable(width = False ,height = False)
        self.configure(bg='#fff')
        set_appearance_mode("light")

        self.title = CTkEntry(
            master=self,

            placeholder_text='Title',
            width= 200,
            height=35,
        )
        self.kentry1 = CTkEntry(
            master=self,

            placeholder_text='Author',
            width= 200,
            height=35,
        )
        self.kentry2 = CTkEntry(
            master=self,

            placeholder_text='Publisher',
            width= 200,
            height=35,
        )
        self.kentry3 = CTkEntry(
            master=self,

            placeholder_text='category',
            width= 200,
            height=35,
        )
        self.kentry4 = CTkEntry(
            master=self,

            placeholder_text='ID',
            width= 200,
            height=35,
        )

        button = CTkButton(
            master=self,
            text="Update",
            font=("Arial Black", 15),
            text_color="white",
            hover= True,

            height=35,
            width= 200,
            border_width=2,
            corner_radius=4,
            command=self.user_NEW

        )
        self.title.place(x= 18, y= 20)
        self.kentry1.place(x= 236, y= 20)
        self.kentry2.place(x= 18, y=65 )
        self.kentry3.place(x= 236, y=65 )
        self.kentry4.place(x= 18, y=110 )

        button.place(x= 236, y= 110)

    def user_NEW(self):
            
        self.texit = self.title.get()
        self.texit1 = self.kentry1.get()
        self.texit2 = self.kentry2.get()
        self.texit3 = self.kentry3.get()
        self.texit4 = self.kentry4.get()
        # connection=create_connection()
        # update_book(connection,self.texit4,self.texit,self.texit1,self.texit2,self.texit3)
        # self.destroy()
        self.master.switch_frame(StartPageAdmin_reservation)