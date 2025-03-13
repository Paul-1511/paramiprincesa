import turtle
import math

# Configuración inicial
turtle.speed(0)
#turtle.tracer(0, 0)
turtle.hideturtle()
turtle.bgcolor("white")
turtle.pencolor("white")

# Número de puntos y radio del círculo
num_puntos = 350
radio = 430

# Generar los puntos en el círculo
puntos = []
for i in range(num_puntos):
    angle = 2 * math.pi * i / num_puntos
    x = radio * math.cos(angle)
    y = -radio * math.sin(angle)
    puntos.append((x, y))

# Dibujar el círculo con los puntos
turtle.penup()
for x, y in puntos:
    turtle.goto(x, y)
    turtle.dot(3, "black")

# Instrucciones
instrucciones = [96,113,76,103,62,115,71,98,77,112,57,116,67,102,63,113,51,117,56,319,67,99,18,106,58,316,53,121,50,118,55,320,66,117,38,114,75,328,80,96,19,105,61,116,
                 70,321,48,122,46,119,54,321,65,100,10,88,72,114,32,109,80,324,64,332,79,97,4,89,342,91,3,77,333,56,120,173,156,195,212,155,203,163,211,145,214,153,194,
                 294,198,147,210,297,197,149,209,301,206,139,215,144,199,292,187,286,176,155,196,150,208,291,200,141,216,138,218,143,213,154,190,286,179,289,201,164,193,
                 295,211,146,213,294,186,287,175,159,193,285,188,291,182,288,209,298,207,153,177,289,190,165,278,170,280,339,87,5,76,327,83,332,57,107,17,100,3,93,20,85,
                 326,53,125,50,312,42,119,61,315,57,318,68,98,19,103,12,86,336,55,334,75,22,84,112,97,348,284,194,157,263,162,212,139,228,146,199,296,211,287,202,140,
                 204,299,196,152,227,140,214,142,222,136,219,307,36,322,47,310,43,123,60,120,40,320,71,317,41,313,58,114,30,110,78,323,35,327,88,108,16,105,59,111,87,
                 331,58,128,204,151,244,143,231,135,216,306,37,321,39,113,73,335,63,314,27,301,203,153,260,155,264,161,267,327,81,333,276,171,283,190,296,185,292,181,
                 152,208,302,220,133,232,142,76,20,90,329,74,23,102,2,94,6,291,211,148,197,298,205,285,191,164,271,332,82,321,242,152,261,158,187,288,213,136,119,48,309,
                 44,122,55,129,218,306,24,315,73,6,100,64,119,180,288,1,95,340,70,7,92,69,8,290,212,144,230,136,66,113,33,328,87,11,67,133,217,303,202,156,208,297,184,
                 166,189,290,178,292,210,149,246,143,75,317,240,138,229,145,205,162,195,283,169,281,172,109,15,307,20,86,330,70,336,52,131,233,135,237,318,40,124,42,306,
                 30,222,33,225,147,204,291,186,295,16,86,151,192,299,184,117,57,129,203,286,342,63,325,76,316,56,335,270,165,103,0,97,159,267,338,73,318,70,3,101,346,94,
                 68,128,220,148,249,320,26,302,204,122,219,28,115,95,331,272,162,95,333,78,111,44,246,321,22,80,141,236,138,211,188,286,212,294,176,280,196,305,25,215,
                 134,238,315,59,127,228,37,303,197,154,180,158,201,304,31,120,206,143,216,131,54,337,269,173,275,342,103,21,84,331,67,111,14,349,104,18,311,60,126,229,
                 38,302,186,289,212,137,207,294,209,146,203,303,32,223,35,221,34,224,127,71,91,328,261,331,97,29,223,130,217,124,55,349,283,163,194,150,245,45,120,220,
                 304,184,151,262,327,92,338,51,250,48,320,80,340,67,321,79,1,62,104,164,279,198,132,239,129,44,243,144,72,329,61,12,182,167,286,192,307,23,317,50,132,
                 281,166,273,326,268,155,98,347,285,141,226,32,118,65,341,98,336,93,125,39,227,146,198,296,146,251,47,243,317,29,215,11,290,183,168,284,189,156,90,9,172,
                 299,151,215,288,136,214,15,348,63,114,46,327,253,103,338,82,108,7,210,142,78,212,133,276,341,90,4,292,146,235,18,186,165,200,294,143,73,204,152,234,19,
                 94,334,66,200,278,131,221,119,260,332,99,24,73,111,52,309,6,170,295,206,158,273,343,86,136,232,125,36,219,134,268,123,45,248,49,65,313,191,153,226,12,
                 214,26,304,152,265,169,5,312,59,195,306,183,14,308,7,168,102,344,272,324,77,315,234,124,28,300,148,195,281,130,55,192,312,220,11,104,336,75,5,211,290,
                 214,95,2,206,299,32,225,14,187,17,191,56,128,240,21,186,115,72,25,116,60,182,300,204,86,143,282,172,270,122,49,133,235,122,30,214,80,348,105,333,259,
                 108,180,307,194,299,186,60,110,253,330,89,107,33,224,28,241,323,85,153,302,150,276,326,263,124,205,71,339,49,255,149,217,28,13,229,43,133,280,138,230,
                 125,262,114,255,164,299,29,123,265,339,100,249,327,73,10,167,12,66,195,133,238,21,216,150,205,6,173,298,218,294,174,116,69,310,156,293,177,50,251,318,
                 81,96,160,192,283,2,169,299,146,71,26,125,241,43,207,1,314,74,98,250,319,49,118,37,121,271,345,99,214,53,250,147,222,34,199,142,247,137,287,341,108,
                 337,105,224,129,282,206,44,228,22,345,285,160,303,149,296,209,140,90,326,75,7,93,348,95,329,272,159,196,67,8,208,76,334,258,161,300,145,77,320,83,23,
                 215,135,48,32,344,62,122,269,133,264,113,81,5,164,13,232,16,175,191,209,151,295,173,315,189,50,114,22,126,35,220,84,202,157,207,115,252,47,209,90,343,
                 70,309,19,228,67,333,270,132,277,201,124,242,322,64,13,188,299,197,63,101,335,257,109,53,182,19,119,272,327,39,54,249,99,169,271,176,9,288,339,5,215,
                 307,49,178,313,4,282,193,174,314,56,213,101,225,126,18,231,134,216,294,211,141,87,225,31,93,337,84,1,209,6,281,131,199,305,65,137,237,76,195,33,314,64,
                 342,95,242,42,311,181,56,187,20,227,34,223,27,233,125,216,289,78,239,18,61,180,32,228,28,327,96,149,298,200,138,219,293,17,235,73,300,86,318,233,23,79,
                 211,156,6,114,218,37,130,115,248,321,243,41,112,265,334,106,163,94,224,102,166,199,23,226,86,332,266,322,79,5,168,34,55,214,138,287,184,293,153,241,30,
                 121,236,22,243,122,15,63,343,106,272,320,196,24,222,35,133,223,146,130,238,19,320,69,225,41,184,48,234,133,113,256,29,308,11,280,325,79,132,60,44,305,
                 151,213,187,46,203,294,65,8,179,321,195,310,211,298,189,287,129,38,203,88,127,261,135,193,26,251,48,123,218,148,304,67,129,259,107,54,193,209,138,180,
                 57,32,298,92,236,145,294,77,304,186,160,260,106,91,168,9,207,144,278,199,78,292,220,98,307,21,129,279,141,267,331,100,167,35,226,68,117,241,48,308,71,
                 328,248,55,216,342,23,242,29,222,42,315,244,116,50,138,222,10,309,157,335,96,241,127,283,119,103,212,281,152,192,27,329,260,334,6,311,108,334,158,197,
                 319,80,288,62,336,5,227,133,265,35,219,99,65,335,105,269,112,338,53,253,317,4,171,34,230,137,202,154,187,67,230,19,88,317,52,215,89,126,38,166,11,70,
                 85,336,256,120,324,83,204,45,242,133,251,27,296,205,146,162,299,90,0,225,119,209,74,299,183,51,255,102,339,46,118,275,110,308,158,274,111,177,316,331,
                 69,97,304,200,109,315,83,241,137,215,8,279,55,182,307,114,76,305,31,68,182,107,212,23,124,267,173,158,268,118,257,163,16,62,310,9,223,87,208,142,297,93,
                 335,99,33,231,14,125,283,131,36,217,288,273,323,193,170,297,198,151,76,299,165,12,307,72,56,247,116,53,194,25,306,73,342,120,270,2,86,303,100,218,19,
                 291,81,243,27,254,174,30,233,134,211,24,39,199,148,227,33,134,208,294,214,128,282,137,152,300,17,347,88,222,38,120,16,306,75,238,143,53,213,337,322,239,
                 31,137,268,166,277,331,188,150,214,77,92,208,48,73,186,292,180,7,78,303,42,246,133,256,317,168,153,299,87,150,204,126,141,43,221,59,187,290,20,229,2,
                 313,121,63,220,34,225,16,211,304,85,238,118,43,188,64,307,56,258,117,212,4,269,251,30,228,145,1,177,57,210,80,206,52,251,330,100,213,31,119,41,327,34,
                 249,114,55,188,277,108,208,147,305,38,214,289,84,3,78,326,256,36,225,40,202,295,88,135,67,328,31,227,294,171,94,296,169,88,216,133,248,26,229,15,235,
                 323,121,164,208,124,317,82,299,158,16,195,159,103,270,347,225,71,321,261,278,133,240,314,119,94,37,54,244,121,253,28,61,337,2,160,84,155,274,342,270,
                 129,329,186,297,87,204,134,14,162,191,60,104,252,90,338,221,62,328,313,175,101,261,133,236,77,11,232,28,178,43,75,327,142,205,1,170,9,178,299,80,321,
                 244,21,56,113,315,231,247,331,280,198,35,215,37,167,297,192,139,233,147,127,288,85,345,18,131,53,308,103,337,114,268,6,310,51,176,65,194,281,296,311,45,
                 209,130,286,87,109,276,202,162,47,117,217,294,97,222,31,231,22,343,200,295,226,346,272,256,126,0,315,41,227,96,213,42,23,178,62,125,19,233,324,58,300,78,
                 113,59,214,199,184,306,160,301,144,204,105,41,222,36,123,234,129,219,142,225,30,259,116,345,60,19,159,200,62,224,85,299,102,313,138,30,257,50,214,79,341,
                 272,114,280,173,199,150,219,297,211,140,81,4,181,308,24,230,38,318,74,337,159,5,72,316,237,92,203,151,301,25,225,134,34,241,77,42,128,324,34,246,261,115,
                 304,196,336,95,332,150,56,211,118,24,113,308,164,185,305,84,313,156,141,286,217,82,242,116,334,188,114,265,244,147,49,271,112,26,330,125,238,121,142,171,
                 307,117,246,21,348,269,343,131,267,146,204,298,166,93,214,229,140,327,89,294,279,45,222,32,136,216,144,211,326,48,116,71,7,154,175,67,239,46,185,298,103,
                 65,11,295,212,324,71,300,156,20,319,236,15,107,222,39,164,335,67,301,141,252,114,284,162,266,168,198,152,48,273,112,346,247,82,205,121,320,274,189,288,
                 21,233,51,210,71,203,220,116,251,236,34,319,72,54,215,22,318,83,291,131,237,119,271,340,23,197,180,299,202,147,190,258,108,316,171,32,264,100,45,276,66,
                 98,136,204,2,17,132,117,44,125,229,0
]

# Dibujar las líneas según las instrucciones
turtle.pensize(1)
turtle.pencolor("black")
turtle.penup()
turtle.hideturtle()

for i in range(len(instrucciones) - 1):
    punto1 = puntos[instrucciones[i] % num_puntos]
    punto2 = puntos[instrucciones[i+1] % num_puntos]
    turtle.hideturtle()
    turtle.goto(punto1)
    turtle.pendown()
    turtle.goto(punto2)
    turtle.penup()

# Mantener la ventana abierta
turtle.done()