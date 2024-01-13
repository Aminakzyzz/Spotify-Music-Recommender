import matplotlib.pyplot as plt

def generate_and_save_plot():
    # Generate a simple plot
    x = [1, 2, 3, 4, 5]
    y = [2*i for i in x]

    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Plot')
    
    # Save the plot as an image
    plt.savefig('plot.png')
    
    # Display the plot
    # plt.show()

if __name__ == "__main__":
    generate_and_save_plot()

