import matplotlib.pyplot as plt

data = {
    "time" : [i for i in range (1, 10)],
    "temperature" : [i*i for i in range (1, 10)]
}
plt.plot(
    data["time"],
    data["temperature"],
    color = "r"
    
)
plt.show()
