def get_user_input():
    while True:
        user_input = input("Enter a word (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            print(f"You entered: {user_input}")

# Calling the function
get_user_input()
