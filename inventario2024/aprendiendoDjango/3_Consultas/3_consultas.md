# Consulta por Valor                         |  ModficarDatos                        |  Guardar
  `User.objects.get(username='name')`        |  `user.set_password('new_password')`  |  user.save()
  `get_object_or_404(User , username='juan'` |


  # ConsultaCreacion
  `objects.get_or_create(user=user)`