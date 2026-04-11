from fifo import ejecutar_fifo
from lifo import ejecutar_lifo
from rr import ejecutar_rr
from metricas import calcular_metricas
from prints import imprimir_tabla
from comparacion import comparar_algoritmos
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

    # FIFO
    tf_f = ejecutar_fifo(ti, t)
    T_f, E_f, I_f, pT_f, pE_f, pI_f = calcular_metricas(ti, t, tf_f)
    imprimir_tabla("FIFO", procesos, ti, t, tf_f, T_f, E_f, I_f, pT_f, pE_f, pI_f)

    # LIFO
    tf_l = ejecutar_lifo(ti, t)
    T_l, E_l, I_l, pT_l, pE_l, pI_l = calcular_metricas(ti, t, tf_l)
    imprimir_tabla("LIFO", procesos, ti, t, tf_l, T_l, E_l, I_l, pT_l, pE_l, pI_l)

    # Round Robin (q=4)
    tf_r = ejecutar_rr(ti, t, q=4)
    T_r, E_r, I_r, pT_r, pE_r, pI_r = calcular_metricas(ti, t, tf_r)
    imprimir_tabla("Round Robin (q=4)", procesos, ti, t, tf_r, T_r, E_r, I_r, pT_r, pE_r, pI_r)

    # Comparación Final
    res = {"FIFO": pE_f, "LIFO": pE_l, "Round Robin": pE_r}
    comparar_algoritmos(res)

if __name__ == "__main__":
    main()
