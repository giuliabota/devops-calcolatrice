from operazioni import somma, sottrazione, moltiplicazione

def calcolatrice(operazione: str, a: float, b: float):
    if operazione == "somma":
        return somma(a, b)
    elif operazione == "sottrazione":
        return sottrazione(a, b)
    elif operazione == "moltiplicazione":
        return moltiplicazione(a, b)    
    else:
        return None
    
#Esempi di utilizzo con output esplicito degli input e output
if __name__ == "__main__":
    print("Somma di 3 e 5:", calcolatrice("somma", 3, 5))
    print("Sottrazione di 10 e 4:", calcolatrice("sottrazione", 10, 4))
    print("Operazione non valida:", calcolatrice("moltiplicazione", 2, 3))




    