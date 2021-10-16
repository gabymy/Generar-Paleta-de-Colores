from tkinter import *
import random 
from random import sample
from random import choice

ventana = Tk()
ventana.title("Palette Gen")
ventana.config(bg="#000066")
ventana.geometry("400x500")
ventana.resizable(0,0)

#color
fondo1 = Label(ventana, width=40, height=20)
fondo1.pack(pady=5, fill=X)
nombre1 = Label(fondo1, font= ("Comic Sans MS", 10), bg="#CCCCFF", fg="black")
nombre1.pack(side=LEFT, padx=10, pady=20)
color1 = Button(fondo1, text="Cambiar color", font= ("Comic Sans MS", 10), command= lambda: elegircolor1(), bg="#CCCCFF", fg="black")
color1.pack(side=RIGHT, padx=10, pady=20)

fondo2 = Label(ventana, width=40, height=20)
fondo2.pack(pady=5, fill=X)
nombre2 = Label(fondo2, font= ("Comic Sans MS", 10), bg="#CCCCFF", fg="black")
nombre2.pack(side=LEFT, padx=10, pady=20)
color2 = Button(fondo2, text="Cambiar color", font= ("Comic Sans MS", 10), command= lambda: elegircolor2(), bg="#CCCCFF", fg="black")
color2.pack(side=RIGHT, padx=10, pady=20)

fondo3 = Label(ventana, width=40, height=20)
fondo3.pack(pady=5, fill=X)
nombre3 = Label(fondo3, font= ("Comic Sans MS", 10), bg="#CCCCFF", fg="black")
nombre3.pack(side=LEFT, padx=10, pady=20)
color3 = Button(fondo3, text="Cambiar color", font= ("Comic Sans MS", 10), command= lambda: elegircolor3(), bg="#CCCCFF", fg="black")
color3.pack(side=RIGHT, padx=10, pady=20)

fondo4 = Label(ventana, width=40, height=20)
fondo4.pack(pady=5, fill=X)
nombre4 = Label(fondo4, font= ("Comic Sans MS", 10), bg="#CCCCFF", fg="black")
nombre4.pack(side=LEFT, padx=10, pady=20)
color4 = Button(fondo4, text="Cambiar color", font= ("Comic Sans MS", 10), command= lambda: elegircolor4(), bg="#CCCCFF", fg="black")
color4.pack(side=RIGHT, padx=10, pady=20)

fondo5 = Label(ventana, width=40, height=20)
fondo5.pack(pady=5, fill=X)
nombre5 = Label(fondo5, font= ("Comic Sans MS", 10), bg="#CCCCFF", fg="black")
nombre5.pack(side=LEFT, padx=10, pady=20)
color5 = Button(fondo5, text="Cambiar color", font= ("Comic Sans MS", 10), command= lambda: elegircolor5(), bg="#CCCCFF", fg="black")
color5.pack(side=RIGHT, padx=10, pady=20)

#boton
elegir = Button(ventana, text="Generar Nueva Paleta", font=("Comic Sans MS", 10), command= lambda:color(), bg="#CCCCFF", fg="black")
elegir. pack(padx=30, pady=20)

