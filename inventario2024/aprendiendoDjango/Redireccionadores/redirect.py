def FlujoFuncionamiento():
    """usar nombre de la url prinpal de cada app y 
    luego el nombre propio que se le da en cada app
    
    Ejemplo:
        URL core principal:
            path('news/',include(('newsletter.urls','newsletter'),namespace='news')),
        URL Core app
            path('home/',home, name='home'),




        Redirect: 
            return redirect('news:home')
            
        """