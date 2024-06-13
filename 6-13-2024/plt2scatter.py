import matplotlib.pyplot as plt

data = {
    "time" : [i for i in range (1, 10)],
    "temperature" : [i*i for i in range (1, 10)]
}
plt.scatter(
    data["time"],
    data["temperature"],
    marker = "^"
    
)
plt.show()
