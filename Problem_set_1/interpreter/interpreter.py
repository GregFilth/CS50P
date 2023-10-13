expression = input("Expression: ").strip()
x, y, z = expression.split(" ")

match y:
    case "+":
        print(float(float(x)+float(z)))
    case "-":
        print(float(float(x)-float(z)))
    case "*":
        print(float(float(x)*float(z)))
    case "/":
        print(float(float(x)/float(z)))