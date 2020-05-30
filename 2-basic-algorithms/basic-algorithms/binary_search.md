Algorithm: 
Binary Search


Use Case:
Searching a sorted list for a value.

Procedure:
1. Find the center of the list by setting an upper and lower bound to find the center.   
2. Check if the element at the center is the target.  
3. If it is, return the index of the target.
4. If not, is the target greater or less than that element?
5. If greater, move the lower bound to just above the current center.
6. If less, move the upper bound to just below the current center.
7. Repear step 1-6 until you find the target or until the bounds are the same or cross.



Time Efficiency (Worst Case):
O(log<sub>2</sub>) 

| Array Size | Iterations | Growth          |
| :------:   | :--------: | :----:          |
|    0       |     0      |    0            |
|    1       |     1      |   2<sup>0</sup> |
|    2       |     2      |   2<sup>1</sup> |
|    4       |     3      |   2<sup>2</sup> |
|    8       |     4      |   2<sup>3</sup> |