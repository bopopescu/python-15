from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
x=[4,6,8]
y=[12,16,18]
#plt.plot(x,y)
#plt.bar(x,y)
plt.stackplot(x,y,colors=['m','c'])
plt.legend()
plt.show()


