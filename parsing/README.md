# Trabajo Práctico 3 - Análisis Sintáctico

- Francisco Nievas

## Ejercicio 1: Evaluación de Parsers

### **Reportes**

#### *Flat* Trees
```
Model: Flat
Parsed 1444 sentences
Labeled
  Precision: 99.93%
  Recall: 14.58%
  F1: 25.44%
Unlabeled
  Precision: 100.00%
  Recall: 14.59%
  F1: 25.46%

real 6.45
user 6.28
sys 0.46
```

#### *Rbranch* Trees
```
Model: Rbranch
Parsed 1444 sentences
Labeled
  Precision: 8.81%
  Recall: 14.58%
  F1: 10.98%
Unlabeled
  Precision: 8.88%
  Recall: 14.69%
  F1: 11.07%
real 7.42
user 7.15
sys 0.60
```

#### *Lbranch* Trees
```
Model: Lbranch
Parsed 1444 sentences
Labeled
  Precision: 8.81%
  Recall: 14.58%
  F1: 10.98%
Unlabeled
  Precision: 14.71%
  Recall: 24.35%
  F1: 18.34%
real 7.01
user 7.01
sys 0.30
```
