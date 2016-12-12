# Advanced Sorting

## Critiries

* Are the algorithms described clearly and sufficiently completely?
  * Completeness: 5
  * Clarity: 5 
* Are the theoretical performance estimations presented? 10
* Have the algorithms been correctly implemented? 10
* Do the implementations correspond to the algorithms which had to be implemented? 10
* Are the design and implementation decisions documented fully and clearly? 10
* Are all the data sets adequate for the experiments? 
  * Types and quantities: are all required data types covered? Is the no of records big enough? 5
  * Specifics in values: are the algorithm constraints / specifics regarding data values properly handled? 5
* Experiments
  * Nos of Operations: are the numbers of performed operations measured correctly? 5
  * Time: Has the time taken by the program correctly measured? 5
  * Influence of Operation Environment: has the harmful influence of multitasking properly minimized in the experiment; has it been explained in the report? 5
  * Precision: has the measures been taken with sufficient precision; has it been explained in the report? 5
* Analysis of results
  * Graphical representation: have the comparative diagrams been built for the results analysis? 7
  * Correctness: Have all the results been correctly presented in the diagrams? 7
  * Conclusions: Have all important conclusions been made based on the analysis? 6


## Results
### Intro
In our variant we need to compare two algorithms - Heapsort and Quicksort for different input types - reals and dates.

#### Quicksort

Quicksort uses divide-and-conquer, and so it's a recursive algorithm.
Here is how quicksort uses divide-and-conquer. We need to think of sorting a subarray `array[p..r]`, where initially the subarray is `array[0..n-1]`.
	
1. **Divide** by choosing any element in the subarray `array[p..r]`. Call this element the **pivot**. Rearrange the elements in `array[p..r]` so that all other elements in `array[p..r]` that are less than or equal to the pivot are to its left and all elements in `array[p..r]` are to the pivot's right. We call this procedure `partitioning`. At this point, it doesn't matter what order the elements to the left of the pivot are in relative to each other, and the same holds for the elements to the right of the pivot. We just care that each element is somewhere on the correct side of the pivot.

2. **Conquer** by recursively sorting the subarrays `array[p..q-1]` (all elements to the left of the pivot, which must be less than or equal to the pivot) and `array[q+1..r]` (all elements to the right of the pivot, which must be greater than the pivot).

3. **Combine** by doing nothing. Once the conquer step recursively sorts, we are done. Why? All elements to the left of the pivot, in `array[p..q-1]`, are less than or equal to the pivot and are sorted, and all elements to the right of the pivot, in `array[q+1..r]`, are greater than the pivot and are sorted. The elements in `array[p..r]` can't help but be sorted!



## Credits
- https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort
