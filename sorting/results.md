# Sorting
In our variant, we need to compare two algorithms - Heapsort and Quicksort for different input types - reals and dates.

## Algorithms overview
### Quicksort

Quicksort (sometimes called partition-exchange sort) is an efficient sorting algorithm developed by Tony Hoare in 1959, with his work published in 1961; it is still a commonly used algorithm for sorting. 

Quicksort is a comparison sort, meaning that it can sort items of any type for which a "less-than" relation (formally, a total order) is defined. In efficient implementations it is not a stable sort, meaning that the relative order of equal sort items is not preserved. Quicksort can operate in-place on an array, requiring small additional amounts of memory to perform the sorting.

Algorithm uses divide-and-conquer principle, and so it's a recursive algorithm.
Here is how quicksort uses divide-and-conquer. Think of sorting a subarray `array[p..r]`, where initially the subarray is `array[0..n-1]`.
	
1. **Divide** by choosing any element in the subarray `array[p..r]`. Call this element the **pivot**. Rearrange the elements in `array[p..r]` so that all other elements in `array[p..r]` that are less than or equal to the pivot are to its left and all elements in `array[p..r]` are to the pivot's right. This procedure is called *partitioning*. At this point, it doesn't matter what order the elements to the left of the pivot are in relative to each other, and the same holds for the elements to the right of the pivot. We just care that each element is somewhere on the correct side of the pivot.

2. **Conquer** by recursively sorting the subarrays `array[p..q-1]` (all elements to the left of the pivot, which must be less than or equal to the pivot) and `array[q+1..r]` (all elements to the right of the pivot, which must be greater than the pivot).

3. **Combine** by doing nothing. Once the conquer step recursively sorts, we are done. Why? All elements to the left of the pivot, in `array[p..q-1]`, are less than or equal to the pivot and are sorted, and all elements to the right of the pivot, in `array[q+1..r]`, are greater than the pivot and are sorted. The elements in `array[p..r]` can't help but be sorted!

Mathematical analysis of Quicksort shows that, on average, the algorithm takes `O(nlog(n))` comparisons to sort n items. In the worst case, it makes `O(n^2)` comparisons, though this behavior is rare. Although, somewhat is slower in practice on most machines than a well-implemented Quicksort, it has the advantage of a more favorable worst-case `O(nlog(n))` runtime. 

### Heapsort

Heapsort is a comparison-based sorting algorithm. Heapsort can be thought of as an improved selection sort: like that algorithm, it divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region. The improvement consists of the use of a heap data structure rather than a linear-time search to find the maximum.

**Heap** is a specialized tree-based data structure that satisfies the heap property: if A is a parent node of B then the key (the value) of node A is ordered with respect to the key of node B with the same ordering applying across the heap. A heap can be classified further as either a "max heap" or a "min heap". In a max heap, the keys of parent nodes are always greater than or equal to those of the children and the highest key is in the root node. In a min heap, the keys of parent nodes are less than or equal to those of the children and the lowest key is in the root node.

The heap is one maximally efficient implementation of an abstract data type called a **priority queue**, and in fact priority queues are often referred to as "heaps", regardless of how they may be implemented. A common implementation of a heap is the binary heap, in which the tree is a complete binary tree (see figure).

<p align="center">
  <img src="https://interactivepython.org/runestone/static/pythonds/_images/heapOrder.png" alt="Heap visiualization"/>
</p>

Heapsort was invented by J. W. J. Williams in 1964. This was also the birth of the heap, presented already by Williams as a useful data structure in its own right.

The Heapsort algorithm can be divided into two parts.

In the first step, a heap is built out of the data. The heap is often placed in an array with the layout of a complete binary tree. The complete binary tree maps the binary tree structure into the array indices; each array index represents a node; the indexes of the node’s parent, left child branch, or right child branch are simple expressions. For a zero-based array, the root node is stored at index 0; if `i` is the index of the current node, then

```javascript
  iParent(i)     = floor((i-1) / 2) // where floor functions map a real number to the smallest leading integer.
  iLeftChild(i)  = 2*i + 1
  iRightChild(i) = 2*i + 2
```

