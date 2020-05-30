Algorithm: 
Binary Search


Use Case:
Searching a sorted list for a value.

Procedure:
Given a sorted list and asked to check if a value exists in the list.  
Check if the list length is odd or even.  
Find the mid-point of a list then check if the value if greater than or less than the target value.
Repeat



Time Efficiency (Worst Case):
1/2 O(N) ?

| Array Size | Iterations | Growth          |
| :------:   | :--------: | :----:          |
|    0       |     0      |    0            |
|    1       |     1      |   2<sup>0</sup> |
|    2       |     2      |   2<sup>1</sup> |
|    4       |     3      |   2<sup>2</sup> |
|    8       |     4      |   2<sup>3</sup> |