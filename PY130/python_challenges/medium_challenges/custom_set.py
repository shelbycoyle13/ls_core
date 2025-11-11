class CustomSet:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        
        self._elements = []
        for element in elements:
            if element not in self._elements:
                self._elements.append(element)

    def add(self, arg): #Adds a new element to the current set
        if arg not in self._elements:
            self._elements.append(arg)

    def is_empty(self):
        if len(self._elements) == 0:
            return True
        return False

    def contains(self, arg): #Checks if the set has a current value
        if arg in self._elements:
            return True
        return False

    def is_subset(self, other): #ALL elements of set A must be in set B
        return all(other.contains(element) for element in self._elements)

    def is_disjoint(self, other): #NONE of the elements of set A must be in set B
        return all(not other.contains(element) for element in self._elements)

    def is_same(self, other): #Sets must have the exact same elements
        if len(self._elements) != len(other._elements):
            return False
        return all(other.contains(element) for element in self._elements)

    def intersection(self, other): #Returns a new set that contains the shared elements of set A and set B
        new_list = []
        for element in other._elements:
            if element in self._elements:
                new_list.append(element)

        return CustomSet(new_list)

    def difference(self, other): #Returns a new set that has the elements in A not present in B; i.e. A - B
        new_list = []
        for element in self._elements:
            if element not in other._elements:
                new_list.append(element)
        
        return CustomSet(new_list)

    def union(self, other): #Returns a new set that has ALL of the elements combined in both A and B
        new_list = []
        for element in self._elements:
            if element not in new_list:
                new_list.append(element)

        for el in other._elements:
            if el not in new_list:
                new_list.append(el)

        return CustomSet(new_list)
    
    def __eq__(self, other):
        return self.is_same(other)