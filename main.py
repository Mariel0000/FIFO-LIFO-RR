import os

def leer_archivo(ruta):
    procesos, ti, t = [], [], []
    if not os.path.exists(ruta):
        print(f"Error: No se encuentra {ruta}")
        return None, None, None
        
    with open(ruta, 'r') as f:
        lineas = f.readlines()
        for linea in lineas[1:]:
            partes = linea.strip().split(',')
            if len(partes) == 3:
                procesos.append(partes[0])
                ti.append(int(partes[1]))
                t.append(int(partes[2]))
    return procesos, ti, t

def main():
    procesos, ti, t = leer_archivo('procesos.txt')
    if procesos is None: return
