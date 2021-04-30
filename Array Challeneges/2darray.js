            function flatten(arr2d){
                var flat =[];{
                for(var i = 0; i < arr2d.length; i++)
                for(var x = 0; x < arr2d[i].length; x++){
                flat.push(arr2d[i][x])}
                return flat
            }
        }
    
                
            var result = flatten( [ [2, 5, 8], [3, 6, 1], [5, 7, 7] ] );
            console.log(result);