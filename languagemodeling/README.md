### Trabajo Práctico 1 - Modelado de Lenguaje

- Francisco Nievas
* frannievas@gmail.com

#### Ejercicio 1: Corpus

Como corpus en lenguaje natural se utilizó los textos de los libros de [Game_of_Thrones](https://en.wikipedia.org/wiki/Game_of_Thrones) en español.
Como "corpus reader" se utilizó `PlaintextCorpusReader` de la libreria [nltk](http://www.nltk.org/_modules/nltk/corpus/reader/plaintext.html), junto a `RegexpTokenizer` que permite utilizar una expreción regular para poder tokenizar y segmentar las oraciones.

La siguiente es la expreción regular que se utilizo:
```python
# pattern = r'''(?ix)    # set flag to allow verbose regexps
#       (?:sr\.|sra\.)
#     | (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
#     | \w+(?:-\w+)*        # words with optional internal hyphens
#     | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
#     | \.\.\.            # ellipsis
#     | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
# '''
```
Se procedió a verificar la correcta segmentación, y no hubo necesidad de cambiar la expreción para corregir algun defecto.

#### Ejercicio 2: Modelo de n-gramas

Se implementó un modelo de n-gramas con marcadores de comienzo y fin de oración (< s > y < /s > ) utilizando como base la estructura provista por la cátedra.
El modelo de n-gramas hace una suposición de Markov de nivel n-1.

#### Ejercicio 3: Generación de Texto

Se implementó una clase `NGramGenerator` que genera oraciones del lenguaje natural. Para ello recibe como parámetro un modelo entrenado y luego para generar las oraciones posee un método `generate_sentence` que utiliza a `generate_token` para generar palabras hasta que el marcador de fin de oración es generado.

Para elegir las palabras aleatorias se utiliza el método de la [transformada inversa](https://en.wikipedia.org/wiki/Inverse_transform_sampling)


###### Palabras generadas:

###### Unigrama (N = 1)
```
comida señores burla , un blanca está . . Nido
lobos golpes decidido Meñique
Somos tienes el catorce la en al fracasos bebé Ser malcríes a Cuatro , Caballero manchadas
```
###### Bigrama (N = 2)
```
Lord Tywin era un poco .
Por encima de los dedos de Lannister .
Muy bien la Guardia de hielo podrido ; Timoth me hiciera , sospechó que dar con las brumas .

```

###### Trigrama (N = 3)
```
No ... no hay vela que ardía con una orden .
Ser Kevan viene a despertarme . Alteza intervino Ser Kevan estaba frío .
suficiente para mantenerlo caliente .

```

###### 4-Grama
```
Siento haberte pegado aquella vez dijo .
Aunque más valdrá que les guarde el dinero hasta que volvamos a Tyrosh .
Si encuentras pruebas ... dijo , con la maraña de cicatrices que había perdido media oreja .
```
###### 5-Grama
```
Tenían que estar locos para acercarse tanto a Invernalia .
Sam no sabía qué podría resultar peor : que lo reconociera un enemigo de su señor padre .
Puedo prometer que no serás molestada por visitantes no deseados .

```

#### Ejercicio 4: Suavizado "add-one"

Se implemento el método de suavizado "add-one" [(*laplace* smoothing)](https://en.wikipedia.org/wiki/Additive_smoothing) el cual consiste en "repartir" las probabilidades de que ocurran ciertas n-gramas en nuestro modelo para evitar tener una masiva cantidad de ceros.


#### Ejercicio 5: Evaluación de Modelos de Lenguaje
