import socket
import getpass
import platform

# Información básica del sistema
usuario = getpass.getuser()
hostname = socket.gethostname()
sistema = platform.system()
version = platform.version()
arquitectura = platform.machine()
procesador = platform.processor()

print("===================================")
print("        HOLA MUNDO PYTHON")
print("===================================")

print(f"Usuario       : {usuario}")
print(f"Hostname      : {hostname}")
print(f"Sistema       : {sistema}")
print(f"Versión       : {version}")
print(f"Arquitectura  : {arquitectura}")
print(f"Procesador    : {procesador}")

print("===================================")
print("Programa ejecutado correctamente")
print("===================================")
