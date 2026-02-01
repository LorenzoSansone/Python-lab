def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

   
def get_int(prompt):
    while True: #until the input is correct (break on else branch)
        try:
            return int(input(prompt))
        except ValueError: #if something goes wrong this part is executed to handle the error
            pass #catch the error but we pass about compute the error

main()