#Напишіть програму для перетворення відстані (вказана у футах)
#у дюйми (1 фут = 12 дюймів), ярди (1 фут = 0,333333333 ярда) і
#милі (1 фут = 0,000189393939 милі).

f=int(input("Введіть кількість футів : "))
i=f*12
y=f*0.333333333
m=f*0.000189393939
print("The distance in inches is" f" {i} " "inches.")
print("The distance in yards is" f" {y:.3f} " "yards.")
print("The distance in miles is" f" {m:$^10.3f} " "miles.")
