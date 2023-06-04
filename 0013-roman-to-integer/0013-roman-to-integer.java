class Solution {
    public int romanToInt(String s) {
        char[] romanArr= s.toCharArray();
        int len=romanArr.length;
        int FinalValue = 0;
        int curVal, nextVal;
        for(int i=0; i<len; i++){
            curVal = value(romanArr[i]);
            if(i!=len-1){
                nextVal = value(romanArr[i+1]);
            }else{
                nextVal = 0;
            }
            if(curVal>=nextVal){
                FinalValue = FinalValue + curVal;
            }else{
                FinalValue = FinalValue - curVal;
            }
        }
        return FinalValue;
    }
        
        public static int value(char num) {
            if(num == 'I'){
                return 1;
            }
            if(num == 'V'){
                return 5;
            }else if(num == 'X'){
                return 10;
            }else if(num == 'L'){
                return 50;
            }else if(num == 'C'){
                return 100;
            }else if(num == 'D'){
                return 500;
            }else if(num == 'M'){
                return 1000;
            }else {
                return -1;
            }
        }
}