In the second step, a sorted array is created by repeatedly removing the largest element from the heap (the root of the heap), and inserting it into the array. The heap is updated after each removal to maintain the heap. Once all objects have been removed from the heap, the result is a sorted array.

Heapsort is an in-place algorithm, but it is not a stable sort. The array can be split into two parts, the sorted array and the heap. The heap's invariant is preserved after each extraction, so the only cost is that of extraction.

The heapsort algorithm involves preparing the list by first turning it into a max heap. Then the algorithm repeatedly swaps the first value of the list with the last value, decreasing the range of values considered in the heap operation by one, and sifting the new first value into its position in the heap. This repeats until the range of considered values is one value in length.

The steps are:

1. Call the `makeInitialHeap()` function on the list. Also referred to as `heapify()`, this builds a heap from a list in `O(n)` operations.
2. Swap the first element of the list with the final element. Decrease the considered range of the list by one.
3. Call the `sift()` function on the list to sift the new first element to its appropriate index in the heap.
4. Go to step (2) unless the considered range of the list is one element.

The `buildMaxHeap()` operation is run once, and is `O(n)` in performance. The `sift()` function is `O(log(n))`, and is called `n` times. Therefore, the performance of this algorithm is `O(n+n*log(n))` which evaluates to `O(nlog(n))`.

## Theoretical performance comparison

|                        | Quicksort   | Heapsort    |
| ---------------------- | ----------- | ----------- |
| Worst-case performance |    O(n^2)   | O(nlog(n))  |
| Average performance    | O(nlog(n))  | O(nlog(n))  |
| Best-case performance  | O(nlog(n))  | O(nlog(n))  |

## Implementation

For comparing these algorithms was chosen C++ language, because other high-level programming languages, e.g. Java, JavaScript, C# are doing a lot of optimization internally. C++ is a compromise between low-level C and other mentioned` languages. We want to mention that nobody in the team had experience working with C++. Hence, some code can be written not in "best-practices" of the language.

