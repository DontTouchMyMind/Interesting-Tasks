# По стандарту BMI (Body mass index) можно высчитать свой статус.
# BMI = MASS / HEIGHT^2
#
# Underweight = <18.5
# Normal = 18.5–25
# Overweight = 25–30
# Obesity = 30 or greater
#
# Пример:
# Input:
# mass = 84
# height = 180
# Output:
# Overweight 3 kg
from decimal import Decimal


bmi_statuses = {
    'Underweight': (0, Decimal(18.4)),
    'Normal': (Decimal(18.5), 25),
    'Overweight': (25, Decimal(29.9)),
    'Obesity': (30, 300)
}

mass = Decimal(input('mass = '))
height = Decimal(str(float(input('height = ')) / 100))
normal_mass = 25 * (height**2)
current_bmi = round(mass / (height**2), 1)
bmi_status = {key for key, value in bmi_statuses.items() if (value[0] <= current_bmi <= value[1])}.pop()
different_mass = f'{abs(round(mass - normal_mass))} kg' if bmi_status != 'Normal' else ''
print(f'{bmi_status} {different_mass}')
