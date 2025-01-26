def find_reverse(index, name):
    if index >= len(name):
        return ""
    find_reverse(index + 1, name)
    print(name[index], end="")


if __name__ == "__main__":
    name = input(f"Enter the string: ")
    find_reverse(0, name)
