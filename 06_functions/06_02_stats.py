'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(numbers):
  max_number = max(numbers)
  min_number = min(numbers)
  sum_number = sum(numbers)
  avg_number = sum_number/len(numbers)
  return print(f"{max_number}, {min_number}, {sum_number}, {avg_number}")
  pass

# call the function below here
stats(example_list)
