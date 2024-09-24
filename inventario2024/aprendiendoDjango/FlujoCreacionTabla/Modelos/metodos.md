
# Creacion                    |   # Filtrado                       | # ValidacionExistencia
  "model.create(name=value)"  |   "instance.filter(name=value)"    | "model.objects.filter(id=id).exists()"
  "model.save()"

# FiltradoEliminacion         |
   "model.objects.filter      |
   (name=name).delete()"      |


#                                  Mostrar 
# Listar Todo
  `productos = Producto.objects.all()`

