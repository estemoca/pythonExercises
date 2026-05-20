#1.  Recursividad Pura
def f(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return f(n - 1) + f(n - 2) + f(n - 3)


#2. Top-Down clásico
def g(n, me):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in me:
        return me[n]
    
    res = g(n - 1, me) + g(n - 2, me) + g(n - 3, me)
    me[n] = res
    return res

# Uso: g(N, {})

#3 Bottom-Up (Iterativo con Array)
def h(n):
    if n <= 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]


#4 Top-Down con Caché (Herramienta de Lenguaje)
from functools import lru_cache

@lru_cache(None)
def i(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return i(n - 1) + i(n - 2) + i(n - 3)

#5: Bottom-Up con Caché (Tabla, sin optimización)
def j(n):
    if n == 0:
        return 1
    
    dp = [0] * (n + 1)
    
    # Casos base/inicialización
    dp[0] = 1
    if n >= 1: dp[1] = 1
    if n >= 2: dp[2] = 2
    
    for k in range(3, n + 1):
        dp[k] = dp[k - 1] + dp[k - 2] + dp[k - 3]
    
    return dp[n]

#6: Optimización de Espacio (Bottom-Up $O(1)$)
def k(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2

    a, b, c = 1, 1, 2  # n-3, n-2, n-1
    
    for _ in range(3, n + 1):
        res = a + b + c
        a = b
        b = c
        c = res
        
    return c