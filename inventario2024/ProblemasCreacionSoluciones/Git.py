# Problema Salia el Siguiente Mensaje 
    # fatal: loose object 4357e60bd88795b16c5806a171b1c8a2dc2f7aa3
    # (stored in .git/objects/43/57e60bd88795b16c5806a171b1c8a2dc2f7aa3) 
    # is corrupt
def Solucion():
    # Ejecutar Estos Comandos
    """
        find .git/objects/ -size 0 -exec rm -f {} \;
        git fetch origin
        Por ultimo git status y Deberia Funcionar
    """
