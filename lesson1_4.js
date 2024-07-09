var calc ={};
calc.add=function(a,b){
    return a+b;
}
console.log(' Before splitting into modules -' +
    'the result of calling calc.add funtion : %d',
    calc.add(10,10));