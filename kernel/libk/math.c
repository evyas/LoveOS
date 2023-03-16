int sqrt(int num) {
    int temp = 0, sqrt;
    int number = num;
    sqrt = number / 2;
 
    while(sqrt != temp){
        temp = sqrt;
        sqrt = (number/temp + temp) / 2;
    }
   
   return sqrt;
}