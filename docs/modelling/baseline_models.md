# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

Neural networks, naïve bayes, SVM, and random forests, have been already applied to develop predictive models of fire occurrence based on satellite data (https://www.sciencedirect.com/science/article/abs/pii/S0379711218303941#:~:text=Multiple%20algorithms%20can%20be%20used,occurrence%20based%20on%20satellite%20data.)

El paper tomado como referencia usó:
Neural networks - MLP classifier con 21 parámetros
SVM - con 14 parámetros

## Variables de entrada

NVDI - Índice diferencia normalizada de vegetación 
LST - Temperatura de la superficie de la tierra
Burned area - Indicador de anomalías térmicas o existencia de fuego

## Variable objetivo

Class: con dos posibles valores, existencia de incendio forestal o no existencia de incendio forestal

## Evaluación del modelo

### Métricas de evaluación

Matriz de confusión 

### Resultados de evaluación

An average of 117 instances out of total 119 instances of the class “fire” is found to be correctly classified using “NN”, while SVM managed to predict 116 fire instances out of 119 accurately.

![Alt text](image.png)

![Alt text](image-1.png)

## Análisis de los resultados

Fortaleza: alta precisión
Debilidad: dataset con pocas observaciones

## Conclusiones

Predice adecuadamente la existencia de incendio forestal, la mayor desviación puede darse en que prediga existencia de fuego cuando no, pero este sería el menor de los riesgos.

![Alt text](image-2.png)

## Referencias

Paper: (https://www.sciencedirect.com/science/article/abs/pii/S0379711218303941#:~:text=Multiple%20algorithms%20can%20be%20used,occurrence%20based%20on%20satellite%20data.)
