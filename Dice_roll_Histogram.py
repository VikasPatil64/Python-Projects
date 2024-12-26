# DICE ROLL HISTOGRAM

import random
import matplotlib.pyplot as plt

def roll_die(num_rolls):
    results=[random.randint(1,6) for _ in range (num_rolls)]
    return results

def plot_histogram(results):
    plt.hist(results, bins = range(1,8), edgecolor="black", align = "left")
    plt.title("Histogram of Dice Rolls")
    plt.xlabel("Dice Face")   
    plt.ylabel("Frequency")  
    plt.xticks(range(1,7))
    plt.show()
    
def main():
    num_rolls = int(input("Enter the number of times to roll the dice :"))
    results = roll_die(num_rolls)
    plot_histogram(results)
    
if __name__ == "__main__":
    main()