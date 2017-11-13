# Data Analysis in Python SEA/UAB course 2017/2018
This is a course promoted by the SEA and UAB, to share Python and Data Analysis knowledge with scientific community.
Is important to notice that this is an introductory course.
___
Este curso esta promovido por el SEA y la UAB, el objetivo es compartir los conocimientos tanto de Python como de Data Analysis con la comunidad científica. Es importante tener en cuenta que es un curso introductorio.

## Phylosophy of the course:
This course is about learning the basics of Python and also to learn a couple of mathematical and statistical techniques to deal with the data, with the objective of extracting information from the data.
The aim is not to go deep into the mathematical representations of all the models but on the applications of those models with Python.
___
La idea de este curso es aprender a grandes rasgos como usar Python, y también una buena batería de modelos matemáticos y estadísticos para poder extraer la información necesaria a partir de los datos.
El objetivo no es profundizar en las representaciones matemáticas de los modelos, pero si entender su aplicación y poder usarlos con agilidad mediante Python.
## Here are the instructions to follow the course:
To follow the course you need to download the material from this web-page. The slides, other PDFs and also the code.
___
Para seguir el curso, debéis descargar todo el material desde esta misma página. Las transparencias, PDFs y también el código.

### Prerequisites:

The student must know basics about computers and programming, and also a little bit of maths and statistics is recommendable.
___
El estudiante debe tener conocimientos básicos sobre ordenadores y programación, y es recomendable tener conocimientos básicos sobre  matemáticas y estadística.

### Installing:

To install the environment related necessary for the course, you can find the information in the slides.
Also if you are familiar with Python and other languages, for this course we will use:
* [Anaconda](https://www.continuum.io/downloads) - The main enviroment

#### For those who want deep learning libraries:
**Is important that deep learning libraries just work under Unix systems (Linux and OS)**
Here is an example of how to install pytorch, which is one of the most used libraries in the world in terms of deep learning, for this library we need to have python3.6 by now so execute the following commands:
```
conda install python=3.6
```
##### PyTorch:
Try it if it works in a particular enviroment and see if something is broke with this commands:
```
conda create --name pytorch
source activate pytorch
conda install pytorch torchvision -c soumith
```

This are the commands to install the CPU version (not GPU), if you want to install pytorch with GPU support:
```
conda install pytorch torchvision cuda80 -c soumith
```
instead of:
```
conda install pytorch torchvision -c soumith
```

* [PyTorch](http://pytorch.org/) - initial pytorch page

Then open a local python in the same AnacondaPrompt with:
```
python
>>> import torch
```
And try if all is working ok.

##### Tensorflow of Windows users
For Windows users, that can not install pytorch, you can try to install tensorflow, following this guide:
* [Install Tensorflow on Windows](https://www.tensorflow.org/install/install_windows)
___
Para instalar el entorno que vamos a usar durante el curso, usaremos el material que se proporciona en las diapositivas.
Para los que tengáis experiencia con Python y con otros lenguajes parecidos, durante el curso usaremos:
* [Anaconda](https://www.continuum.io/downloads) - The main enviroment

#### Para los que queráis librerías de Deep Learning:
**Es importante saber que la mayoria de entornos de deep learning actualmente solo están soportados por sistemas Unix (Linux y OS)**
Una posible forma de instalar pytorch, que es una de las librerías de deep learning mas usadas actualmente, es ejecutando los siguientes comandos:
```
conda install python=3.6
```
##### PyTorch:
Primero crearemos un entorno virtual para probar que nada que instale pytorch rompa alguna de las dependencias entre librerías:
```
conda create --name pytorch
source activate pytorch
conda install pytorch torchvision -c soumith
```
Estos son los comandos para instalar Pytorch (CPU), si queremos la versión de GPU, tendremos que ejecutar:
```
conda install pytorch torchvision cuda80 -c soumith
```
en lugar de:
```
conda install pytorch torchvision -c soumith
```

* [PyTorch](http://pytorch.org/) - Pagina de PyTorch

Para revisar que lo tenemos instalado:
```
python
>>> import torch
```
Y podemos probar un pequeño ejemplo para ver que funciona correctamente.

##### Tensorflow para usuarios de Windows:
Para los que usáis windows, y que no podáis instalar pytorch, podéis seguir la siguiente guía para instalar tensorflow:
* [Instalar Tensorflow en Windows](https://www.tensorflow.org/install/install_windows)

## Authors:

* **José María Lago** - *Entire page* - [JM](https://github.com/jmlago)

## License:
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">licencia de Creative Commons Reconocimiento-NoComercial 4.0 Internacional</a>.
