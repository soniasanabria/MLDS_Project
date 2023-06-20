# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

Total observaciones: 1.713 aunque el paper original habla de 804, se validó base original y también tiene 1.713
Clase fire: 386
Clase no fire: 1.327
Es una base bastante desbalanceada.

![Class distribution](image-3.png)

![Class graphics](image-5.png)

Variables: 

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| NDVI | Índice diferencia normalizada de vegetación | float | 0 - 1| https://github.com/ouladsayadyounes/Wildfires |
| LST | Temperatura de la superficie de la tierra | float | [13.000 - 15.000] | https://github.com/ouladsayadyounes/Wildfires |
| BURNED_AREA | Indicador de anomalías térmicas o existencia de fuego | float | [3,0 - 9,0] | https://github.com/ouladsayadyounes/Wildfires |
| CLASS | Variable objetivo | Categórica | [fire, not fire] | https://github.com/ouladsayadyounes/Wildfires |

- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.

![Variables description](image-6.png)

## Resumen de calidad de los datos

Datos faltantes: 0

![Valores faltantes](image.png)

Filas duplicadas: 275

![Duplicados](image-1.png)

Tratamiento: eliminar filas duplicadas

## Variable objetivo

Variable objetivo desbalanceada
Clase fire: 386
Clase no fire: 1.327

![Variable objetivo](image-2.png)

## Variables individuales

Posibles transformaciones
Variable objetivo: volverla categorica
Variables independientes: escalamiento


