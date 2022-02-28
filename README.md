# _*Prueba_stech*_
En este repositorio, dejo subida la prueba técnica de Stech, una descripción de la instalación y uso.

## _*Instalación de Python y git*_:
- Se deberá instalar python: para ello, ingresaremos en el link "https://www.python.org/" y descargaremos la versión más actual (al momento de crear este proyecto, se utilizó python 3.10).
- Se deberá instalar git. Para ello ingresaremos en "https://git-scm.com/" y descargaremos la última versión compatible con nuestro procesador.

## _*Clonación del proyecto*_:
Dentro del disco "C" hacer click derecho y seleccionar "gitbash here" y ejecutar el siguiente comando:
- git clone https://github.com/nicolaspablocordoba/Prueba_stech.git

## _*Librerías necesarias*_:
Para poder ejecutar el proyecto, se deberán instalar las siguientes librerías desde la consola de Windows. Para ello, abriremos inicio, escribiremos "CMD" y abriremos la consola del sistema. Luego, procederemos a ejecutar los siguientes comandos:
- pip install selenium
- pip install html-testRunner
- pip install webdriver-manager

## _*Ejecutar los test*_:
Para poder correr el archivo que contiene los test, según el orden pedido, se deberá ingresar en la ruta "C:\Prueba_stech\Test" y ejecutar el archivo "Suite_test_netflix". Si la instalación se realizó de manera correcta, se abrirá una consola de windows que dirá "Running Test" y comenzará a abrirse la ventana del navegador chrome.

Una vez finalizados todos los test, la consola se cerrará y en la carpeta "Reports" se creará un archivo llamado "Reporte NetflixTest", el cual contendrá un reporte de los test corridos y en caso de que lo amerite el test, mostrará en el botón "View" el texto que haya generado el test.
