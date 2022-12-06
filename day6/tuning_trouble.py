def sliding_window(string, window_size):

    # Loop through the string, starting at the first character
    for i in range(len(string)):
        # Extract the current window of characters from the string
        window = string[i : i + window_size]

        # Check if the window is the correct size
        if len(window) == window_size:
            # check if the window contains 4 distinct characters
            if not len(set(window)) < len(window):
                print(
                    f"character {i + window_size} is the last character in the window of size {window_size} that don't repeat"
                )
                break


data = open("input.txt", "r").read().splitlines()
sliding_window(data[0], 4)
sliding_window(data[0], 14)
