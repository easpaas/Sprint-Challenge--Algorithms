#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```
  a = 0  `O(1) - binding a value`
  while (a < n * n * n):  `O(n) - loops n times`
    a = a + n * n   `0(1) - binding a value`
```
## runtime: O(1+n+1) = O(n) - linear

b)
```
  sum = 0   `O(1) - binding a value`
  for i in range(n):    `O(n) - loops n times`
    j = 1   `O(1) - binding a value`
    while j < n:    `O(n) - loops n times`
      j *= 2    `O(1) - binding a value`
      sum += 1    `O(1) - binding a value`
```

## runtime: O(1+n*n+1+1+1) = O(n**2) - quadratic

c)

## Exercise II


