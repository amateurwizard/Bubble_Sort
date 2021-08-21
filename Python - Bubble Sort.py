# Author: Amateur Wizard
# Date: 2021/08/21


def bubble_sort(my_list):       # This is the method that sorts a list
    swapped = True
    store = 0       # This is a temporary store for the list items, initialised for integers

    while swapped:
        swapped = False

        for counter in range(0, len(my_list) - 1):    # For loop will loop for each item in the list
            if my_list[counter] > my_list[counter + 1]:     # Runs when item next is smaller
                store = my_list[counter + 1]
                my_list[counter + 1] = my_list[counter]
                my_list[counter] = store
                swapped = True

    return my_list      # Returns the list to the item that called it


def main():
    my_list = [3, 1, 16, 2, 8, 5, 9]    # This is the list that will be sorted

    my_list = bubble_sort(my_list)      # This saves the sorted list to the same array variable

    print(my_list)
    exit()


if __name__ == '__main__':
    main()
