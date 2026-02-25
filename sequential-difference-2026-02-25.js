/*
Given an array of numbers, return a new array containing the value needed to get from each number to the next number.

For the last number, use 0 since there is no next number.
For example, given [1, 2, 4, 7], return [1, 2, 3, 0].
 */
function findDifferences(arr) {
    const result = []
    const lastElement = arr[arr.length - 1] // start from the end of the array
    let currentElement
    for (let i = arr.length - 1; i >= 0; i--) {
        if (i === arr.length - 1) {
            result[i] = lastElement - arr[i]
        } else {
            result[i] = currentElement - arr[i]
        }
        currentElement = arr[i]
    }
    return result;
}