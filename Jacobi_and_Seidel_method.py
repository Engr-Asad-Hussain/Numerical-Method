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

def Logic(X):
      Sum = 0
      for rows in range(0, A.shape[0]):
            for columns in range(0, A.shape[1]):
                  if rows != columns :
                        intermediate = A[rows][columns] * X[columns]
                        Sum = Sum + intermediate
                  elif rows == columns :
                        coefficient = A[rows][columns]
                        vector_value = B[rows]
                        
            X_new = (vector_value - Sum) / coefficient
            intermediate, Sum, coefficient, vector_value = 0, 0, 0, 0
            X[rows] = X_new

      vector = np.subtract(np.matmul(A, X), B)
      magnitude = np.linalg.norm(vector)
      return(X, magnitude)

def main():
      print(":::JACOBI ITERATIVE METHOD:::")
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
      print("JACOBI PROGRAM ENDS")
      print("----------------------------------------")
      print("----------------------------------------")
      print()

      #variable = int(input("ENTER ORDER OF SQUARE MATRIX:: "))
      print(":::SEIDEL ITERATIVE METHOD:::")
      global A, B
      A = np.copy(initial_matrix)
      #A = np.random.randint(-10, 10, size=(variable,variable))
      #np.fill_diagonal(A, 10*variable)
      print("MATRIX::")
      print(A)
      print("Order of Matrix::" + str(A.shape))
      print()

      #B = np.random.randint(-10, 10, size=(variable,1))
      B = np.copy(initial_vector)
      print("VECTOR::")
      print(B)
      print("Order of Vector::" + str(B.shape))
      print()

      X = np.zeros((variable,1))

      i = 1
      while(i != 0):
            new_value, magnitude = Logic(X)
            if magnitude < 1e-14 :
                  break
            i += 1
            X = new_value

      print("SOLUTION:: ")
      print(X)
      print("NUMBER OF ITERATIONS::" + str(i))
      print("SEIDEL PROGRAM ENDS")
      
if __name__=="__main__":
      main()
