import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv('data.csv')

 
# Declaring the points for first line plot
Y1 = df['dinamic'].values
X1 = [1, 2 , 3, 4, 5, 6] 

# Setting the figure size
fig = plt.figure(figsize=(10,5))

# plotting the first plot
plt.plot(X1, Y1, label = "Dinâmico") 

# Declaring the points for second line plot
X2 = [1, 2 , 3, 4, 5, 6] 
Y2 = df['recursive'].values

# plotting the second plot 
plt.plot(X2, Y2, label = "Recursivo") 
  
# Labeling the X-axis 
plt.xlabel('Amostras') 

# Labeling the Y-axis 
plt.ylabel('Tempo (Segundos)') 


# Give a title to the graph
plt.title('Tempo de Execução') 
  
# Show a legend on the plot 
plt.legend() 

#Saving the plot as an image
fig.savefig('line plot.jpg', bbox_inches='tight', dpi=150)

#Showing the plot
plt.show() 