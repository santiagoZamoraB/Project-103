import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#dirección del directorio que se va a monitorear
from_dir = 'C:/Users/w12w1/Downloads'

#Hacer la clase FileSystemHandler junto con los metodos para realizar el seguimiento de los archivos
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Oye, {event.src_path} ha sido creado")

    def on_deleted(self, event):
        print(f"lo siento, Alguien borró {event.src_path}")

    def on_modified(self, event):
        print(f"El {event.src_path} ha sido modificado")
    
    def on_moved(self, event):
        print(f"el {event.src_path} ha sido movido")

#inicialisamos la clase
event_handler = FileEventHandler()

#Inicia el objeto de la clase Observer
observer = Observer()

#Crea el objeto de la clase Observer
observer.schedule(event_handler, from_dir, recursive=True)

#Inicia la clase Observer
observer.start()

#crea un metodo parar detener el observer con shift + tecla
try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("detenido")
    observer.stop()