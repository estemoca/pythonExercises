 

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



from functools import lru_cache

@lru_cache(None)
def i(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return i(n - 1) + i(n - 2) + i(n - 3)




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

def f(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return f(n - 1) + f(n - 2) + f(n - 3)







from functools import lru_cache

# E P 1: C Ú (Malla)
F_M = 3
C_M = 3

@lru_cache(None)
def a(f, c):
    if f == 0 or c == 0:
        return 1
    
    r = a(f - 1, c) + a(f, c - 1)
    
    return r

def b(X, Y):
    T = [[0] * Y for _ in range(X)]

    for i in range(Y):
        T[0][i] = 1
    for j in range(X):
        T[j][0] = 1

    for i in range(1, X):
        for j in range(1, Y):
            T[i][j] = T[i - 1][j] + T[i][j - 1]
            
    return T[X - 1][Y - 1]

# E P 2: M d M (Monedas)
D = [1, 5, 10, 25]  # Conjunto D
S = 30
I = float('inf')

def c(v_a):
    if v_a == 0:
        return 0
    if v_a < 0:
        return I
    m_r = I
    
    for d_c in D:
        r_s = c(v_a - d_c)
        if r_s != I:
            m_r = min(m_r, 1 + r_s)
    return m_r

def d(conj_d, v_t):
    C = [I] * (v_t + 1)
    
    C[0] = 0
    
    for v_c in range(1, v_t + 1):
        for d_i in conj_d:
            
            if v_c >= d_i:
                C[v_c] = min(C[v_c], 1 + C[v_c - d_i])
                
    return C[v_t]

# E P 3: S (Fb)
N_F = 10
M = {} # Mapa M

def e(n):
    if n in M:
        return M[n]
        
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    r = e(n - 1) + e(n - 2)
    
    M[n] = r
    
    return r

def f(n):
    if n <= 0: return 0
    if n == 1: return 1

    v1 = 0
    v2 = 1
    
    for _ in range(2, n + 1):
        v3 = v1 + v2
        
        v1 = v2
        v2 = v3
        
    return v2