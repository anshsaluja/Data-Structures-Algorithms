class Solution {
    public boolean isPalindrome(int x) {
        int m = x;
        int y = 0;
        if(x<0)
        {
            return false;
        }
        while(m!=0)
        {
            int j = m%10;
            y = y*10 +j;
            m=m/10;


        }
        if(y==x)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}