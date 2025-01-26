def reverse_stack_without_auxilary_space(stack):
    if not stack:
        return
    top = stack.pop()
    # recusrively reverse remaining stack
    reverse_stack_without_auxilary_space(stack)
    insert_at_bottom(stack, top)


def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)


if __name__ == "__main__":
    stack = [1, 2, 3, 4, 5]
    reverse_stack_without_auxilary_space(stack)
    print(stack)
