# -*- coding: utf-8 -*-
def main():
    hello()
    name = input("What's your name? ")
    hello(name)
    
def hello(to="world"):
    print("Hello",to)

main()
