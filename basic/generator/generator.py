#GENERATOR: A generator function is a special type of function that returns an iterator object. 
# Instead of using return to send back a single value, generator functions use yield to produce a series of results over time.
# The function pauses its execution after yield, maintaining its state between iterations.

#Why Do We Need Generators?
#Memory Efficient : Handle large or infinite data without loading everything into memory.
#No List Overhead : Yield items one by one, avoiding full list creation.
#Lazy Evaluation : Compute values only when needed, improving performance.
#Support Infinite Sequences : Ideal for generating unbounded data like Fibonacci series.
#Pipeline Processing : Chain generators to process data in stages efficiently.

#BASE VERSION: 
"""
def main():
    n = int(input("What's n? "))

    for s in sheep(n):
        print(s)

def sheep(n):
    flock =[]
    for i in range(n):
        flock.append("sheep" * i)
    return flock
"""

#SECOND VERSION: with generator
def main():
    n = int(input("What's n? "))

    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "sheep" * i #it's like return one value at time

if __name__ == "__main__":
    main()
