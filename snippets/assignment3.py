t = 0.01 # через какой интервал времени делаем вычисления

G = 6.6740831e-11 # гравитационная постоянная
Mm = 7.3477e22 # масса Луны kg
Rm = 1737100 # радиус Луны m

# Начальные условия
# Нужно их назначить
T = # время
H = # высота
V = # скорость

Md = 4600 # Масса нашего корабля без топлива
Mf = # Масса топлива - недозаправлен
Ft = 45000 # Сила тяги двигателя в N
Vf = 3050 # Скорость истечения топлива из двигателя
Mt = # Считаем сколько мы расходуем топлива за 1 сек kg/s

while H >= 0:
    Ma = # Считаем новую полную массу
    if (Mf > (Mt*t)): # Еслм у нас есть топливо на время t
        Mf = # Пересчитываем остаток топлива
        ae = # Пересчитываем ускорение от двигателя
    else: # Если топливо закончилось, то падаем
        ae = # Пересчитываем ускорение от двигателя

    g = # Пересчитываем ускорение свободного падения
    a = # Считаем результирующее ускорение !!! У нас несколько ускорений и они разнонаправлены !!!
    V = V + a * t 
    H = H + V * t
    T = T + t
    if (abs(T - round(T)) <= t / 2):
        print ('T=' + str(T) + " s;" + " Mf=" + str(Mf) + " H=" + str(H) + " m;" + " V=" + str(V) + " m/s;" + " a=" + str(a) + " m/s^2")

print ('T=' + str(T) + " s;" + " Mf=" + str(Mf) + " H=" + str(H) + " m;" + " V=" + str(V) + " m/s;" + " a=" + str(a) + " m/s^2")
