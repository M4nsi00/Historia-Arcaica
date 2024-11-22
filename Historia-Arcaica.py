def mapa():
    puntos_vida = 100
    print ("Eres un aventurero que entro en una cueva, mientras que la investigas encuentras una espada dentro de una piedra \n")
    print ("Hay un grabado en la piedra la cual dice que para sacar la piedra debes debes de calcular la fuerza necesaria para sacar la espada de la piedra \n")
    #Para estas líneas de código estoy utilizando el tema de trabajo
    print("Sabes que tienes un trabajo de 7.5 Joules y que la espada necesita un desplazamiento de 15 centimetros para que salga, pero ¿cual es la fuerza necesaria? \n")
    fuerza_bien = 7.5/0.15
    #En este caso se aplica la formula de Trabajo = Fuerza * desplazamiento, la cual se despegua quedando que la Fuerza = Fuerza/desplazamiento
    while True:
        fuerza = float(input("Cual es la fuerza necesario para sacar la espada? "))
        if fuerza == fuerza_bien:
            print ("Haz sacado la espada pero algo paso... \n")
            break
        else:
            print ("No es correcta la fuerza calculado")
    #Finaliza
    
    print("De la espada sale una niebla extraña que crea un monstruo \n")
    print("Tambien se escucha una voz que dice \n")
    print("Si quieres vencer a los monstruos debes de calcular la energía que se pierde cuando tu espada choca contra cada monstruo, si no es correcta perderas puntos de vida \n")
    monstruos = 1
    #Para esta parte utilice el tema de choques
    while True:
        print("El monstruo tiene una masa de 80 kg y esta en reposo, tu espada avanza hacia el con una masa de 10 kilogramos a una velocidad de 4 m/s \n")
        #En este caso se utiliza la formula de m1u1 + m2u2 = vc(u1+u2) + perdida
        #En este caso como el monstruo esta en reposo se cancela la parte de m2u2, y en este caso como pide calcular la perdida. Despejamos la formula de forma que queda m1u1 - vc(m1+m2) = perdida
        energia = (10*4)-1*(80+10)
        perdida_energia = int(input("¿Cuanta energía se pierde al momento de que estos dos colicionan si el sistema acaba con una velocidad de 1 m/s? "))
        if perdida_energia == energia:
            print("Haz vencido al monstruo")
            monstruos -=1
        else:
            print("No haz matado al monstruo, perdiste 10 puntos de vida, vuelve a intentar")
            puntos_vida -= 10
        if puntos_vida == 0:
            print("Haz perdido, sales corriendo de la cueva y perdiste la espada")
            break
        elif monstruos == 0:
            print("Haz vencido al monstruo felicidiades, la cueva se ilumina y has encontrado un gran tesoro")
            break  
def main():
    mapa()

main()