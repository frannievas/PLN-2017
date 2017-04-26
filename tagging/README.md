## Trabajo Práctico 1 - Modelado de Lenguaje

- Francisco Nievas
* frannievas@gmail.com

### Ejercicio 1: Corpus Ancora: Estadísticas de etiquetas POS

- sents: 17378
- total words: 517194
- vocabulary of words: 46501
- vocabulary of taggs: 85


##### Descripción de los taggs
- Adjetivo: a
- Adverbio: r
- Determinante: d
- Nombres: n
- Verbos: v
- Pronombres: p
- Conjunciones: c
- Interjecciones: i
- Preposiciones: s
- Puntuacion: f
- Numerales: z
- Fechas y Horas: W

##### 10 taggs mas frecuentes

 * sp000: *Preposición* Preposición adposición
 * nc0s000: *nombre* Nombre comun singular
 * da0000: *Determinante* Determinante articulo
 * aq0000: *adjetivo* Adjetivo Calificativo
 * fc: *Puntuacion* Puntuación comma
 * np00000: *nombre* Nombre propio
 * nc0p000: *nombre* Nombre comun plural
 * fp: *Puntuación* Puntuación punto
 * rg: *Adverbios* Adverbio general
 * cc: *Conjunciones* Conjuncion coordinada

|   Tagg  | Counts |      percent       |                        Words                        |
| :------ | :----- | :----------------- | :-------------------------------------------------- |
|  sp000  | 79884  | 15.445654821981694 |           ['de', 'en', 'a', 'del', 'con']           |
| nc0s000 | 63452  | 12.268510462225006 |  ['presidente', 'equipo', 'partido', 'país', 'año'] |
|  da0000 | 54549  | 10.547106114920126 |           ['la', 'el', 'los', 'las', 'El']          |
|  aq0000 | 33906  | 6.555760507662502  |   ['pasado', 'gran', 'mayor', 'nuevo', 'próximo']   |
|    fc   | 30147  | 5.8289539321801875 |                        [',']                        |
| np00000 | 29111  | 5.628642250296794  | ['Gobierno', 'España', 'PP', 'Barcelona', 'Madrid'] |
| nc0p000 | 27736  | 5.3627845643994325 |  ['años', 'millones', 'personas', 'países', 'días'] |
|    fp   | 17512  | 3.3859634875887967 |                        ['.']                        |
|    rg   | 15336  | 2.9652316152159535 |       ['más', 'hoy', 'también', 'ayer', 'ya']       |
|    cc   | 15023  | 2.9047127383534996 |           ['y', 'pero', 'o', 'Pero', 'e']           |

| Level of Ambiguity | Counts |                                     Words                                     |
| :----------------- | :----- | :---------------------------------------------------------------------------- |
|         1          | 43972  |    [(',', 30147), ('con', 4150), ('por', 4088), ('su', 3508), ('El', 2817)]   |
|         2          |  2318  |    [('el', 14524), ('en', 12111), ('y', 11212), ('"', 9296), ('los', 7823)]   |
|         3          |  180   |    [('de', 28471), ('la', 18100), ('.', 17519), ('un', 5198), ('no', 3300)]   |
|         4          |   23   |    [('que', 15385), ('a', 8194), ('dos', 917), ('este', 830), ('fue', 730)]   |
|         5          |   5    | [('mismo', 247), ('cinco', 224), ('medio', 105), ('ocho', 75), ('vista', 50)] |
|         6          |   3    |                 [('una', 3852), ('como', 1736), ('uno', 335)]                 |
|         7          |   0    |                                       []                                      |
|         8          |   0    |                                       []                                      |






### Ejercicio2

| Tagg | Counts |      percent       |                          Words                          |
| :--- | :----- | :----------------- | :------------------------------------------------------ |
| sps  | 70141  | 13.559869236316114 |             ['de', 'en', 'a', 'con', 'por']             |
| da0  | 51828  | 10.019544956299335 |             ['la', 'el', 'los', 'las', 'El']            |
| ncm  | 46641  | 9.016778504027885  | ['años', 'presidente', 'millones', 'equipo', 'partido'] |
| ncf  | 40880  | 7.903044644082673  |    ['personas', 'parte', 'vida', 'situación', 'vez']    |
| aq0  | 33904  | 6.554423327127664  |     ['pasado', 'gran', 'mayor', 'nuevo', 'próximo']     |
| vmi  | 30682  | 5.931536589279466  |        ['está', 'tiene', 'dijo', 'puede', 'hace']       |
|  fc  | 30148  | 5.828302102001087  |                          [',']                          |
| np0  | 29113  |  5.62821278677052  |   ['Gobierno', 'España', 'PP', 'Barcelona', 'Madrid']   |
|  fp  | 17513  | 3.3856658721090964 |                          ['.']                          |
|  rg  | 15333  | 2.964221710560656  |         ['más', 'hoy', 'también', 'ayer', 'ya']         |
