def ejecutar_lifo(ti, t):
    n = len(ti)
    tf = [0] * n
    done = [False] * n
    t_clock = 0
    completados = 0

    while completados < n:
        encontrado = False
        for i in range(n-1, -1, -1):
            if not done[i] and ti[i] <= t_clock:
                t_clock += t[i]
                tf[i] = t_clock
                done[i] = True
                completados += 1
                encontrado = True
                break
        if not encontrado:
            t_clock += 1
    return tf
