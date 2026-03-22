from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """
    ll = LinkedList()

    ll.insert_at_front(3)
    ll.insert_at_front(2)
    ll.insert_at_front(1)
    ll.insert_at_end(4)
    ll.insert_at_end(5)

    print("Original list:")
    ll.display()

    total = ll.recursive_sum()
    print("Sum of list:", total)

    target = 3
    found = ll.recursive_search(target)
    print(f"Search for {target}:", found)

    target = 10
    found = ll.recursive_search(target)
    print(f"Search for {target}:", found)

    ll.recursive_reverse()
    print("Reversed list:")
    ll.display()