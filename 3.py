class NestedList:
    def __init__(self, elements):
        self.elements = elements

    # Function to check if the nested list is empty
    def is_empty(self):
        # Return True if the list is empty, otherwise False
        return len(self.elements) == 0

    # Function to flatten the nested list
    def flatten(self):
        flattened = []

        # Iterate over the elements of the nested list
        for element in self.elements:
            if isinstance(element, NestedList):
                # If the element is another NestedList, call flatten recursively
                flattened.extend(element.flatten())
            else:
                # Otherwise, add the element to the flattened list
                flattened.append(element)

        return flattened


# Example of nested list
nls = NestedList([1, NestedList([2, 3]), 4, 5, NestedList([NestedList([6])])])

# Check if the nested list is empty
print(nls.is_empty())  # Output: False

# Flatten the nested list
print(nls.flatten())  # Output: [1, 2, 3, 4, 5, 6]

# Empty NestedList example
empty_nls = NestedList([])

# Check if the empty nested list is empty
print(empty_nls.is_empty())  # Output: True
