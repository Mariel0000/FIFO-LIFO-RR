def calcular_metricas(ti, t, tf):
    n = len(ti)
    T, E, I = [], [], []
    
    for i in range(n):
        t_val = tf[i] - ti[i]        # Tiempo de servicio
        e_val = t_val - t[i]         # Tiempo de espera
        i_val = t[i] / t_val if t_val != 0 else 0 
        
        T.append(t_val)
        E.append(e_val)
        I.append(i_val)

    pT = sum(T) / n
    pE = sum(E) / n
    pI = sum(I) / n

    return T, E, I, pT, pE, pI
