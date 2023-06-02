from canvas import Canvas
from shapes import Rectangle, Square

# Perguntando a largura e a altura que enquadrará o(s) desenho(s)
canvas_width = int(input("Coloque a largura do canvas: "))
canvas_height = int(input("Coloque a altura do canvas: "))

colors = {"branco": (255, 255, 255), "preto": (0, 0, 0)}
canvas_color = input('Diga a cor do canvas, "branco" ou "preto" apenas: ')

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])


while True:
    shape_type = input("Gostaria de desenhar um 'quadrado' ou um 'retangulo'(digite sair para parar): ")
    # Caso tenha digitado retângulo
    if shape_type.lower() == 'retangulo':
        rec_x = int(input("x do retângulo: "))
        rec_y = int(input("y do retângulo: "))
        rec_width = int(input("largura do retângulo: "))
        rec_height = int(input("altura do retângulo: "))
        red = int(input("O quão vermelho quer seu retângulo: "))
        green = int(input("O quão verde quer seu retângulo: "))
        blue = int(input("O quão azul quer seu retângulo: "))

        # Criando um retângulo
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    # Caso tenha digitado quadrado
    if shape_type.lower() == 'quadrado':
        squ_x = int(input("x do quadrado: "))
        squ_y = int(input("y do quadrado: "))
        squ_side = int(input("tamanho do quadrado: "))
        red = int(input("O quão vermelho quer seu quadrado: "))
        green = int(input("O quão verde quer seu quadrado: "))
        blue = int(input("O quão azul quer seu quadrado: "))
        color = (red, green, blue)

        # Criando um quadrado
        s1 = Square(x=squ_x, y=squ_y, side=squ_side, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type.lower() == "sair":
        break

    else:
        print("Você digitou algo errado, apenas é possível escrever: quadrado | retangulo | sair")

canvas.make("canvas.png")