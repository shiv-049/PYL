#1. Hello TensorFlow Program
import tensorflow as tf

hello = tf.constant("Hello, TensorFlow!")
print(hello.numpy())

#2. Tensor Creation (1D & 2D)
import tensorflow as tf

# 1D Tensor
tensor_1d = tf.constant([1.3, 1, 4.0, 23.99])
print("1D Tensor:", tensor_1d)

# 2D Tensor
tensor_2d = tf.constant([[1,2,3],[4,5,6],[7,8,9]])
print("2D Tensor:\n", tensor_2d)

#3. Tensor Operations
import tensorflow as tf

# Define matrices
matrix1 = tf.constant([[2,2,2],[2,2,2],[2,2,2]])
matrix2 = tf.constant([[1,1,1],[1,1,1],[1,1,1]])

# Matrix Multiplication
product = tf.matmul(matrix1, matrix2)

# Addition
sum_result = tf.add(matrix1, matrix2)

print("Matrix Multiplication:\n", product.numpy())
print("Matrix Addition:\n", sum_result.numpy())


4. Determinant of Matrix
import tensorflow as tf

matrix = tf.constant([[2.0,7.0,2.0],
                      [1.0,4.0,2.0],
                      [9.0,0.0,2.0]])

det = tf.linalg.det(matrix)

print("Determinant:", det.numpy())
