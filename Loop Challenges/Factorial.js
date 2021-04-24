var product = 2
{
    for(var i= 1; i<100000000; i=(product++))
    product = product * i;

    console.log(i)}