Source code can be find in [cpp-sources](https://github.com/rudnitskih/ucu-adc-coursework/tree/master/sorting/cpp-sources) folder. Code was written in [Code Blocks](http://www.codeblocks.org/) IDE and compiled by [GCC](http://gcc.gnu.org/). Additionally, need to enable [C++11](http://stackoverflow.com/a/24398366) mode in Code Blocks.

The program to compare algorithms is a console application.

![Application screenshot](./results/application_screenshot.png "Application screenshot")

### Technical details of implementation

The code can be divided into the following parts:

- **generator**, for generating test values;
- **heapsort**, implementation heapsort algorithm;
- **quicksort**, implementation quicksort algorithm;
- **utils**, helper functions, e.g. `saveToFile()`, `compareDates()`;
- **main**, for managing flow of operations.

For storing real values we use `double` data type, for storing Date we use the following custom data structure:
```cpp
	struct date {
	    int day;
	    int month;
	    int year;
	};

```

For generating random values we use the following ways.

Random real:
```cpp
double r = ((double)rand() / (double)(RAND_MAX)); // values in range (0, 1)
```

Random date:
```cpp
date date;
date.year = rand() % 20 + 1996;
date.month = rand() % 12 + 1;
date.day = rand() % 28 + 1;
```

Before both generation, we need to add a 'seed' to C++ generator: `srand((unsigned)time(NULL));`

For storing, array of data we used *[vector](http://www.cplusplus.com/reference/vector/vector/data/)* data type because is good solution to store array with dynamic length.
Source codes of algorithms you can check in [heapsort](//github.com/rudnitskih/ucu-adc-coursework/blob/master/sorting/cpp-sources/heapsort.h) and [quicksort](//github.com/rudnitskih/ucu-adc-coursework/blob/master/sorting/cpp-sources/quicksort.h) files.

To calculate correct time of algorithm execution we run the same algorithms with the same parameters ten times and estimated average duration.
```cpp
	
int countOfIteration = 10;

for (int i = 0; i < countOfIteration; i++ ) {
    algorithmPerformance currentPerfomance;

    if (algorithmName == "heapsort") {
        currentPerfomance = heapsort(vectorOfValues);
    } else {
        currentPerfomance = quicksort(vectorOfValues);
    }

    addPerfomanceValues(perfomance, currentPerfomance);

}

calculateAvaragePerfomance(perfomance, countOfIteration);
```

Results prepared on the machine with following characteristics:

- Laptop Dell Inspiron 3520
- OS Ubuntu 14.04 64-bit
- Processor Intel® Core™ i5-3210M CPU @ 2.50GHz × 4 
- SSD disk 128GB
- 8 Gb RAM

To minimize an influence of environment, we have run compiled program after reboot and have not started other processes. For calculating time was used [clock()](http://www.cplusplus.com/reference/ctime/clock/) utility which return count of *clock ticks*, which are units of time of a constant but system-specific length (with a relation of CLOCKS_PER_SEC clock ticks per second).
On machine with characteristics above CLOCKS_PER_SEC is equal to 1000000, so a precision of measured time is 0.00001 which enough for our experiment.

## Results

All raw results, which generated by application, can be found in [results](https://github.com/rudnitskih/ucu-adc-coursework/tree/master/sorting/results) folder in .csv files. We used the free LibreOffice to prepare final charts.

There are final tables for each algorithm:

![Heapsort results](./results/table_heapsort.png "Heapsort results")
![Quicksort results](./results/table_quicksort.png "Quicksort results")

As we can see "Scale factors" are located in the same small range, which mean algorithms were implemented correctly. It can also be seen in the corresponding graphs (average values were built by multiplying "Average Case Estimation" values on average scale factor).

For Heapsort algorithm:
![Average estimations for Heapsort](./results/average_estimation(heapsort).png "Average estimations for heapsort")

For Quicksort algorithm:
![Average estimations for Quicksort](./results/average_estimation(quicksort).png "Average estimations for Quicksort")

To answer the question "Which algorithm faster Heapsort vs Quicksort?", we built charts for both data types:

![Dates results](./results/dates_time_sorting.png "Dates results")
![Reals results](./results/reals_time_sorting.png "Reals results")

In both cases, Quicksort beats Heapsort almost in two times. Why?

Heapsort guarantee `O(nlog(n))` time, that is much better than the worst-case in Quicksort. The secret of Quicksort is: it does not swap unnecessary elements. Swap is time consuming.
With Heapsort, even if all of your data is already ordered, you are going to swap 100% of elements to order the array. With Quicksort you do not swap what is already ordered. If your data is completely ordered, you swap almost nothing. Although there is a lot of fussing about worst-case, a little improvement on the choice of pivot, any other than getting the first or last element of array, can avoid it. If you get a pivot from the intermediate element between first, last and middle element, it is sufficient to avoid worst-case.

What is superior in Quicksort is not the worst case, but the best case. In best case you do the same number of comparisons, but you swap almost nothing. In average case you swap part of the elements, but not all elements, as in Heapsort. That is what gives Quicksort the best time. 

Hence, it is the reason why many languages have default sort algorithm as Quicksort. 

## Conclusions

In this part, we compared two algorithms Heapsort and Quicksort. Theoretical descriptions give us a possibility to understand general details and complexity of algorithms.

Heapsort looked better than Quicksort because its Average, Worst- and Best-case performance the same - `O(nlog(n))`, and for Quicksort worst-case is `O(n^2)`. To compare them we have written C++ implementation for both algorithms and run on different types and amount of data.  

Final results changed our assumptions in start - Quicksort better than Heapsort, because it requires fewer exchange operations.


## Credits

- https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort
- https://en.wikipedia.org/wiki/Quicksort
- https://en.wikipedia.org/wiki/Heapsort
- https://en.wikipedia.org/wiki/Heap_(data_structure)
- https://www.cs.auckland.ac.nz/~jmor159/PLDS210/qsort3.html
- http://stackoverflow.com/questions/18591924/how-to-use-bitmask
- https://www.cs.auckland.ac.nz/~jmor159/PLDS210/qsort3.html
- Presentations of course "Algorithms and Data Structure" by Vadim Ermolayev (Block I Topic 3: Algorithm (Performance) Analysis: a Bit of Statistics and Experiments, Block III Topic 2: The Most Efficient Internal Sorting Algorithms)
