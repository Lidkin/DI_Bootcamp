import numpy as np

data_int = np.array(np.random.randint(1, 100, size=25)).reshape(5,5)
#1._______________________________________________________

print('\n1++++++++++++++++++++++++++++++1\n',data_int)

#2._______________________________________________________
min_val = np.min(data_int)
max_val = np.max(data_int)

data_norm = (data_int - min_val) / (max_val - min_val)
data_norm = np.round(data_norm, decimals=2)

print('\n2++++++++++++++++++++++++++++++2\n',data_norm)

#3.________________________-_______________________________
mean_val = np.round(np.mean(data_int))
std_dev = np.std(data_int)

z_score_vector = (data_int - mean_val) / std_dev

print('\n3++++++++++++++++++++++++++++++3\n',z_score_vector)

#4.________________________________________________________
split_vector = np.ravel(data_int)

print('\n4++++++++++++++++++++++++++++++4\n',split_vector)

#5.________________________________________________________

vect1 = np.array(np.random.randint(1,10, size=5))
vect2 = np.array(np.random.randint(1,10, size=5))
dot_product = np.dot(vect1, vect2)

print('\n5++++++++++++++++++++++++++++++5\n',dot_product)

#6.________________________________________________________
data2 = np.array(np.random.randint(1, 100, size=9)).reshape(3,3)
data1 = data_int[0:3, 0:3]

multiplication_matrix = data1*data2


print('\n6++++++++++++++++++++++++++++++6\n',multiplication_matrix,'\n', np.dot(data1, data2))

#7.________________________________________________________
indentify_matrix = np.identity(3)
martix = indentify_matrix*2
matrix = np.linalg.inv(martix)
print('\n7++++++++++++++++++++++++++++++7\n',matrix)

#8.________________________________________________________

eigen_values_vectors = np.linalg.eig(data1)
print('\n8++++++++++++++++++++++++++++++8\n',eigen_values_vectors)

#9________________________________________________________

print('\n9++++++++++++++++++++++++++++++9\n',data_int.shape)

random_idx = np.random.choice(data_int.size, 5)

print('\n-----------------------------------\n',random_idx)

data_float = data_int.astype('float16')
data_float = data_float.reshape(25, )
data_float = data_float.ravel()

data_float[random_idx] = np.nan
data_float = data_float.reshape(5, 5)

print('\n------------------------------------\n',data_float)

print('\n------------------------------------\n', np.isnan( data_float))

print('\n------------------------------------\n', np.argwhere(np.isnan(data_float)))

#10__________________________________________________________

#nanmean skips the nan values to calculate the mean of the array
matrix_mean = np.nanmean(data_float)

print('\n10++++++++++++++++++++++++++++++10\n', matrix_mean)

nan_idx = np.isnan(data_float)

data_float[nan_idx] = matrix_mean
print(data_float)