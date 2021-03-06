#authors: ehsan nayernia-amirhosein ataei

import numpy as np

import matplotlib.pyplot as plt

text = open('text.txt', 'r')

a = text.readline()
i = [0]*3
for c in range(len(a)):
    if a[c] == '0':
        i[0]=i[0]+1  
    if a[c] == '1':
        i[1]=i[1]+1  
    if a[c] == '2':
        i[2]=i[2]+1
      
## plot section
fig = plt.figure()
nums = ['0', '1', '2']
barlist = plt.bar(nums, i, width=1)
barlist[0].set_color('g')
barlist[1].set_color('b')
barlist[2].set_color('r')

plt.savefig('out.png', format='png', dpi=160)
plt.show()
