"""Problem: Single Element in sorted Array.

Question: You are given a sorted array consisting of only integers,
where every element appears exactly twice,
except for one element which appears exactly once.
Find this single element that appears only once.

Here it easily seems that you just need to traverse the array,
and if you don’t find its duplicate next to it,
you get that element which is single.
This procedure takes time complexity of O(n).
But the twist lies here, you are given some constraints on it, and they are:
your solution should run in O(log n) time and O(1) space.

O(1) means you are not allowed to use extra space i.e. constant space.
Let's define some terms before our solution:

Indexing: Indexing means assigning position to the element in an array ->
0 based indexing means first element of array is having index 0,
and other elements after it have 1, 2, 3 and so on.

Pair: Here pair is the combination of two same element (values like (2, 2)).
1st element of this pair is called the leader and 2nd element is called Follower.

In Simple Binary Search Algorithm we divide the array into two half from mid-element,
and then decide whether to go in first half or second half on the basis
of comparing the value of mid-element and the element that we are given to search for.

We use this concept to solve out problem:-

Let's take an Example Array: [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]

Similarly in this problem, we divide the array in two half from mid element:
[1, 1, 2, 2, 3, 4, 4, 5(mid), 5, 6, 6, 7, 7, 8, 8] and position of elements are:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Now here we get stuck where to go in second half or first half after dividing the array
since we don’t know in which half that single element is in ?

So here lies the application of indexing based on 0 for finding that single element:-

Consider if array was appropriate, and it had no single element
[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8] then our middle element
would be 4 and is a follower as well as it is on odd index.

So point to understand here, when array is appropriate:
if element is a follower then it must be on odd index.

But in our case [1, 1, 2, 2, 3, 4, 4, 5(mid), 5, 6, 6, 7, 7, 8, 8]
5 becomes the middle element and 5 here is leader, but contradictory
it comes on odd index whereas it should have been on even index
to be a leader of appropriate array.

Now from the above observation we can conclude that:

If mid-element comes on odd index then it should have
its leader of same value next of it.

If leader exists then Single element would in second half
(because every element upto mid is in its position)
If leader does not exist then single element lies in first half
(which is same in our case)
Thus this suggests us that we should continue search in first half

At some point while applying this algorithm we will only be left
with 3 elements and add that time,
we need just to compare our mid-element with its previous element
and its succeeding element
and the element which does not match to mid will be our answer.

Let's take and Example from above array:
[1, 1, 2, 2, 3, 4, 4, 5(mid), 5, 6, 6, 7, 7, 8, 8]
Here, mid = 5 since mid is on odd index
(for appropriate array, follower should be on odd index as discussed earlier)
it must have its leader ahead, but we get 4 which is not the leader for 5,
Thus we go to first half for further search.

1st step: [1, 1, 2, 2, 3, 4, 4]
2nd step: [3, 4, 4]

Here, mid = 2 and is on odd index, thus we check for element ahead of it,
and we get 2 as it leader of mid, so we can say that every element
before mid is on its position. Thus, we go to second half

Here, mid = 4 but here only 3 elements are left and 3 (element of array)
doesn't match with mid, hence we came to know that 3 is the single element here.
"""


def single_not_dub(arr: list[int]) -> int:
    lf: int = 0
    rt: int = len(arr) - 1

    # when array contains only one element, and it is the answer itself.
    if len(arr) == 1:
        return arr[0]

    # 1. Start main binary search loop.
    while lf <= rt:
        mid: int = lf + (rt - lf) // 2

        # 2. Boundary conditions: simply checking the overflow condition,
        # when index is close to end left or right.
        if mid + 1 < len(arr):
            # checking if element next to mid is same or not.
            if arr[mid] != arr[mid + 1]:
                if mid < 1:
                    return arr[mid]

                # since element after and before
                # they are not same, the mid is answer itself.
                if arr[mid] != arr[mid - 1]:
                    return arr[mid]
        elif mid >= 1 and arr[mid] != arr[mid - 1]:
            return arr[mid]

        # 3. Define the half where single elements exist,
        # when mid-position is odd therefore it should be follower.
        if mid % 2 == 1:
            # Since mid is follower and if leader is found next to it,
            # then we change the value of low to mid +1
            # as we go in second half.
            if arr[mid] == arr[mid - 1]:
                lf = mid + 1
            # if leader is not found next then we go for first half,
            # and change the value of high for first half to mid-1.
            else:
                rt = mid - 1
        elif arr[mid] == arr[mid + 1]:
            lf = mid + 1
        else:
            rt = mid - 1
    return -1


def main() -> None:
    arr1: list[int] = []
    arr2: list[int] = [1]
    arr3: list[int] = [1, 1]
    arr4: list[int] = [
        1,
        1,
        2,
        2,
        3,
        3,
        4,
        4,
        5,
        5,
        6,
        6,
        7,
        7,
        8,
        8,
        22,
        22,
        88,
        88,
        99,
        99,
        100,
        100,
        150,
        150,
        200,
        200,
    ]
    arr5: list[int] = [
        1,
        1,
        2,
        2,
        3,
        3,
        4,
        4,
        5,
        5,
        6,
        6,
        7,
        7,
        8,
        8,
        22,
        22,
        88,
        88,
        99,
        99,
        100,
        100,
        150,
        150,
        200,
    ]

    print(single_not_dub(arr1))
    print(single_not_dub(arr2))
    print(single_not_dub(arr3))
    print(single_not_dub(arr4))
    print(single_not_dub(arr5))


if __name__ == "__main__":
    main()
