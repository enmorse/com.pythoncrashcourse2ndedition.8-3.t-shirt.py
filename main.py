# Write a function named make_shirt() that accepts
# a size and the text message of a message that should
# be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and
# the message printed on it.

# Call the function once using positional arguments
# to make the shirt. Call the function a second time
# using keyword arguments.

def make_shirt(size, msg):
    print(f"\nThe size of the shirt is {size} and the "
          f"message printed on the shirt is {msg}.")


make_shirt("XL", "\"Nothing But the Glove\"")
make_shirt(size="XL", msg="\"Nothing But the Glove\"")
