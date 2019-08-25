import os

file_1 = open('mvdb.txt','w')
file_2 = open('mvdb_o.txt','r')
l_t_copy = file_2.readlines()
file_1.writelines(l_t_copy)

file_1.close()
file_2.close()
