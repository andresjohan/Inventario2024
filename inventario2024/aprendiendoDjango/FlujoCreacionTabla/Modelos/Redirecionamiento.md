# Django 
``  Redirecionadores A ---> 
    |HTML           |     Functions         | almacenador Exterior Data |
    |---------------|-----------------------|---------------------------|
    |render         |    redirect  name     |toma data  pantalla        |
    |<a href="">    |    reverse            |almacena en form           |
    |               |    reverse_lazy       |
    |               |    <a href="">        |
    |return HttpResponseRedirect('/productos')

   

    |Nombres Simbolicos  (namespaces , name ) |
    |-----------------------------------------|
    |General | Normal     |
    |-----------------------------------------|
    |namespace|name                           |