#función
def color():
 hexa = [ "#FFFFFF", "#F0FFFF", "#F5FFFA", "#FFFAFA", "#FFFFF0", "#F8F8FF", "#FFFAF0", "#F0F8FF", "#E0FFFF", "#F0FFF0", "#FFFFE0", "#FFF5EE", "#FFF0F5", "#F5F5F5", "#FDF5E6", "#FFF8DC", "#FAF0E6", "#FAFAD2", "#FFFACD", "#F5F5DC", "#E6E6FA", "#FFEFD5", "#FFE4E1", "#FAEBD7", "#FFEBCD", "#FFE4C4", "#AFEEEE", "#FFE4B5", "#DCDCDC", "#FFDAB9", "#FFDEAD", "#EEE8AA", "#F5DEB3", "#B0E0E6", "#7FFFD4", "#D3D3D3", "#FFC0CB", "#ADD8E6", "#D8BFD8", "#FFB6C1", "#87CEFA", "#98FB98", "#B0C4DE", "#F0D58C", "#87CEEB", "#00FFFF", "#00FFFF", "#C0C0C0", "#DDA0DD", "#BEBEBE", "#90EE90", "#EE82EE", "#FFFF00", "#40E0D0", "#DEB887", "#ADFF2F", "#D2B48C", "#48D1CC", "#FFA07A", "#66CDAA", "#A9A9A9", "#DA70D6", "#8FBC8F", "#00BFFF", "#F4A460", "#FFD700", "#00FA9A", "#BDB76B", "#6495ED", "#FF69B4", "#E9967A", "#00CED1", "#00FF7F", "#F08080", "#BC8F8F", "#FA8072", "#7FFF00", "#9370DB", "#7CFC00", "#1E90FF", "#9ACD32", "#DB7093", "#7B68EE", "#BA55D3", "#FF7F50", "#5F9EA0", "#20B2AA", "#DAA520", "#FFA500", "#778899", "#FF00FF", "#FF00FF", "#3CB371", "#CD853F", "#4682B4", "#4169E1", "#708090", "#FF6347", "#FF8C00", "#6A5ACD", "#32CD32", "#00FF00", "#CD5C5C", "#9932CC", "#8A2BE2", "#FF1493", "#B8860B", "#D2691E", "#008B8B", "#696969", "#6B8E23", "#2E8B57", "#008080", "#9400D3", "#C71585", "#FF4500", "#808000", "#A0522D",
 "#483D8B", "#556B2F", "#228B22", "#DC143C", "#0000FF", "#8B008B", "#2F4F4F", "#8B4513", "#A52A2A", "#B22222", "#800080", "#008000", "#FF0000", "#0000CD", "#4B0082", "#191970", "#006400", "#00008B", "#000080", "#8B0000", "#800000", "#000000"]
 c1, c2, c3, c4, c5 = random.sample(hexa, 5)
 fondo1["bg"]= c1
 nombre1["text"]= c1

 fondo2["bg"]=c2
 nombre2["text"]=c2

 fondo3["bg"]=c3
 nombre3["text"]=c3

 fondo4["bg"]=c4
 nombre4["text"]=c4

 fondo5["bg"]=c5
 nombre5["text"]=c5

def elegircolor1():
 hexa = [ "#FFFFFF", "#F0FFFF", "#F5FFFA", "#FFFAFA", "#FFFFF0", "#F8F8FF", "#FFFAF0", "#F0F8FF", "#E0FFFF", "#F0FFF0", "#FFFFE0", "#FFF5EE", "#FFF0F5", "#F5F5F5", "#FDF5E6", "#FFF8DC", "#FAF0E6", "#FAFAD2", "#FFFACD", "#F5F5DC", "#E6E6FA", "#FFEFD5", "#FFE4E1", "#FAEBD7", "#FFEBCD", "#FFE4C4", "#AFEEEE", "#FFE4B5", "#DCDCDC", "#FFDAB9", "#FFDEAD", "#EEE8AA", "#F5DEB3", "#B0E0E6", "#7FFFD4", "#D3D3D3", "#FFC0CB", "#ADD8E6", "#D8BFD8", "#FFB6C1", "#87CEFA", "#98FB98", "#B0C4DE", "#F0D58C", "#87CEEB", "#00FFFF", "#00FFFF", "#C0C0C0", "#DDA0DD", "#BEBEBE", "#90EE90", "#EE82EE", "#FFFF00", "#40E0D0", "#DEB887", "#ADFF2F", "#D2B48C", "#48D1CC", "#FFA07A", "#66CDAA", "#A9A9A9", "#DA70D6", "#8FBC8F", "#00BFFF", "#F4A460", "#FFD700", "#00FA9A", "#BDB76B", "#6495ED", "#FF69B4", "#E9967A", "#00CED1", "#00FF7F", "#F08080", "#BC8F8F", "#FA8072", "#7FFF00", "#9370DB", "#7CFC00", "#1E90FF", "#9ACD32", "#DB7093", "#7B68EE", "#BA55D3", "#FF7F50", "#5F9EA0", "#20B2AA", "#DAA520", "#FFA500", "#778899", "#FF00FF", "#FF00FF", "#3CB371", "#CD853F", "#4682B4", "#4169E1", "#708090", "#FF6347", "#FF8C00", "#6A5ACD", "#32CD32", "#00FF00", "#CD5C5C", "#9932CC", "#8A2BE2", "#FF1493", "#B8860B", "#D2691E", "#008B8B", "#696969", "#6B8E23", "#2E8B57", "#008080", "#9400D3", "#C71585", "#FF4500", "#808000", "#A0522D",
 "#483D8B", "#556B2F", "#228B22", "#DC143C", "#0000FF", "#8B008B", "#2F4F4F", "#8B4513", "#A52A2A", "#B22222", "#800080", "#008000", "#FF0000", "#0000CD", "#4B0082", "#191970", "#006400", "#00008B", "#000080", "#8B0000", "#800000", "#000000"]
 co1 = random.choice(hexa)
 fondo1["bg"]= co1
 nombre1["text"]= co1

