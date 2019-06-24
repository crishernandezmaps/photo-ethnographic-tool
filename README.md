#  Herramienta para el procesamiento y georeferenciación de imágenes recolectadas en trabajo etnográfico de campo <sup>[1](#foot01)</sup>

## Índice
- [Presentación](https://github.com/crishernandezmaps/photo-ethnographic-tool#presentación)
- [Objetivo](https://github.com/crishernandezmaps/photo-ethnographic-tool#objetivo)
- [Desarrollo](https://github.com/crishernandezmaps/photo-ethnographic-tool#desarrollo)
- [Alcances](https://github.com/crishernandezmaps/photo-ethnographic-tool#alcances)
- [Aspectos técnicos](https://github.com/crishernandezmaps/photo-ethnographic-tool#aspectos-técnicos)
    - [Lenguaje y Librerías](https://github.com/crishernandezmaps/photo-ethnographic-tool#lenguaje-y-librer%C3%ADas)
    - [Instalación Local](https://github.com/crishernandezmaps/photo-ethnographic-tool#instalación-local)
- [Versión Web](https://github.com/crishernandezmaps/photo-ethnographic-tool#versión-web)


## Presentación
Esta herramienta es parte del trabajo realizado durante el segundo semestre del año 2018 y el primer semestre del año 2019, en el marco del proyecto FONDECYT Nº 1171554 "Prácticas de intervenir y habitar el territorio: develando el conocimiento urbano situado” (Jiron, Mansilla, Lange, Imilan, 2017).

El [Instituto de la Vivienda de la Facultad de Arquitectura y Urbanismo](https://vivienda.uchilefau.cl/) de la [Universidad de Chile](http://www.uchile.cl/), ha creado para el proyecto Fondecyt Situado una herramienta de código abierto para el procesamiento de imágenes y la extracción y agregación de [metadata](https://es.wikipedia.org/wiki/Metadatos).

La siguiente herramienta esta creada pensando en las necesidades de procesamiento de imágenes recolectadas en trabajo de campo etnográfico. Se busca a través de esta pieza de software que los investigadores centren sus capacidades mas en la observación experta y menos en el procesamiento de datos, especialmente fotografías. 

Las fotografías representan en el trabajo de campo etnográfico una fuente muy rica de información, la cual por su inmediatez y sencillez en el rescate a través de teléfonos móviles, incrementa la capacidad narrativa y la profundidad de las observaciones. Asimismo, los sensores con los que cuenta un teléfono móvil entrega información adicional a la imagen, como fecha y hora de la captura y localización (coordenadas). 

Las coordenadas en particular permiten adherir otra componente relevante al análisis etnográfico, que es la espacialidad. El poder agregar el lugar al trabajo de campo, involucra distinciones para la identificación de patrones geográfico-culturales, indispensables para el estudio de lo urbano.

De especial interés también fue a la hora del desarrollo de esta herramienta, es la capacidad de agregar metadata adicional a las fotografías, lo que permite clasificarlas y generar diversos análisis adicionales.   

El objetivo de la herramienta es la lectura de las fotografías alojadas localmente en el computador del investigador, la extracción de la metadata tanto [Exif](https://es.wikipedia.org/wiki/Exchangeable_image_file_format) como [Iptc](https://iptc.org/standards/photo-metadata/).

## Objetivo
El trabajo de experimentación realizado buscó responder a la problemática sobre cuáles herramientas de uso libre y gratuito están disponibles para ser usadas o transformadas en dispositivos que facilitasen la labor investigativa etnográfica en terreno. En este sentido, la labor del equipo se volcó a sestear diversas tecnologías, ya sea brindándoles un nuevo uso (al que originalmente tienen) o desarrollando en diversos lenguajes de programación, herramientas propias.

## Desarrollo
El desarrollo se basó en usar el insumo fotográfico, principalmente. Estas fotografías fueron procesadas por el equipo para agregar etiquetas a la metadata de la foto. Estas imágenes fueron rescatadas por el equipo en terreno con sus teléfonos celulares, con la salvedad que siempre debiese el GPS del móvil estuviera encendido. 

La metadata de las imágenes fue extraída utilizando el lenguaje de programación Python (3.6). Así como también diversas librerías adicionales. De esta forma, la metadata contenida en la IPTC info de cada foto, fue extraída de forma automatizada. Las variables extraídas fueron las siguientes:
	
- Etiquetas agregadas por el equipo
- Time Stamp
- Coordenadas de la posición donde fue tomada la foto.

Esta información permitió construir una visualización tanto de los puntos en un mapa donde las imágenes fueron tomadas como de las categorías a la que pertenecía cada imagen. Esto ya que las etiquetas agregadas por el equipo permitieron generar un menu que clasifica las imágenes. De esta forma, se agrupan de acuerdo a lo que el/la investigador(a) consideró que representaba dicha foto en terreno.

## Alcances
El alcance de esta experimentación en humanidades digitales (mezclar disciplinas sociales con ciencias de la computación), implica que desde este desarrollo, por su carácter de código abierto, pueden surgir nuevos desarrollos y mejoras, ya no solamente llevados adelante por el equipo original de este proyecto, sino que por cualquier investigador alrededor del mundo. Dicho alcance, permite que la investigación social, a través del lenguaje común internacional de la programación de software, pueda expandir su quehacer de forma global.

## Aspectos técnicos
### Lenguaje y Librerías
Esta herramienta esta desarrollada en el lenguaje de programación [Python](https://www.python.org/) (versión 3.6.4). Las librerías utilizadas son:
- Click==7.0
- Flask==1.0.3
- geojson==2.4.1
- gunicorn==19.9.0
- IPTCInfo3==2.0.3 <sup>[2](#foot02)</sup>
- itsdangerous==1.1.0
- Jinja2==2.10.1
- MarkupSafe==1.1.1
- Pillow==6.0.0
- Werkzeug==0.15.4

### Instalación Local
Para poder utilizar la aplicación debes contar con Python3, Git y Github. Aquí instrucciones para la instalación en MacOS, Linux y Windows. En el procesamiento local es posible procesar cientos de imagenes al mismo tiempo.

#### Python3
Siempre y cuando no se tenga instalado ya Python3, se recomienda la instalación de Python3 mediante el Software Anaconda: https://www.anaconda.com/distribution/ (Python 3.7 version). Presionando el boton *Download* se descargará un ejecutable. Desde aquí la instalación es como cualquier otro programa.

- Instalar Anaconda en MacOs: https://www.youtube.com/watch?v=nVlrpNf3EdM
- Instalar Anaconda en Linux (Ubuntu): https://www.youtube.com/watch?v=DY0DB_NwEu0 
- Instalar Anaconda en Windows: https://www.youtube.com/watch?v=52h3r_lROGY (Video)

#### Git
[Git](https://git-scm.com/downloads) es un sistema de versionado de código que nos permite construir software de forma colaborativa. Se puede encontrar el descargable para instalar en los tres sistemas operativos antes mencionados, aquī: https://git-scm.com/downloads

#### Github
Github es un servicio que aloja Git. En Github podemos realizar versionado de código en līnea. Solo requiere contar con una cuenta de usuario y activación por parte del usuario: https://github.com.

#### Instalación
Ejecutar los siguientes comandos en terminal/shell/command prompt:
- git clone https://github.com/crishernandezmaps/invi_app.git
- cd invi_app
- pip install -r requirements.txt
- export FLASK_APP=app.py
- export FLASK_ENV=development
- flask run
- La app se desplegará en el puerto http://127.0.0.1:5000/ (visita esta dirección en tu Browser - Safari, Firefox, Chrome)

## Versión Web
Se ha realizado un deployment en la nube de la herramienta para su testeo. Se debe probar de la siguiente manera:
- Visitar https://invi-app.herokuapp.com 
- Subir imágenes (se recomienda un máximo de 5 si las imagenes pesan mas de 2MB).
- Presionar *upload* y esperar por el resultado.
- El resultado es un archivo del tipo GeoJson, el cual puede ser copiado y pegado a http://geojson.io para su visualización.
- Una vez visualizado puede ser descargado desde *geojson.io* en formato **CSV** y guardado localmente en el computador.
- Visitar **CARTO** (https://carto.com) y subir una nueva **base de datos** o **dataset**.
- Una vez que se ha subido el archivo CSV, se podrá visualizar como un mapa dinámico, el cual se puede visitar en una url. Como este mapa de ejemplo: https://crishmill.carto.com/builder/ec6d7456-5954-4dd9-ab0a-84a8a834693b 


---
<a name="foot01">(1)</a> Elaborado por [Cris Hernández](http://crishernandez.co), Geógrafo, Universidad de Chile. Junio del 2019.<br/>
<a name="foot02">(2)</a> Para instalar IPTCinfo3
* Descargar o clonar repo https://github.com/crccheck/iptcinfo3
* Para evitar los numerosos Warning (si esto ocurriera): https://stackoverflow.com/questions/50407738/python-disable-iptcinfo-warning (opcional)
* cd en iptcinfo3
* Modificar iptcinfo3.py y setup.py por el shebang adecuado si utilizas Python3: #!/usr/bin/env python3 (opcional)
* Finalmente python3 setup.py install