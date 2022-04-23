from tkinter import *
from tkinter import ttk
from database import *
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.ventana = master
        self.dibujarLabel()
        self.dibujarEntry()
        self.dibujarBoton()
        self.dibujarLista("")

    def dibujarLabel(self):
        self.lbl_name = Label(self.ventana, foreground="white", background="#314252", text="Nombre", font=(8)).place(x =60, y=110)
        self.lbl_edad = Label(self.ventana, foreground="white", background="#314252", text="Edad", font=(8)).place(x =60, y=160)
        self.lbl_carrera = Label(self.ventana, foreground="white", background="#314252", text="Carrera ", font=(8)).place(x =60, y=210)

    def dibujarEntry(self):
        self.nombre = StringVar()
        self.edad = StringVar()
        self.carrera = StringVar()
        self.buscar_= StringVar()
        self.txt_nombre = Entry(self.ventana, font=('Arial', 12), textvariable=self.nombre).place(x=140, y=110)
        self.txt_edad = Entry(self.ventana, font=('Arial', 12), textvariable=self.edad).place(x=140, y=160)
        self.txt_carrera = Entry(self.ventana, font=('Arial', 12), textvariable=self.carrera).place(x=140, y=210)

        #Agregando Buscar
        self.txt_buscar = Entry(self.ventana, font=('Arial', 12), textvariable= self.buscar_).place(x=60, y=340)

    def vaciarEntry(self, text):
        self.nombre.set(text)
        self.edad.set(text)
        self.carrera.set(text)


    def dibujarBoton(self):
        self.btn_guardar = Button(self.ventana, text="Guardar", relief="flat", background="#0051C8",cursor="hand2", foreground="white", command= lambda : self.guardar()).place(x=750, y=340, width=90)
        self.btn_cancelar = Button(self.ventana, text="Cancelar", relief="flat", background="red",cursor="hand2", foreground="white", command= lambda: self.vaciarEntry("") ).place(x=850, y=340, width=90)

        #Agregando Buscar
        self.btn_buscar= Button(self.ventana, text="Filtrar", relief="flat", background="green", cursor="hand2", foreground="white", command=lambda: self.buscar(self.buscar_.get())).place(x=260, y=340, width=90)


    def buscar(self, ref):
        self.LimpiarLista()
        self.dibujarLista(ref)


    def guardar(self):
        arr = [self.nombre.get(), self.edad.get(), self.carrera.get()]
        d = Data()
        d.insertItems(arr)
        self.nombre.set('')
        self.edad.set('')
        self.carrera.set('')
        self.LimpiarLista()
        self.dibujarLista("")

    def LimpiarLista(self):
        self.lista.delete(*self.lista.get_children())


    def dibujarLista(self, ref):
        self.lista = ttk.Treeview(self.ventana, columns=(1, 2, 3), show="headings", height="8")
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure("Treeview.Heading", background="#0051C8", relief="flat", foreground="white")
        self.lista.heading(1, text="Nombre")
        self.lista.heading(2, text="Edad")
        self.lista.heading(3, text="Carrera")
        self.lista.column(2, anchor=CENTER)

        #Evento
        self.lista.bind('<Double 1>', self.obtenerFila)


        if ref == "":
        # llenar la lista
            d = Data()
            elements = d.returnAllElements()
            for i in elements:
                self.lista.insert('', 'end', values=i)
        else:
            d = Data()
            elements = d.ReturnForCarreer(ref)
            for i in elements:
                self.lista.insert('', 'end', values=i)


        self.lista.place(x=340, y=90)

    def obtenerFila(self, event):
        na = StringVar()
        ed = StringVar()
        ca = StringVar()
        nombreFila = self.lista.identify_row(event.y)
        elemento = self.lista.item(self.lista.focus())
        n = elemento['values'][0]
        e = elemento['values'][1]
        c = elemento['values'][2]
        na.set(n)
        ed.set(e)
        ca.set(c)

        pop = Toplevel(self.ventana)
        pop.geometry('400x200')
        txt_n = Entry(pop, textvariable=na).place(x=40, y=40)
        txt_e = Entry(pop, textvariable=ed).place(x=40, y=80)
        txt_c = Entry(pop, textvariable=ca).place(x=40, y=120)
        #BOTONES
        btn_cambiar = Button(pop, text="Actualizar", relief="flat", background="#00CE54", foreground="white", command=lambda:self.editar(n, na.get(), ed.get(), ca.get())).place(x=180, y=160, width=90)
        btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="red", foreground="white", command=lambda:self.eliminar(na.get())).place(x=290, y=160, width=90)

    def editar(self, n, no, e, c):
        d = Data()
        arr = [no, e, c]
        d.UpdateItem(arr, n)
        messagebox.showinfo(title="Actualización", message="Se ha actualizado la base de datos.")
        self.LimpiarLista()
        self.dibujarLista("")

    def eliminar(self, n):
        d = Data()
        d.Delete(n)
        messagebox.showinfo(title="Actualización", message="Se ha actualizado la base de datos.")
        self.LimpiarLista()
        self.dibujarLista("")

root = Tk()
root.title("CRUD python mysql")
root.geometry("1000x400")
root.config(background="#314252")
aplicacion = App(root)
root.mainloop()