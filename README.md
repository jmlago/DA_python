# Data Analysis in Python SEA/UAB course 2017/2018 (EN)
This is a course promoted by the SEA and UAB, to share Python and Data Analysis knowledge with scientific community.
Is important to notice that this is an introductory course.

## Phylosophy of the course:
This course is about learning the basics of Python and also to learn a couple of mathematical and statistical techniques to deal with the data, with the objective of extracting information from the data.
The aim is not to go deep into the mathematical representations of all the models but on the applications of those models with Python.

## Here are the instructions to follow the course:
To follow the course you need to download the material from this web-page. The slides, other PDFs and also the code.

## Prerequisites:

The student must know basics about computers and programming, and also a little bit of maths and statistics is recommendable.

## Installing:

To install the environment related necessary for the course, you can find the information in the slides.
Also if you are familiar with Python and other languages, for this course we will use:
* [Anaconda](https://www.anaconda.com/download/) - The main enviroment

### Deep learning libraries (Mx-Net):
Here is an example of how to install mxnet, which is one of the best DL frameworks, for this we will execute the following commands (just for windows users) in  the `AnacondaPrompt`:

```
conda create --name mxnet
source activate mxnet
pip install mxnet
```

**For linux users (I didn't tested in OSX)**
```
sudo apt-get install libatlas-base-dev
```

**If you are not using Windows or you want GPU support (only CUDA)**
Go to the following link and choose your OS and your requirements, after that follow the commands (also try to include the conda environments as in the Windows example):
* [Mx-Net](https://mxnet.incubator.apache.org/install/index.html) - The DL framework installation guide

To check if everything is working:
* Open `Spyder` and tip:
```
import mxnet as mx
from mxnet import nd
mx.random.seed(1)


x = nd.ones((3, 4))
y = nd.random_normal(0, 1, shape=(3, 4))
print(x)
print(y)
print(x + y)
```
* Check yourselves if the results are correct. If you are having issues, you can send me an e-mail via SEA

### Deep learning libraries (Others):
If you are interested in deep learning world, and you want also to install other deep learning frameworks (majority of them are just available in Linux), you can take a look at:
* [Tensorflow](https://www.tensorflow.org/install/) - Tensorflow installation guide
* [Pytorch](http://pytorch.org/) - Pytorch installation commands
We will discuss that during the course.

## Contents of the course:
I hope that we can do all this content:

### Aerial perspective of DA:
Basic concepts of Data Analysis and Python. A global view of the environment... (`Anaconda`, `Spyder` and other IDEs, `basic commands`, ...)

### Data gathering:
This will be teached maybe during the last sessions, because of complexity with regexs and web scrapping... (`BeautifulSoup`, `requests`, ...)

### Exploratory analysis and cleaning:
With real data, understand how to prepare the data, and how to do visualizations... (`numpy`, `pandas`, `matplotlib`, ...)

### Algorithm Selection:
We will see some algorithms of data analysis, like SVD and clustering algorithms... (theoretical concepts, `scikit-learn`, `scipy`, ...)

### Performance Engineering:
When we work with big amounts of data, or with complex algorithms or functions, we need to know how we can speed up our code... (`numba`, `mxnet`, ...)

### Deep Learning:
A tiny view of the deep learning world... (NN (possible CNN),`mxnet`, ...)

___

# Análisis de datos en Python SEA/UAB, curso 2017/2018 (ES)
Este es un curso promovido por el SEA y la UAB, para compartir conocimientos de Python y Análisis de datos con la comunidad científica.
Es importante entender que este es un curso introductorio.
## Filosofía del curso:
Este curso esta orientado a aprender los conceptos básicos de Python y también de aprender un par de técnicas matemáticas y/o estadísticas para tratar con los datos, con el objetivo de extraer información de los mismos.
El objetivo no es profundizar en las representaciones matemáticas de todos los modelos, sino en las aplicaciones de dichos modelos con Python.

## Como seguir el curso:
Para seguir el curso, se debe descargar el material de esta página web. Las diapositivas, otros archivos PDF y también el código.
## Prerrequisitos:

El estudiante debe saber lo básico sobre computación y programación, y también es recomendable un poco de matemáticas y estadística.

## Instalación:
Para instalar el entorno de Python que vamos a necesitar durante el curso, podemos encontrar la información en las diapositivas.
Si estamos familiarizados ya con Python y otros lenguajes, y queremos instalar ya el entorno:

* [Anaconda](https://www.anaconda.com/download/) - El entorno principal

### Librerías de Deep Learning (Mx-Net):

Aquí hay un ejemplo de cómo instalar mxnet, que es uno de los mejores frameworks de DL, para esto ejecutaremos los siguientes comandos (solo para usuarios de Windows) en el `AnacondaPrompt`:

```
conda create --name mxnet
source activate mxnet
pip install mxnet
```
**Para los usuarios de linux (no lo he probado con OSX)**
```
sudo apt-get install libatlas-base-dev
```

**Si no vamos a usar Windows o queremos soporte para GPU (solo CUDA)**
Iremos al siguiente enlace y elegiremos nuestro sistema operativo y sus requisitos, luego seguiremos los comandos (también intentaremos incluir el entorno `conda` como en el ejemplo de Windows):
* [Mx-Net](https://mxnet.incubator.apache.org/install/index.html) - The DL framework installation guide

Para verificar que todo funciona:
* Abrimos `Spyder` y escribimos:
```
import mxnet as mx
from mxnet import nd
mx.random.seed(1)


x = nd.ones((3, 4))
y = nd.random_normal(0, 1, shape=(3, 4))
print(x)
print(y)
print(x + y)
```
* Podemos comprobar si los resultados son correctos. Si tenéis problemas, podéis enviarme un correo electrónico a través del SEA

### Librerías de Deep Learning (Otros):
Si estáis interesados en el mundo del aprendizaje profundo y también deseáis instalar otros frameworks de aprendizaje profundo (la mayoría de ellos solo están disponibles en Linux), podéis consultar:
* [Tensorflow](https://www.tensorflow.org/install/) - Tensorflow guía de instalación
* [Pytorch](http://pytorch.org/) - Pytorch comandos para instalar

Discutiremos esto durante el curso.

## Indice del contenido del curso
Espero que podamos hacer todo este contenido:

### Perspectiva general del DA:
Conceptos básicos del Data Analysis en Python. Un punto de vista global del entorno... (`Anaconda`, `Spyder` y otros IDEs, `comandos básicos`, ...)

### Extracción de datos:
Estudiaremos esto probablemente en una fase avanzada del curso, debido a la complejidad de las regexs y del web scrapping... (`BeautifulSoup`, `requests`, ...)

### Análisis explicativo y limpieza de datos:
Con datos reales previamente recojidos, entender como preparar los datos y como visualizarlos... (`numpy`, `pandas`, `matplotlib`, ...)

### Algoritmos del DA:
Veremos algunos algoritmos del data analysis, como SVD y algún algoritmo de clustering... (conceptos teóricos, `scikit-learn`, `scipy`, ...)

### Incrementando el rendimiento:
Cuando trabajamos con muchos datos, o con algoritmos que contienen funciones complejas a nivel de computación, por tanto necesitamos saber como acelerar nuestro código... (`numba`, `mxnet`, ...)

### Deep Learning (aprendizaje profundo):
Una pequeña visión del mundo de las redes neuronales... (NN (puede que CNN),`mxnet`, ...)


___

## Authors:

* **José María Lago** - *Entire page* - [JM](https://github.com/jmlago)

## License:
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">licencia de Creative Commons Reconocimiento-NoComercial 4.0 Internacional</a>.
