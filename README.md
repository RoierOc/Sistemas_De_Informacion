# Análisis Comparativo: Power BI vs Tableau

## 1. Objetivo
El propósito de este análisis es crear un **dashboard idéntico** en dos herramientas de Business Intelligence (Power BI y Tableau) usando el dataset **TechStore**, para comparar la **usabilidad**, **rendimiento** y **capacidades** de ambas plataformas, y determinar cuál es más adecuada para el caso de estudio.

## 2. Dataset Utilizado
El dataset está compuesto por cuatro archivos CSV:

- **ventas_techstore.csv:** contiene las ventas históricas de productos, con fecha, cantidad, precio unitario, vendedor y cliente.
- **productos.csv:** catálogo de productos, con categoría, stock y otros atributos.
- **clientes.csv:** información básica de clientes.
- **metas_mensuales.csv:** metas de ventas mensuales para evaluar el desempeño.

---

## 3. Construcción del Dashboard

**Gráficos**
   
- **Gráfico de Líneas:** Ventas por mes

Power BI:

<img width="1207" height="654" alt="image" src="https://github.com/user-attachments/assets/dc0b1a7f-8b8a-4f8b-9096-5814d5a9b297" />

```
Ventas Totales = SUM(ventas_techstore[cantidad])
```
---

Tableau:

<img width="449" height="819" alt="image" src="https://github.com/user-attachments/assets/ad2a92fb-9d42-44a9-83d1-1c60b3c7b103" />

Calculated field:
```
(SUM([ventas_techstore].[Cantidad]))
```

---

- **Gráfico de Barras:** Top 10 productos por ventas

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

---

Tableau:


Calculated field 2:
```
SUM([stock_actual])
```

<img width="767" height="821" alt="image" src="https://github.com/user-attachments/assets/63a21082-1c5d-4c2b-a62a-40feb4c274a0" />

---

- **Gráfico de Pie:** Ventas por categoría


Power BI:

DAX:
```
Ventas Totales = SUM(ventas_techstore[cantidad])
```

<img width="1057" height="615" alt="image" src="https://github.com/user-attachments/assets/f9bb0b4e-efe4-41fb-905f-d091b48bc3a2" />

---

Tableau:

Calculated Field:

```
SUM([venta_total])
```


<img width="372" height="193" alt="image" src="https://github.com/user-attachments/assets/688047e1-209e-4016-982e-04710e13c67e" />

---

 - **Gráfico de Tabla:** Performance de vendedores (ventas, clientes atendidos)


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

---

# Comparación de herramientas:

Crear el dashboard en Power BI fue un proceso bastante directo. La interfaz es muy intuitiva: cargas los datos, defines relaciones y construyes visualizaciones sin demasiada fricción. DAX ayuda a crear medidas personalizadas de forma sencilla y, con algo de apoyo en documentación o IA, es fácil entender y replicar el código. En general, fue rápido armar el dashboard y el resultado se ve limpio y profesional.

En Tableau, la experiencia es distinta. Es una herramienta que invita más a explorar los datos y probar diferentes visualizaciones. Las calculated fields son fáciles de entender y conectar tablas es bastante simple. Además, permite crear dashboards muy interactivos gracias a las acciones entre hojas, lo que da un resultado final más dinámico. Sin embargo, el proceso toma más tiempo, ya que cada visual debe construirse en una hoja y luego agregarse manualmente al dashboard. Además, la interfaz me resultó un poco menos intuitiva que la de Power BI.

Otro punto importante es el costo: Power BI tiene una versión de escritorio gratuita, mientras que Tableau requiere una licencia de pago, en conclusión, la experiencia en Power BI fue más rápida y eficiente, ideal si se busca construir un dashboard de forma ágil y sin gastar mucho.