def elegircolor2():
 hexa = [ "#FFFFFF", "#F0FFFF", "#F5FFFA", "#FFFAFA", "#FFFFF0", "#F8F8FF", "#FFFAF0", "#F0F8FF", "#E0FFFF", "#F0FFF0", "#FFFFE0", "#FFF5EE", "#FFF0F5", "#F5F5F5", "#FDF5E6", "#FFF8DC", "#FAF0E6", "#FAFAD2", "#FFFACD", "#F5F5DC", "#E6E6FA", "#FFEFD5", "#FFE4E1", "#FAEBD7", "#FFEBCD", "#FFE4C4", "#AFEEEE", "#FFE4B5", "#DCDCDC", "#FFDAB9", "#FFDEAD", "#EEE8AA", "#F5DEB3", "#B0E0E6", "#7FFFD4", "#D3D3D3", "#FFC0CB", "#ADD8E6", "#D8BFD8", "#FFB6C1", "#87CEFA", "#98FB98", "#B0C4DE", "#F0D58C", "#87CEEB", "#00FFFF", "#00FFFF", "#C0C0C0", "#DDA0DD", "#BEBEBE", "#90EE90", "#EE82EE", "#FFFF00", "#40E0D0", "#DEB887", "#ADFF2F", "#D2B48C", "#48D1CC", "#FFA07A", "#66CDAA", "#A9A9A9", "#DA70D6", "#8FBC8F", "#00BFFF", "#F4A460", "#FFD700", "#00FA9A", "#BDB76B", "#6495ED", "#FF69B4", "#E9967A", "#00CED1", "#00FF7F", "#F08080", "#BC8F8F", "#FA8072", "#7FFF00", "#9370DB", "#7CFC00", "#1E90FF", "#9ACD32", "#DB7093", "#7B68EE", "#BA55D3", "#FF7F50", "#5F9EA0", "#20B2AA", "#DAA520", "#FFA500", "#778899", "#FF00FF", "#FF00FF", "#3CB371", "#CD853F", "#4682B4", "#4169E1", "#708090", "#FF6347", "#FF8C00", "#6A5ACD", "#32CD32", "#00FF00", "#CD5C5C", "#9932CC", "#8A2BE2", "#FF1493", "#B8860B", "#D2691E", "#008B8B", "#696969", "#6B8E23", "#2E8B57", "#008080", "#9400D3", "#C71585", "#FF4500", "#808000", "#A0522D",
 "#483D8B", "#556B2F", "#228B22", "#DC143C", "#0000FF", "#8B008B", "#2F4F4F", "#8B4513", "#A52A2A", "#B22222", "#800080", "#008000", "#FF0000", "#0000CD", "#4B0082", "#191970", "#006400", "#00008B", "#000080", "#8B0000", "#800000", "#000000"]
 co2 = random.choice(hexa)
 fondo2["bg"]= co2
 nombre2["text"]= co2

