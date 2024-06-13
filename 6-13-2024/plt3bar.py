import matplotlib.pyplot as plt

time= [i for i in range (1, 10)]
tem= [i*i for i in range (1, 10)]

plt.title('Temperature of room')
plt.xlabel('time(s)')
plt.ylabel('temperature(*C)')
plt.bar(time,tem,label='EX1')
plt.show()
