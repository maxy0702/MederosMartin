# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
# Crear el gráfico sin la función seno

plt.figure()

# Añadir líneas verticales y horizontales para dividir los cuadrantes
plt.axvline(x=0, color='red', linestyle='--')
plt.axhline(y=0, color='red', linestyle='--')

# Añadir 10 círculos concéntricos separados a la misma distancia
for i in range(1, 11):
    circle = plt.Circle((0, 0), i, color='blue', fill=False, linestyle='--')
    plt.gca().add_patch(circle)

# Añadir vectores en cada cuadrante con la nueva referencia de ángulos

# Vector en 230 grados (ajustado según nueva referencia)
angle1 = np.deg2rad(30)
end_x1 = 6 * np.sin(angle1)
end_y1 = 6 * np.cos(angle1)
plt.arrow(0, 0, end_x1, end_y1, head_width=0.3, head_length=0.5, fc='purple', ec='purple')

# Vector en 250 grados (ajustado según nueva referencia)
angle3 = np.deg2rad(250)
end_x2 = 7 * np.sin(angle3)
end_y2 = 7 * np.cos(angle3)
plt.arrow(0, 0, end_x2, end_y2, head_width=0.3, head_length=0.5, fc='orange', ec='orange')

# Añadir el vector que une las puntas de los dos vectores anteriores
plt.arrow(end_x1, end_y1, end_x2 - end_x1, end_y2 - end_y1, head_width=0.3, head_length=0.5, fc='orange', ec='orange')



plt.axis('equal')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico con Cruz, 10 Círculos Concéntricos y Vectores Ajustados')
plt.show()