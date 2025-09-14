# Sistemas_De_Informacion

Power BI:

DAX 2:

```
Stock = SUM(productos[stock_actual])
```

DAX 2:

```
Ranking Productos = 
RANKX(
    ALL(productos[nombre_producto]),  -- Calcula el ranking de todos los productos sin filtros
    [Stock],                   -- Usa el otro DAX
    ,                          
    DESC,                      -- Orden descendente 
    DENSE                     
)
```


---

<img width="1083" height="620" alt="image" src="https://github.com/user-attachments/assets/4571f66f-025f-4582-a782-2e3f8f5d8074" />



Tableou:


Calculated field 2:
```
SUM([stock_actual])
```

<img width="767" height="821" alt="image" src="https://github.com/user-attachments/assets/63a21082-1c5d-4c2b-a62a-40feb4c274a0" />



3:


Power BI:

DAX:
```
Ventas Totales = SUM(ventas_techstore[cantidad])
```

<img width="1057" height="615" alt="image" src="https://github.com/user-attachments/assets/f9bb0b4e-efe4-41fb-905f-d091b48bc3a2" />




Calculated Field:

```
SUM([venta_total])
```


<img width="372" height="193" alt="image" src="https://github.com/user-attachments/assets/688047e1-209e-4016-982e-04710e13c67e" />



POWER BI:

DEX:

```
Ventas Totales = SUM(ventas_techstore[cantidad])
```
<img width="201" height="135" alt="image" src="https://github.com/user-attachments/assets/ed634af5-68b5-454d-8a4b-9159b314b7f6" />


Tableau:

Calculated Field:
```
(SUM([ventas_techstore].[Cantidad]))
```

<img width="301" height="203" alt="image" src="https://github.com/user-attachments/assets/bbf071b3-36c4-4a6c-ac89-347ae739c165" />




