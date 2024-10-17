import tkinter as tk
from tkinter import messagebox

class Cine:
    def __init__(self):
        self.boletas = []

    def comprar_boleta(self, nombre_pelicula):
        self.boletas.append(nombre_pelicula)

    def cancelar_boleta(self, nombre_pelicula):
        if nombre_pelicula in self.boletas:
            self.boletas.remove(nombre_pelicula)
            return True
        return False

    def obtener_boletas(self):
        return self.boletas

class Aplicacion(tk.Tk):
    def __init__(self, cine):
        super().__init__()
        self.cine = cine
        self.title("Sistema de Boletas de Cine")
        self.geometry("400x300")

        self.pelicula_entry = tk.Entry(self)
        self.pelicula_entry.pack(pady=10)

        self.comprar_button = tk.Button(self, text="Comprar Boleta", command=self.comprar_boleta)
        self.comprar_button.pack(pady=5)

        self.cancelar_button = tk.Button(self, text="Cancelar Boleta", command=self.cancelar_boleta)
        self.cancelar_button.pack(pady=5)

        self.mostrar_button = tk.Button(self, text="Mostrar Boletas", command=self.mostrar_boletas)
        self.mostrar_button.pack(pady=5)

        self.boletas_listbox = tk.Listbox(self)
        self.boletas_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    def comprar_boleta(self):
        nombre_pelicula = self.pelicula_entry.get()
        if nombre_pelicula:
            self.cine.comprar_boleta(nombre_pelicula)
            self.pelicula_entry.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Boleta para '{nombre_pelicula}' comprada.")
        else:
            messagebox.showwarning("Advertencia", "Ingrese el nombre de la película.")

    def cancelar_boleta(self):
        nombre_pelicula = self.pelicula_entry.get()
        if self.cine.cancelar_boleta(nombre_pelicula):
            self.pelicula_entry.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Boleta para '{nombre_pelicula}' cancelada.")
        else:
            messagebox.showwarning("Advertencia", "Boleta no encontrada.")

    def mostrar_boletas(self):
        self.boletas_listbox.delete(0, tk.END)  # Limpiar la lista
        boletas = self.cine.obtener_boletas()
        if boletas:
            for boleta in boletas:
                self.boletas_listbox.insert(tk.END, boleta)
        else:
            messagebox.showinfo("Información", "No hay boletas compradas.")

if __name__ == "__main__":
    cine = Cine()
    app = Aplicacion(cine)
    app.mainloop()
