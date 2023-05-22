def print_operation_table(operation, num_rows = 10, num_columns = 10):
    for row in range(1, num_rows + 1):
        for columns in range(1, num_columns + 1):
            print(operation(row, columns), end='\t')
        print()

print_operation_table(lambda row, colums: row * colums)