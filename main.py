import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

class Youtube_Downloader:
    def __init__(self, root):
        self.root = root
        self._create_widgets()
        
    def _create_widgets(self):
        #Etiquetas del titulo
        self.title_label = tk.Label(self.root, text="Descargador de Videos de YouTube", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
        
        #Formulario de la url
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        #Botones     
        self.download_button = tk.Button(self.root, text="Descargar Video", command= self._download_video)
        self.download_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        #Configuración de la ventana
        self.root.title("Descargar videos de youtube")
        self.root.geometry("350x150")
        self.root.resizable(False, False)
        icono = tk.PhotoImage(file='images/icon.png')
        root.iconphoto(True, icono)
    
    def _download_video(self):
        #Función principal
        url = self.url_entry.get()
        if url:
            try:
                yt = YouTube(url)
                video = yt.streams.get_highest_resolution()
                download_path = filedialog.askdirectory()
                if download_path:
                    video.download(download_path)
                    messagebox.showinfo("¡Exito!", f"Video descargado con éxito: {yt.title} \n Guardado en: {download_path}")
                else:
                    messagebox.showerror("¡Error!", f"¡No se pudo descargar el video!")
            except:
                messagebox.showwarning("Advertencia", "Por favor, introduce una URL válida")
                
root = tk.Tk()
descargar = Youtube_Downloader(root)
root.mainloop()