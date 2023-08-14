import numpy as np

#exc2
vector_zero = np.zeros(10, dtype=float)

print(vector_zero)

#exc3

#exc4
np.info(np.add)

print(np.add.__doc__)

#exc5
vector_arange = np.arange(10, 50)

print(vector_arange)

#exc6
vector_slice = vector_arange[::-1]

print(vector_slice)

#exc7
matrix = np.arange(0, 9).reshape(3, 3)

print(matrix)

#exc8
vector_non_zero = np.nonzero([1, 2, 0, 0, 4, 0])

print(vector_non_zero)

#exc9
matrix_identity = np.eye(3, k=1, dtype=float)

print(matrix_identity)

#exc10
y = np.zeros((5,5))
matrix_five_five = np.full_like(y, np.arange(0, 5, dtype=float))#

print('10',matrix_five_five)

#exc11
vector_ten = np.linspace(0,1,num=11, endpoint=False, dtype=float)[1:]
print(vector_ten)

#exc12
vector_random_ten = np.sort(np.random.rand(10))

print(vector_random_ten)

#exc13
list_type = ['int8', 'int32', 'int64', 'float32', 'float64']

for int_t in list_type[:3]:
    print(np.iinfo(int_t))

for float_t in list_type[3:]:
    print(np.finfo(float_t))

#exc14

vector_16float = np.arange(10, dtype = 'float16').astype('float32', copy=False)

print(vector_16float)

vector_16float = np.arange(10, dtype='float16').astype('int32', copy=False)
print(vector_16float)

#exc15
vector_mean = np.arange(9).reshape(3, 3)
vector_mean = np.mean(vector_mean, axis=1)

print(vector_mean)

#exc16
vector_2D_sort = np.random.randint(0, 10, (2, 3))
vector_2D_sort = np.argsort(vector_2D_sort, axis=0)

print(vector_2D_sort)

#exc17
vector_2D = np.arange(12).reshape(4, 3)

print(vector_2D)

#exc18
vector_repeat = np.repeat([0, 1, 2], [2, 3, 1])
print(vector_repeat)

vector_bitcount = np.bincount(vector_repeat)
print(vector_bitcount)