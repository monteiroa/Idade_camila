# ============================================
# OBI 2021 - Nível Júnior - Fase 1
# Questão: Idade de Camila
# ============================================

# Lê as três idades informadas pelo usuário
a = int(input())
b = int(input())
c = int(input())

# Verifica qual das três idades é a intermediária
if a >= b and a <= c:
    print("A idade de Camila é:", a)

elif a >= c and a <= b:
    print("A idade de Camila é:", a)

elif b >= a and b <= c:
    print("A idade de Camila é:", b)

elif b >= c and b <= a:
    print("A idade de Camila é:", b)

else:
    print("A idade de Camila é:", c)
