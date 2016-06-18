from random import randint

def swap(arr, a, b):
  temp = arr[a]
  arr[a] = arr[b]
  arr[b] = temp

def quicksort(arr):

  def qs(left, right):

    if left < right:
      swap(arr, left, randint(left, right))
      pivot_value = arr[left]
      m = left

      for i in range(left + 1, right + 1):
        if arr[i] < pivot_value:
          m += 1
          swap(arr, i, m)

      swap(arr, left, m)
      qs(left, m - 1)
      qs(m + 1, right)

  qs(0, len(arr) - 1)
  return arr

if __name__ == "__main__":

  arr = [1,5,1,2,2,51,251,5,7,3,6,2,2]

  quicksort(arr)

  print(arr)