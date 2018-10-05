#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:10:21 2018

@authors: Nicolas Miranda & Adrian Garcia
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from mayavi import mlab

tipo_grafo = nx.Graph()

'''
 Creamos el grafo a partir del archivo  datos.txt el cual contiene los valores de
 cada nodo y el peso de las aristas
'''
GRAFO = nx.read_edgelist('data.txt', create_using = tipo_grafo, data=(('weight',float),))


# Definimos nodo origen y destino para determinar la rutina más corta del grafo
origen = 'A'
destino = 'D'


'''
Imprimimos la información más importante del grafo como es el número de nodos, el número
número de aristas y el grado promedio
'''
print nx.info(GRAFO)

print("\n Ruta mas corta")
# Método que nos permite calcular la ruta más corta del grafo usando Dijkstra
ruta_mas_corta = nx.dijkstra_path(GRAFO, origen, destino)
print(' -> '.join(ruta_mas_corta))

print("Longitud de la ruta mas corta")
# Método que nos permite calcular la longitud de la ruta más corta del grafo
print(nx.dijkstra_path_length(GRAFO, origen, destino))


# Métodos para dibujar el grafo en 2D con los nombres de cada nodo
nx.draw(GRAFO, with_labels=True)
plt.show()

# reorder nodes from 0,len(G)-1
# Convertirmos los nodos del grafo en enteros para poder realizar la impresión en 3D
GRAFO_ENTEROS = nx.convert_node_labels_to_integers(GRAFO)


pos = nx.spring_layout(GRAFO_ENTEROS, dim = 3)

xyz = np.array([pos[v] for v in sorted(GRAFO_ENTEROS)])

scalars = np.array(GRAFO_ENTEROS.nodes())+5

mlab.figure(1, bgcolor=(0, 0, 0))
mlab.clf()

# Diseño y presentación del grafo en 3D
pts = mlab.points3d(xyz[:,0], xyz[:,1], xyz[:,2],
                    scalars,
                    scale_factor=0.1,
                    scale_mode='none',
                    colormap='Blues',
                    resolution=20)

pts.mlab_source.dataset.lines = np.array(GRAFO_ENTEROS.edges())
tube = mlab.pipeline.tube(pts, tube_radius=0.01)
mlab.pipeline.surface(tube, color=(0.8, 0.8, 0.8))


# # Método para dibujar el grafo en 3D en una ventana interactiva
mlab.show()
