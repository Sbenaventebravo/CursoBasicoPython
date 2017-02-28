# ejemplo
"""
ejemplos:

patron = "^lo"
va a coindidir con las palabras iniciadas con "lo"

patron = "do$"
va a coincidir con las palabras terminadas en "do"

patron ="^palabra$"
acota las coincidencias a "palabra" exlusivamente

patron = "a*b"
cuantificador
caracteres que multiplican el patron que les antecede
coincide con 0 o mas ocurrencias
ejemplo "b", "ab", "aab", "aaaab"

patron = "a+b"
a diferecia de el asterisco coincide con uno o mas ocurrencias
cadenas 'ab', 'aaab', 'aaaaaaab'

patron= "a?b"
valida si existe una o 0 ocurrencias
cadenas "b", "ab"

patron: a{4}
cadenas aceptadas "aaaa"

patron = a{4,8}
cadenas aceptadas "aaaa", "aaaaa", "aaaaaa", "aaaaaaa" "aaaaaaaa"

patron = loc[ao]
la cadenas aceptadas pueden ser "loco", "loca"
a traves de "[]" se puede, a su vez ,establece rangos
patron = "[0-9]"
patron2 = "[0-9A-Za-z]"
cadenas aceptadas -> cualquier letra o numero en mayusculas o minusculas

patron=[^abc]
este es un rango negado no se aceptaran ni 'a', ni 'b', ni 'c'

patron "a|b"
la cadena puede ser 'a' o 'b'
"""