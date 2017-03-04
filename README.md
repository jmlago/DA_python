# Data Analysis in Python SEA/UAB course 2016/2017
This is a course promoted by the SEA and UAB, to share Python and Data Analysis knowledge with scientific community.
Is important to notice that this is an introduction course.
___
Este curso esta promovido por el SEA y la UAB, el objetivo es compartir los conocimientos tanto de Python como de Data Analysis con la comunidad científica.
## Phylosophy of the course:
This course is about learning the basics of Python and also to learn a couple of mathematical and statistical techniques to deal with the data, with the objective of extracting information from the data.
The aim is not to go deep into the mathematical representations of all the models but on the applications of those models with Python.
___
La idea de este curso es aprender a grandes rasgos como usar Python, y también una buena batería de modelos matemáticos y estadísticos para poder extraer la información necesaria a partir de los datos.
El objetivo no es profundizar en las representaciones matemáticas de los modelos, pero si entender su aplicación y poder usarlos con agilidad mediante Python.
## Here are the instructions to follow the course:
To follow the course you need to download the material from this web-page. The slides and also the code.
___
Para seguir el curso, debéis descargar todo el material desde esta misma página. Las transparencias y también el código.

### Prerequisites:

The student must know basics about computers and programming, and also a little bit of maths and statistics is recommendable.
___
El estudiante debe tener conocimientos básicos sobre ordenadores y programación, y es recomendable tener conocimientos básicos sobre  matemáticas y estadística.

### Installing:

To install the environment related necessary for the course, you can find the information in the slides.
Also if you are familiar with Python and other languages, for this course we will use:
* [Anaconda](https://www.continuum.io/downloads) - The main enviroment

#### For those who want deep learning libraries:
Here is an example of how to install tensorflow and theano, which are 2 of the most used libraries in the world in terms of deep learning, for both libraries we need to have python3.5 by now so execute the following commands in AnacondaPrompt as admin (or as sudoer in Linux systems):
```
conda install python=3.5
```
##### Tensorflow:
Try it if it works in a particular enviroment and see if something is broke with this commands:
```
conda create -n tensorflow
activate tensorflow
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-1.0.0-cp35-cp35m-win_x86_64.whl
```
And if your computer is x64 then replace the last command with:
```
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-1.0.0-cp35-cp35m-win_amd64.whl
```
This are the commands to install the CPU version (not GPU), if you want the complete information look at:
* [Install tensorflow](https://www.tensorflow.org/install/install_windows) - installation pseudo-guide

Then open a local python in the same AnacondaPrompt with:
```
python
>>> import tensorflow as tf
```
And try if all is working ok.
Then you can install tensorflow with the same pip command without an specific environment called tensorflow so, just open the AnacondaPrompt as admin and execute:
```
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-1.0.0-cp35-cp35m-win_x86_64.whl
```
##### Theano:
Just need to open the AnacondaPrompt as admin and execute the following, after DOWNGRADING to python 3.5:
```
conda install theano
```

___
Para instalar el entorno necesario para el curso, debéis mirar en las transparencias.
También, para los que sois familiares con Python y otros lenguajes de programación, para este curso, usaremos:
* [Anaconda](https://www.continuum.io/downloads) - EL entorno principal

## Authors:

* **José María Lago** - *Entire page* - [JM](https://github.com/jmlago)
