def formato_numero(valor, prefijo=''):
    """
    Formatea un número en una representación legible con unidades de medida (k para miles, M para millones).

    Parameters:
    valor (float or int): El número a formatear.
    prefijo (str, optional): Un prefijo opcional a incluir antes del número formateado. Por defecto es una cadena vacía.

    Returns:
    str: El número formateado como una cadena con dos decimales y la unidad de medida adecuada (k para miles, M para millones).

    Examples:
    >>> formato_numero(1500)
    ' 1.50 k'
    >>> formato_numero(2000000, '$')
    '$ 2.00 M'
    >>> formato_numero(500)
    ' 500.00 '
    >>> formato_numero(500, '€')
    '€ 500.00 '
    """
    for unidad in ['','k']:
        if valor < 1000:
            return f'{prefijo} {valor:.2f} {unidad}'
        valor /= 1000
    return f'{prefijo} {valor:.2f} M'
