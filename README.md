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

Calculated field 1:
```
SUM([stock_actual])
```


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

<img width="1279" height="625" alt="image" src="https://github.com/user-attachments/assets/ea7c6665-1440-4ea3-86f5-b2661ac8a03c" />



Calculated Field:

```
SUM([venta_total])
```


