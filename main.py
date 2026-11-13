from linked_list import LinkedList


if __name__ == "__main__":
    # Create an empty linked list.
    linked_list = LinkedList()

    # Add sample employee IDs.
    linked_list.insert_at_end(101)
    linked_list.insert_at_end(202)
    linked_list.insert_at_end(303)

    print("Original list:")
    linked_list.display()

    print(f"\nSum of IDs: {linked_list.recursive_sum()}")

    target = 202
    print(
        f"Search for {target}: "
        f"{linked_list.recursive_search(target)}"
    )

    missing_target = 999
    print(
        f"Search for {missing_target}: "
        f"{linked_list.recursive_search(missing_target)}"
    )

    linked_list.recursive_reverse()

    print("\nReversed list:")
    linked_list.display()