def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(format(i*j,'4.0f'), end="")
        print()

main()