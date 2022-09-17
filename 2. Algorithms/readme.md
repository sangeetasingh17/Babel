## Task

1. You are given a string A

2. Your task is to find the indices of the start and end of string b in A

Input Format :

1. The first ne contains the string
2. The second line contains the string

Constraints :

Output Format :

1. Print the tuple in this format (start_index, end_index)
2. if no match is found, print (-1,-1)

Sample Input :

```
cccdec
cc
```

Sample Output:

```
(0,1)
(1,2)
(4,5)
```

## Algorithm :

- We use re.finditer() for finding the indices where the match object occurs. As it returns an iterable object, the start() method helps in return the indices or else it would show that a match object has been found at some location.
- The standard method in matching using re module is greedy which means the maximum number of characters are matched. Therefore, the ?={0} helps in minimum number of matches.
- The result is that by adding some modifications, the finditer() method returns a list of overlapping indices.
