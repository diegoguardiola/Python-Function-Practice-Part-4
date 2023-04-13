# Find the Max of three numbers.
def max_num(a,b,c):
  return max([a,b,c])

print(max_num(2,4,6))
print(max_num(36,45,95))

# Multiply all the numbers in a list.
def mult_list(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod
    
print(mult_list([1,2,3]))
print(mult_list([30]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(my_str):
  return my_str[::-1]

print(rev_string("mt string"))

# Checks whether a number falls in a given range.
def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(11,2,4))     
print(num_within(3,1,6))     


# Prints out the first n rows of Pascal's triangle.
def pascal(n):
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Compute each subsequent row and add it to the triangle
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            prev_row = triangle[i-1]
            num = prev_row[j-1] + prev_row[j]
            row.append(num)
        row.append(1)
        triangle.append(row)
    
    # Print out the triangle
    for row in triangle:
        print(" ".join(str(num) for num in row).center(n*2))


pascal(2)
pascal(5)