import numpy as np

def Matrix_Segments():
      diagonal_matrix = np.copy(initial_matrix)
      upper_lower_matrix = np.copy(initial_matrix)
      
      for rows in range(0, initial_matrix.shape[0]):     
            for columns in range(0, initial_matrix.shape[1]):
                  if rows != columns:
                        diagonal_matrix[rows][columns] = 0
                  else:
                        upper_lower_matrix[rows][columns] = 0

      return (diagonal_matrix, upper_lower_matrix)

def Inverse_Generator(diagonal_matrix):
      inverse_of_diagonal = np.linalg.inv(diagonal_matrix)
      return (inverse_of_diagonal)

def Calculation(initial_guess, upper_lower_matrix, inverse_of_diagonal):
      new_value = np.matmul(inverse_of_diagonal, np.subtract(initial_vector,
                                      np.matmul(upper_lower_matrix, initial_guess)))
      return (new_value)

def Magnitude(initial_guess):
      vector = np.subtract(np.matmul(initial_matrix, initial_guess), initial_vector)
      magnitude = np.linalg.norm(vector)

      return (magnitude)

def main():
      variable = int(input("ENTER ORDER OF SQUARE MATRIX:: "))
      
      global initial_matrix, initial_vector
      initial_matrix = np.random.randint(-10, 10, size=(variable,variable))
      np.fill_diagonal(initial_matrix, 10*variable)
      print("MATRIX::")
      print(initial_matrix)
      print("Order of Matrix::" + str(initial_matrix.shape))
      print()

      initial_vector = np.random.randint(-10, 10, size=(variable,1))
      print("VECTOR::")
      print(initial_vector)
      print("Order of Vector::" + str(initial_vector.shape))
      print()

      initial_guess = np.zeros((variable,1))

      diagonal_matrix, upper_lower_matrix = Matrix_Segments()
      inverse_of_diagonal = Inverse_Generator(diagonal_matrix)

      i = 1
      while (i != 0):
            new_value = Calculation(initial_guess, upper_lower_matrix, inverse_of_diagonal)
            magnitude = Magnitude(new_value)
           
            if magnitude < 1e-14 :
                  break
            initial_guess = new_value
            i += 1

      print("SOLUTION:: ")
      print(initial_guess)
      print("NUMBER OF ITERATIONS::" + str(i))
      print("PROGRAM ENDS")
      
if __name__=="__main__":
      main()
