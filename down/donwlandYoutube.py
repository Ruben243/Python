import flet as ft  # Es necesario instalar esta libreria
from pytube import YouTube  # Es necesario isntalar esta libreria
import os  # Esta incluida en Python y es necesaria para las rutas del sistema
from time import sleep

def main(page):
    url = ft.TextField(label="URL", autofocus=True)  # Definimos el label
    submit = ft.ElevatedButton(
        "Descargar"
    )  # Definimos el boton para iniciar la descarga
    pb = ft.ProgressBar(width=400)
    pb.value = 0
    pb.visible = False

    def iniciar_descarga(e):
        current_folder = os.getcwd()  # Carpeta de salida
        yt = YouTube(url.value)  # Creamos un objeto Youtube que recibe la url
        video = (
            yt.streams.get_highest_resolution()
        )  # Obtenemos la maxima resolucion posible
        video.download(
            output_path=current_folder
        )  # Iniciamos la descarga pasandole la carpeta de salida
        if video.filesize:
            pb.visible = True
            page.add(
                ft.Text("Descargas", style="headlineSmall"),
                ft.Column([ft.Text("Descarga"), pb]),
            )
            for i in range(0, video.filesize):
                pb.value = i * 0.01
                sleep(0.1)
                page.update()

    submit.on_click = (
        iniciar_descarga  # Asignamos la funcion iniciar descarga al evento onclick
    )

    page.add(url, submit)  # Añadimos los elementos a la pagina


ft.app(target=main)
