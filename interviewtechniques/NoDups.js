/**
 * @param {number[]} nums
 * @return {boolean}
 */

var containsDuplicate = function(nums) {
    // creates a set of numbers
    let numbers = new Set();

    //loops over all numbers in the array
    for(let num of nums) {

        //checks if the number is in Set
        if(!numbers.has(num)) {
            // add to Set if not
            numbers.add(num)
        } else {
            return true;
        }
    }

    //if no duplicates
    return false;
};

