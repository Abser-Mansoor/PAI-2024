import numpy as np
import abc as ab
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
dat = np.array(np.arange(1,11))
plt.subplot(2,3,1)
plt.plot(dat,dat*dat)
plt.xlabel("Numbers")
plt.ylabel("Function Value")
plt.title("y=x^2")
plt.text(2,60,'Could this be a line?',fontsize=15)
plt.annotate('This IS a line!!',(5,20),xytext=(4,10),arrowprops=dict(facecolor='black'))
plt.fill_between(dat,dat*dat,color='r',where= (dat >= 4) & (dat <= 9))
plt.legend()
plt.subplot(2,3,2)
plt.scatter(np.arange(1001,2000),np.arange(1,1000),marker='s',c='red')
plt.subplot(2,3,3)
plt.pie([30,20,40,10],labels=['Per1','Per2','Per3','Per4'],colors=['r','black','b','y'],explode=[0,0.4,0,0])
plt.subplot(2,3,4)
plt.stackplot([1,2,3,4,5],np.random.randint(10,size=5),np.random.randint(10,size=5),np.random.randint(10,size=5),np.random.randint(10,size=5),np.random.randint(10,size=5),labels=['Area 1','Area 2','Area 3','Area 4','Area 5'])
plt.legend(loc='lower right')
plt.subplot(2,3,5)
plt.boxplot([np.arange(0,101,10),np.arange(0,101,5)],vert=False,showmeans=True,labels=['Game Time','Study Time'],patch_artist=True,widths=0.7)
plt.subplot(2,3,6)
plt.stem([1,2,3,4,5,6],[2,3,4,5,6,7],linefmt=':',markerfmt='o')
plt.show()
plt.bar(['Data 1','Data 2', 'Data 3', 'Data 4', 'Data 5', 'Data 6'],np.random.randint(0,100,size=6),color='r',linewidth=[1,2,3,4,5,6],edgecolor=['green','blue','cyan','black','magenta','yellow'])
plt.show()
