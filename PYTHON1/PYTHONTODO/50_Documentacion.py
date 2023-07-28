def areaTriangulo(b,h):

    """
    Calcula el área de un triángulo dado

    >>> areaTriangulo(2,4)
    'El área del triángulo es: 4.0'
    """
    return "El área del triángulo es: " +str((b*h)/2)

import doctest
doctest.testmod()