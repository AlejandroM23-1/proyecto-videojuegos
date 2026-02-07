generos= {
    "Honkai: Star rail": "RPG",
    "Left 4 dead 2": "Horror",
    "Counter Strike": "Shooter",
    "Genshin Impact": "Aventura",
    "Wuthering Waves": "Aventura",
    "Silent Hill": "Horror"
    }

ventas_y_stock= {
    "Honkai: Star rail": (400, 220),
    "Left 4 dead 2": (660, 20),
    "Counter Strike": (50, 120),
    "Genshin Impact": (500, 600),
    "Wuthering Waves": (680, 120),
    "Silent Hill": (924, 3)
    }

clientes={
    "Honkai: Star rail": {"Xalo", "Godlon", "Alejandro", "Enita", "Noah"},
    "Left 4 dead 2": {"Snickzz", "Yashuri", "Alexander", "Alejandro"},
    "Counter Strike": {"Black", "Monesy", "ByStaxx"},
    "Genshin Impact": {"Putupau", "Alpha", "Manuel", "Ramiro"},
    "Wuthering Waves": {"Putupau", "Alpha", "Darko"},
    "Silent Hill": {"Alexander", "Diego", "José"}
    }
juegos= ["Honkai: Star rail", "Left 4 dead 2", "Counter Strike", "Genshin Impact", "Wuthering Waves", "Silent Hill"]

def resumen_juego(juego):
    print(f"\nResumen de | {juego}:\n")
    print(f"\t Género del juego: {generos[juego]}")
    print(f"\t Total de ventas para este juego: {ventas_y_stock[juego][0]} unidades.")
    print(f"\t Total de stock para este juego: {ventas_y_stock[juego][1]} unidades.")
    print(f"\t Clientes que han adquirido el juego: {', '.join(clientes[juego])}")

limite= 500
def mostrar_resumenes():
    for juego in juegos:
        if ventas_y_stock[juego][0] > limite:
            resumen_juego(juego)
mostrar_resumenes()    
ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > limite)

print(f"\n El total de ventas de todos los productos han sido {ventas_totales()} productos")
