function getSecondLargest(nums) {
    // Complete the function
    var i=0;
    var max=nums[i];
    while (i<nums.length){
    if (nums[i]>max){
        max=nums[i]
    }
    i++;
    }
    var j=0;
    var secondMax=0;
    while (j<nums.length){
        if (max>nums[j] && secondMax<nums[j]){
            secondMax=nums[j];
        }
        j++;
    }
    return (secondMax);
}
