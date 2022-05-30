print("Hello Good People! I am Ramunajan. \nFacing problem in calculations? \nTRY ME! \n")
print("   What do u wanna try?\n", "  Type '+' for Addition\n", "  Type '-' for Subtraction\n",
      "  Type '*' for Multiplication\n", "  Type '/' for Division\n", "  Type '**' for Power\n",
      "  Type '%' for finding Remainder")
operator = input()

if operator == "+":
    print("Enter First Number")
    num1 = int(input())
    print("Enter Second Number")
    num2 = int(input())
    print("Hence your required sum is", num1 + num2)

elif operator == "-":
    print("Enter First Number")
    num3 = int(input())
    print("Enter Second Number")
    num4 = int(input())
    print("Hence your required difference is", num3 - num4)

elif operator == "*":
    print("Enter First Number")
    num5 = int(input())
    print("Enter Second Number")
    num6 = int(input())
    print("Hence your required product is", num5 * num6)

elif operator == "/":
    print("Enter First Number")
    num7 = int(input())
    print("Enter Second Number")
    num8 = int(input())
    print("Hence your required quotient is", num7 / num8)

elif operator == "**":
    print("Enter First Number")
    num9 = int(input())
    print("Enter Second Number")
    num10 = int(input())
    print("Hence your required number is", num9 ** num10)

elif operator == "%":
    print("Enter First Number")
    num11 = int(input())
    print("Enter Second Number")
    num12 = int(input())
    print("Hence your required remainder is", num11 % num12)
