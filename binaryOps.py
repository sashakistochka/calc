print("Добро пожаловать в консольный калькулятор!")

operand1 = input("Введите первый операнд (только целое число): ")
operand2 = input("Введите второй операнд (только целое число, кроме ноля, если собираетесь делить): ")

op = input("Введите оператор (+, -, /, *, //, **): ")

if op == "+": result = int(operand1) + int(operand2)
if op == "-": result = int(operand1) - int(operand2)
if op == "/": result = int(operand1) / int(operand2)
if op == "*": result = int(operand1) * int(operand2)
if op == "//": result = int(operand1) // int(operand2)
if op == "**": result = int(operand1) ** int(operand2)

print("Результат вычисления: " + str(result))
