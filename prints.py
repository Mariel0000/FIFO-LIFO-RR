def formatear_numero(val, decimales=4):
    s = f"{val:.{decimales}f}"
    return s.rstrip('0').rstrip('.') if '.' in s else s

def imprimir_tabla(nombre_algo, procesos, ti, t, tf, T, E, I, pT, pE, pI):
    print(f"\n{'='*55}")
    print(f"ESTRATEGIA: {nombre_algo.upper()}")
    print(f"{'='*55}")
    print(f"{'Proc':<6} | {'ti':<4} | {'t':<4} | {'tf':<4} | {'T':<4} | {'E':<4} | {'I'}")
    print("-" * 55)
    
    for i in range(len(procesos)):
        i_str = formatear_numero(I[i], 4)
        print(f"{procesos[i]:<6} | {ti[i]:<4} | {t[i]:<4} | {tf[i]:<4} | {T[i]:<4} | {E[i]:<4} | {i_str}")
        
    print("-" * 55)
    print(f"Promedios: pT = {formatear_numero(pT)}, pE = {formatear_numero(pE)}, pI = {formatear_numero(pI)}")
    print("=" * 55)  
