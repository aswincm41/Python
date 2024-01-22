frozen_set1=frozenset([1,2,3,4,5])
frozen_set2=frozenset([3,4,5,6,7])
print(2 in frozen_set1)
print(7 in frozen_set1)
intersection_set = frozen_set1.intersection(frozen_set2)
print(intersection_set)

union_set = frozen_set1.union(frozen_set2)
print(union_set)

difference_set = frozen_set1.difference(frozen_set2)
print(difference_set)

#Intersection, union, difference


