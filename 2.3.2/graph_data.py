import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Column 2 from data table
A_input_chars = [1, 2, 3, 4]
B_input_chars = [1, 2, 3, 4, 5, 6, 7, 8]

# Column 3 and 4 from data table
# Replace list elements with your times
A_time = [0.00370192,0.022845, 0.177099943, 1.757218] 
B_time = [ 0.0071339,  0.0087039, 0.01190114, 0.0216300, 0.0568580627,  0.173401117325, 0.546566963196, 1.65189599991] 

fig, ax = plt.subplots(1,1)
# plot(x_list, y_list, "color and style")
ax.plot(A_input_chars, A_time, 'ro-', label='Algo. A') # red dots
ax.plot(B_input_chars, B_time, 'bo-', label='Algo. B') # blue dots

# Label and show
ax.set_xlabel ("Length of input in characters")
ax.set_ylabel("Execution time")
ax.set_title("Execution time vs. input length")
ax.legend(loc='center left') # Show and place the legend fig.set_facecolor('white')
fig.savefig('graph_data')