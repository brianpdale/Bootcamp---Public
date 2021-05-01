function evensOfOdds(arr) {
    var totalOdds = 0;
    var totalEvens = 0;
        for(var i = 0; i < arr.length; i++){
        if(arr[i] % 2 === 0)
        totalEvens += 1
        if(arr[i] % 2 === 1)
        totalOdds += 1}
        {
        if(totalOdds > totalEvens)
        return("odds are larger")}
        {if(totalOdds < totalEvens)
        return("evens are larger")}
        {if(totalOdds = totalEvens)
        return("tied")}
        }
var result = evensOfOdds([6, 8, 3, 10, -2, 5, 9]);
console.log(result);