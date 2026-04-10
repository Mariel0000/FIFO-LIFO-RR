def ejecutar_rr(ti, t, q=4):
    n = len(ti)
    tf = [0] * n
    rem = list(t)
    done = [False] * n
    t_clock = 0
    completados = 0

    while completados < n:
        encontrado_ciclo = False
        for i in range(n):
            if not done[i] and ti[i] <= t_clock:
                run_time = min(q, rem[i])
                t_clock += run_time
                rem[i] -= run_time
                encontrado_ciclo = True
                
                if rem[i] == 0:
                    done[i] = True
                    tf[i] = t_clock
                    completados += 1
        if not encontrado_ciclo:
            t_clock += 1
    return tf
