def comparar_algoritmos(resultados):
    print("\n" + "*" * 50)
    print("RESUMEN DE PROMEDIOS (pI)") 
    print("*" * 50)

    for nombre, pI in resultados.items():

        print(f"- {nombre:15}: pI = {pI:.4f}")

    mejor = min(resultados, key=resultados.get) 
    
    print("\nCONCLUSIÓN:")
    print(f"El algoritmo más óptimo es: {mejor.upper()}")
    print("*" * 50 + "\n")
