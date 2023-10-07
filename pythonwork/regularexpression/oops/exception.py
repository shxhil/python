while True:
    try:
        x=int(input(" enter the number ="))
        y=(input("ente rthe number ="))
        z=x/y
        print(z)
        break

    except ValueError:
        print("enter a valid number")

    except ZeroDivisionError:
        print(" not divisible by zero")
    except TypeError:
        print("enter")