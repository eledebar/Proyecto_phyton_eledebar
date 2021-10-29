# Proyecto del Primer Cuatrimestre Fundamentos de Programaciónn (Curso  21/22)
Autor/a: Elena de los Santos Barrera;   uvus:&lt;eledebar&gt;

El proyecto tiene como objetivo analizar los datos de personas diabéticas publicados en el dataset de Kaggle que se puede descargar de la siguiente URL (http://kaggle.com/ishandutta/early-stage-diabetes-risk-prediction-dataset). El dataset original tiene 17 columnas, de las cuales no hay ninguna de tipo fecha, ni de tipo float.
Así que, por una parte, se ha recortado el número de columnas escogiendo solo 2 de las 17 columnas, y se han añadido 6 columnas, las cuales han sido generadas de forma automática, utilizando la herramienta Mockaroo (https://www.mockaroo.com/)
Dos de las columnas generadas son de tipo bool, las cuales devuelven "True" o "False", en en función de si la persona tiene o no una enfermedad concreta. 
Además, se ha añadido otra columna de tipo fecha, que se ha generado con fechas aleatorias y que representa la fecha en la que las diferentes personas obtuvieron su diagnóstico de diabetes.
Tambén se añadieron columnas para recoger el peso en kilogramos (float) y la altura en centímetros (int) de las personas estudiadas.
Por último, se ha añadido una columna de tipo str para registrar la frecuencia con la que practican actividad física los sujetos.          



## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **diabetes.py**: Contiene funciones para enalizar los datos sobre personas diabéticas.
    * **diabetes_test.py**: Contiene funciones de test para probar las funciones del módulo `diabetes.py`. En este módulo está el main
    * **parsers.py**: Contiene funciones de parseo de datos.
* **/data**: Contiene el dataset o datasets del proyecto
    * **dataset_diabetes.csv**: Archivo con los datos de personas diabéticas.
        
## Estructura del *dataset*

Cada fila del dataset recoge los datos anonimizados de una persona, es decir, no sabemos sus nombre ni sus apellidos. Para cada persona se registran 8 datos. Por lo tanto, el dataset está compuesto por 8 columnas, con la siguiente descripción:

* **Age**: de tipo int, representa la edad de la persona.
* **Gender**: de tipo str, representa el género de la persona.
* **Heart_disease**: de tipo boolean, representa si es el paciente diabético sufre o no de enfermedad del corazón. Esta columna se ha generado automáticamente.
* **Thyrod_disease**: de tipo boolean, representa si es el paciente diabético sufre o no de enfermedad de tiroides. Esta columna se ha generado automáticamente.
* **Centimetres_high**: de tipo int, representa la altura del paciente en centímetros. Esta columna se ha generado automáticamente.
* **Kilograms_weight**: de tipo float, representa el peso del paciente en kilos. Esta columna se ha generado automáticamente.
* **fecha_ultimo_trabajo**: de tipo date, representa la fecha del diagnóstico de diabetes que tuvo el paciente. Esta columna se ha generado automáticamente.

## Tipos implementados

Para trabajar con los datos del dataset se ha definido la siguiente tupla con nombre:

 `tupla = Info(int(Age), Gender, parsing_boolean (Heart_disease), parsing_boolean(Thyroid_disease), int(Centimetres_high), float(Kilograms_weight), \
                         parsing_date(Date_of_diagnosis), Physical_activity)`

en la que los tipos de cada uno de los campos son los siguientes:

`Info(int, str, boolean, boolean, int, float, str, str, in, boolean, int,vdatetime.date, str)`


## Funciones implementadas
En este proyecto se han implementado las siguientes funciones, que están clasificadas según los bloques y tipos de funciones que se requieren en cada una de las entregas.
El módulo principal es el módulo diabetes.py, así que aquí es donde se hará referencia a cada uno de los bloques de las entregas.
### Módulo diabetes

#### Entrega 1

* **Bloque 0**  
  * **lee_fichero(fichero)**: lee los datos del fichero csv y devuelve una lista de tuplas de tipo Info con los datos del fichero. Para implementar esta función se han definido las siguientes funciones auxiliares en el [módulo `parsers`](#módulo-parsers):
    * **parsea_booleano(cadena)**: Función para convertir de cadena a booleano.
    * **parsea_fecha(cadena)**: Función para convertir de cadena a fecha.   
