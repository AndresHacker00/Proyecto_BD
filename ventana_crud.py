from tkinter import*

class Ventana (Frame):

    def __init__(self, master = None):
        super().__init__(master, width = 700, height = 260)
        self.master = master
        self.pack()
        self.create_widgets()

    def fNuevo(self):
        pass 

    def fModificar(self):
        pass

    def fEliminar(self):
        pass 

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x =  0, y = 0, width = 93, height = 259)    

        self.btnNuevo = Button(frame1, text= "Nuevo", command = self.fNuevo, bg ="blue", fg="black")
        self.btnNuevo.place(x = 5, y = 50, width = 80, height = 30)

        frame2 = Frame(self, bg = "#d3dde3" )
        frame2.place(x = 95, y=25, width = 150, height = 259)

        #Titulos & Textboxes

        lbl1 = Label(frame2, text = "idPedidos" )
        lbl1.place(x = 3, y = 5)
        self.txtidPedidos = Entry(frame2)
        self.txtidPedidos.place(x = 3, y = 25, width = 50, height = 20)

        lbl2 = Label(frame2, text = "fecha" )
        lbl2.place(x = 3, y = 55)
        self.txtFecha = Entry(frame2)
        self.txtFecha.place(x = 3, y = 75, width = 50, height = 20)

        lbl3 = Label(frame2, text = "recibe" )
        lbl3.place(x = 3, y = 105)
        lbl3.txtidPedidos = Entry(frame2)
        lbl3.txtidPedidos.place(x = 3, y = 125, width = 50, height = 20)

        lbl4 = Label(frame2, text = "lugar entrega" )
        lbl4.place(x = 3, y = 160)
        #lbl4.txtidPedidos = Entry(frame2)
        #lbl4.txtidPedidos.place(x = 3, y = 180, width = 50, height = 20)

        #self.btnGuardar = Button(frame2, text = "Guardar", command = self.fGuardar, bg ="green")
        
        #self.grid.heading("#0", text = "Idpedido", anchor=CENTER)
        #self.grid.heading("#0", text = "fecha", anchor = CENTER)



        


        