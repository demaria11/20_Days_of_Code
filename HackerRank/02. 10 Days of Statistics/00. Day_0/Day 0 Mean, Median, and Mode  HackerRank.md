# Day 0: Mean, Median, and Mode | HackerRank

> Compute the mean, median, mode, and standard deviation.

**Objective** 

In this challenge, we practice calculating the _mean_, _median_, and _mode_. Check out the [Tutorial](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/challenges/s10-basic-statistics/tutorial) tab for learning materials and an instructional video!

**Task**  

Given an array, , of integers, calculate and print the respective _mean_, _median_, and _mode_ on separate lines. If your array contains more than one _modal value_, choose the numerically smallest one.

**Note:** Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of decimal place (i.e., , format).

**Example**  
  

The mean is .  
The median is .  
The mode is because occurs most frequently.

**Input Format**

The first line contains an integer, , the number of elements in the array.  
The second line contains space-separated integers that describe the array's elements.

**Constraints**

*   , where is the element of the array.

**Output Format**

Print lines of output in the following order:

1.  Print the _mean_ on the first line to a scale of decimal place (i.e., , ).
2.  Print the _median_ on a new line, to a scale of decimal place (i.e., , ).
3.  Print the _mode_ on a new line. If more than one such value exists, print the numerically smallest one.

**Sample Input**

    10
    64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
    

**Explanation**

**Mean:** 

We sum all elements in the array, divide the sum by , and print our result on a new line.

**Median:** 

To calculate the median, we need the elements of the array to be sorted in either non-increasing or non-decreasing order. The sorted array . We then average the two middle elements:

and print our result on a new line.

**Mode:** 
 
We can find the number of occurrences of all the elements in the array:

 4978 : 1
11735 : 1
14216 : 1
14470 : 1
38120 : 1
51135 : 1
64630 : 1
67060 : 1
73429 : 1
99233 : 1

Every number occurs once, making the maximum number of occurrences for any number in . Because we have multiple values to choose from, we want to select the smallest one, , and print it on a new line.

Welcome to the dark side!
-------------------------

We've introduced a new Dark Mode for a better coding experience.

Test against custom input


[Source](https://www.hackerrank.com/challenges/s10-basic-statistics/problem)