## Problemas encontrados
TL/DR: un poco todo.
* La estructura misma de la BBDD. He intentado varias logicas, ninguna me ha convencido (el precio esta en inventario y no al nivel de Tarifa, la habitacion que aparece en el segundo nivel pero su cupo esta al nivel del inventario, se usan habitaciones al singular y al plural en los niveles 2 y 4).
* La gestion de modelos de datos. Para el inventario queria una clave doble (rate, date) pero parece que lo hice mal. Al final la logica era mas cerca de un booking que de un inventario.
* Queria hacer un DTO, sobre todo para el JSON del Availability, pero entre eso y los serializers no he sido capaz. Asi que acabo con algo bastante feo con nested loops.

Aun no se cual era la logica del arbol de disponibilidad. Leyendo el ejemplo:
- Primera hipotesis: seria capaz de tener tres veces la misma habitacion para un mismo precio un dia.
- Segunda hipotesis: Room no es el codigo de una habitacion en si misma, sino un tipo de habitacion, una categoria (y alli tendria mas sentido poner el precio en el Room Model.
- Tercera hipotesis: se trataba de dormitorios, por eso el cupo estaba al final en el inventario, se refiere a la disponibilidad de camas en una habitacion.

Bueno, con toda esa incertidumbre constante, cambiando los CRUDs cada dia, no he sido capaz de ir muy lejos. Nada de Swagger, de DTOs, de Test Unit, factorizar la gestion de errores... Y sobretodo, el Availability y los modelos no deberian corresponder a lo que se esperaba.

## Estructura
```
/crs
  /apis
      /availability
      /hotels
      /inventories
      /rates
      /rooms
      utils.py
  /migrations
  urls.py
  models.py
```
## Lanzar
Dudo que merece la pena probarlo.
Pero por si acaso. He usado un virtual env, pero fuera de Django no creo que hace falta descargar otra libreria.
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
