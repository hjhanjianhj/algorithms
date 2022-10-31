# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = [5,4,5,7,2,8,3,2,8]
    print(data)

    for count in range(len(data)-1):
        for current_index in range(len(data)-count-1):
            if data[current_index] > data[current_index + 1]:
                # temp = data[current_index]
                # data[current_index] = data[current_index + 1]
                # data[current_index+1] = temp
                # data[current_index], data[current_index+1] = data[current_index+1], data[current_index]
                # data[current_index] = data[current_index] ^ data[current_index+1]
                # data[current_index+1] = data[current_index] ^ data[current_index+1]
                # data[current_index] = data[current_index] ^ data[current_index+1]
                pass


    print(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
