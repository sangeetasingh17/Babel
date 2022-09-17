## Algorithm

- We use re.finditer() for finding the indices where the match object occurs. As it returns an iterable object, the start() method helps in return the indices or else it would show that a match object has been found at some location.
- The standard method in matching using re module is greedy which means the maximum number of characters are matched. Therefore, the ?={0} helps in minimum number of matches.
- The result is that by adding some modifications, the finditer() method returns a list of overlapping indices.
