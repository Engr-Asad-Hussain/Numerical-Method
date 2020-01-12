import numpy as np

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
      variable = int(input("ENTER ORDER OF SQUARE MATRIX:: "))
      
      global A, B
      A = np.random.randint(-10, 10, size=(variable,variable))
      np.fill_diagonal(A, 10*variable)
      print("MATRIX::")
      print(A)
      print("Order of Matrix::" + str(A.shape))
      print()

      B = np.random.randint(-10, 10, size=(variable,1))
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
      print("PROGRAM ENDS")
      
if __name__=="__main__":
      main()