def elegircolor3():
 hexa = [ "#FFFFFF", "#F0FFFF", "#F5FFFA", "#FFFAFA", "#FFFFF0", "#F8F8FF", "#FFFAF0", "#F0F8FF", "#E0FFFF", "#F0FFF0", "#FFFFE0", "#FFF5EE", "#FFF0F5", "#F5F5F5", "#FDF5E6", "#FFF8DC", "#FAF0E6", "#FAFAD2", "#FFFACD", "#F5F5DC", "#E6E6FA", "#FFEFD5", "#FFE4E1", "#FAEBD7", "#FFEBCD", "#FFE4C4", "#AFEEEE", "#FFE4B5", "#DCDCDC", "#FFDAB9", "#FFDEAD", "#EEE8AA", "#F5DEB3", "#B0E0E6", "#7FFFD4", "#D3D3D3", "#FFC0CB", "#ADD8E6", "#D8BFD8", "#FFB6C1", "#87CEFA", "#98FB98", "#B0C4DE", "#F0D58C", "#87CEEB", "#00FFFF", "#00FFFF", "#C0C0C0", "#DDA0DD", "#BEBEBE", "#90EE90", "#EE82EE", "#FFFF00", "#40E0D0", "#DEB887", "#ADFF2F", "#D2B48C", "#48D1CC", "#FFA07A", "#66CDAA", "#A9A9A9", "#DA70D6", "#8FBC8F", "#00BFFF", "#F4A460", "#FFD700", "#00FA9A", "#BDB76B", "#6495ED", "#FF69B4", "#E9967A", "#00CED1", "#00FF7F", "#F08080", "#BC8F8F", "#FA8072", "#7FFF00", "#9370DB", "#7CFC00", "#1E90FF", "#9ACD32", "#DB7093", "#7B68EE", "#BA55D3", "#FF7F50", "#5F9EA0", "#20B2AA", "#DAA520", "#FFA500", "#778899", "#FF00FF", "#FF00FF", "#3CB371", "#CD853F", "#4682B4", "#4169E1", "#708090", "#FF6347", "#FF8C00", "#6A5ACD", "#32CD32", "#00FF00", "#CD5C5C", "#9932CC", "#8A2BE2", "#FF1493", "#B8860B", "#D2691E", "#008B8B", "#696969", "#6B8E23", "#2E8B57", "#008080", "#9400D3", "#C71585", "#FF4500", "#808000", "#A0522D",
 "#483D8B", "#556B2F", "#228B22", "#DC143C", "#0000FF", "#8B008B", "#2F4F4F", "#8B4513", "#A52A2A", "#B22222", "#800080", "#008000", "#FF0000", "#0000CD", "#4B0082", "#191970", "#006400", "#00008B", "#000080", "#8B0000", "#800000", "#000000"]
 co3 = random.choice(hexa)
 fondo3["bg"]= co3
 nombre3["text"]= co3

def elegircolor4():
 hexa = [ "#FFFFFF", "#F0FFFF", "#F5FFFA", "#FFFAFA", "#FFFFF0", "#F8F8FF", "#FFFAF0", "#F0F8FF", "#E0FFFF", "#F0FFF0", "#FFFFE0", "#FFF5EE", "#FFF0F5", "#F5F5F5", "#FDF5E6", "#FFF8DC", "#FAF0E6", "#FAFAD2", "#FFFACD", "#F5F5DC", "#E6E6FA", "#FFEFD5", "#FFE4E1", "#FAEBD7", "#FFEBCD", "#FFE4C4", "#AFEEEE", "#FFE4B5", "#DCDCDC", "#FFDAB9", "#FFDEAD", "#EEE8AA", "#F5DEB3", "#B0E0E6", "#7FFFD4", "#D3D3D3", "#FFC0CB", "#ADD8E6", "#D8BFD8", "#FFB6C1", "#87CEFA", "#98FB98", "#B0C4DE", "#F0D58C", "#87CEEB", "#00FFFF", "#00FFFF", "#C0C0C0", "#DDA0DD", "#BEBEBE", "#90EE90", "#EE82EE", "#FFFF00", "#40E0D0", "#DEB887", "#ADFF2F", "#D2B48C", "#48D1CC", "#FFA07A", "#66CDAA", "#A9A9A9", "#DA70D6", "#8FBC8F", "#00BFFF", "#F4A460", "#FFD700", "#00FA9A", "#BDB76B", "#6495ED", "#FF69B4", "#E9967A", "#00CED1", "#00FF7F", "#F08080", "#BC8F8F", "#FA8072", "#7FFF00", "#9370DB", "#7CFC00", "#1E90FF", "#9ACD32", "#DB7093", "#7B68EE", "#BA55D3", "#FF7F50", "#5F9EA0", "#20B2AA", "#DAA520", "#FFA500", "#778899", "#FF00FF", "#FF00FF", "#3CB371", "#CD853F", "#4682B4", "#4169E1", "#708090", "#FF6347", "#FF8C00", "#6A5ACD", "#32CD32", "#00FF00", "#CD5C5C", "#9932CC", "#8A2BE2", "#FF1493", "#B8860B", "#D2691E", "#008B8B", "#696969", "#6B8E23", "#2E8B57", "#008080", "#9400D3", "#C71585", "#FF4500", "#808000", "#A0522D",
 "#483D8B", "#556B2F", "#228B22", "#DC143C", "#0000FF", "#8B008B", "#2F4F4F", "#8B4513", "#A52A2A", "#B22222", "#800080", "#008000", "#FF0000", "#0000CD", "#4B0082", "#191970", "#006400", "#00008B", "#000080", "#8B0000", "#800000", "#000000"]
 co4 = random.choice(hexa)
 fondo4["bg"]= co4
 nombre4["text"]= co4

