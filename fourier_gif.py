import numpy as np
import matplotlib.pyplot as plt
import os
import imageio

t = np.linspace(0, 4 * np.pi, 400)

n = 100

path = os.path.abspath(os.path.dirname(__file__))
png_dir = path+'/imgs'
if not os.path.isdir(path+'/imgs'):
    os.mkdir(path+'/imgs')
    print('created')
else:
    print('already have it')

# Função que queremos plotar. Isso aqui é o resultado da onda quadrada
# Function we are going to plot. This one in particular is the Square Wave
def f(i, x):
    return (4 / np.pi) * np.sin(i * x) / i


for k in range(1, n):
    x = 0
    plt.clf()
    for i in range(1, 2 * k, 2):
        x = x + f(i, t)
    nome = str(k) + '.png'
    plt.plot(t, x)
    plt.grid()
    plt.xlim(0, 2 * np.pi)
    plt.ylim(-1.5, 1.5)
    plt.title(f'Evolution of the Fourier Series for the "square wave" \n from 1 to {k+1} terms')
    plt.savefig('imgs/' + nome)

last = nome


# Faz gif:
images = []
nomes = []

# Tira o .png dos nomes das imagens /// Removes .png from the images inside ./imgs
for file_name in os.listdir(png_dir):
    nomes.append(file_name[:-4:1])

# Transforma o nome das imagens (string com um numero) em ints///
# Transform image names from strings to ints (they are all numbers)
namelist = []
for nome in nomes:
    namelist.append(int(nome))


# Sorta a lista de inteiros criada aqui em cima, transforma tudo em string e adiciona '.png' no final
# Sorts the list of integers created above, re-strings it, and adds .png
nome_real = []
for num in sorted(namelist):
    nome_real.append(str(num) + '.png')

# Usando a lista de imagens sortadas, cria o gif.
# Creates the .gif
for nome in nome_real:
    if nome in os.listdir(png_dir):
        file_path = os.path.join(png_dir, nome)
        if nome == last:
            for i in range(15):
                images.append(imageio.imread(file_path))
        else:
            images.append(imageio.imread(file_path))
imageio.mimsave(path+'/square_wave.gif', images, duration='0.1')
