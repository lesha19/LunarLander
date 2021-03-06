# Lunar Lander
# Посадка на Луну

## Константы
### Гравитационная постоянная
`G = 6.6740831e-11 m^3/(s^2*kg) или N*m^2/kg^2`
### Луна
**Масса** `Mm = 7.3477e22 kg`

**Радиус** `Rm = 1737.10 km`
### Лунный модуль
**Сухая масса** `Md = 4600 kg`

**Масса топлива** `Mf = 11800 kg`

**Тяга двигателя** `Ft = 45000 N (100%)`
Может изменяться от 10% до 60%

**Скорость истечения топлива**
`Vf = 3050 m/s`
## Формулы

### Зависимость ускорения свободного падения от высоты над поверхностью тела
`g = G * M / (R + h)^2`

`g (m/s^2)` - ускорение свободного падения на высоте `h (m)` над поверхностью тела радиусом `R (m)` и массой `M (kg)`

`G`- гравитационная постоянная
### Тяга двигателя ###
`Ft = Mt * Vf (kg/s*m/s = kg*m/s^2 = N)`

`Mt (kg/s)` - расход топлива в секунду