def elegircolor5():
 hexa = [ "#FFFFFF", "#F0FFFF", "#F5FFFA", "#FFFAFA", "#FFFFF0", "#F8F8FF", "#FFFAF0", "#F0F8FF", "#E0FFFF", "#F0FFF0", "#FFFFE0", "#FFF5EE", "#FFF0F5", "#F5F5F5", "#FDF5E6", "#FFF8DC", "#FAF0E6", "#FAFAD2", "#FFFACD", "#F5F5DC", "#E6E6FA", "#FFEFD5", "#FFE4E1", "#FAEBD7", "#FFEBCD", "#FFE4C4", "#AFEEEE", "#FFE4B5", "#DCDCDC", "#FFDAB9", "#FFDEAD", "#EEE8AA", "#F5DEB3", "#B0E0E6", "#7FFFD4", "#D3D3D3", "#FFC0CB", "#ADD8E6", "#D8BFD8", "#FFB6C1", "#87CEFA", "#98FB98", "#B0C4DE", "#F0D58C", "#87CEEB", "#00FFFF", "#00FFFF", "#C0C0C0", "#DDA0DD", "#BEBEBE", "#90EE90", "#EE82EE", "#FFFF00", "#40E0D0", "#DEB887", "#ADFF2F", "#D2B48C", "#48D1CC", "#FFA07A", "#66CDAA", "#A9A9A9", "#DA70D6", "#8FBC8F", "#00BFFF", "#F4A460", "#FFD700", "#00FA9A", "#BDB76B", "#6495ED", "#FF69B4", "#E9967A", "#00CED1", "#00FF7F", "#F08080", "#BC8F8F", "#FA8072", "#7FFF00", "#9370DB", "#7CFC00", "#1E90FF", "#9ACD32", "#DB7093", "#7B68EE", "#BA55D3", "#FF7F50", "#5F9EA0", "#20B2AA", "#DAA520", "#FFA500", "#778899", "#FF00FF", "#FF00FF", "#3CB371", "#CD853F", "#4682B4", "#4169E1", "#708090", "#FF6347", "#FF8C00", "#6A5ACD", "#32CD32", "#00FF00", "#CD5C5C", "#9932CC", "#8A2BE2", "#FF1493", "#B8860B", "#D2691E", "#008B8B", "#696969", "#6B8E23", "#2E8B57", "#008080", "#9400D3", "#C71585", "#FF4500", "#808000", "#A0522D",
 "#483D8B", "#556B2F", "#228B22", "#DC143C", "#0000FF", "#8B008B", "#2F4F4F", "#8B4513", "#A52A2A", "#B22222", "#800080", "#008000", "#FF0000", "#0000CD", "#4B0082", "#191970", "#006400", "#00008B", "#000080", "#8B0000", "#800000", "#000000"]
 co5 = random.choice(hexa)
 fondo5["bg"]= co5
 nombre5["text"]= co5
 

ventana.mainloop()
