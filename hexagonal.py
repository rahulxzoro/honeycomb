def hexagonal(rows, columns):
    for i in range(rows):
        print(" --- " * columns)
        print("/   \\" * columns )
        print("\   /" * columns)
    print(" --- " * columns)    

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
hexagonal(rows, columns)