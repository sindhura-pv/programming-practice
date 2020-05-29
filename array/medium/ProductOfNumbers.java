class ProductOfNumbers {
    
    ArrayList<Integer> nums;
    int last, zero;

    public ProductOfNumbers() {
        
        nums = new ArrayList<>();
        last = 1;
        zero = -1;
        
    }
    
    public void add(int num) {
        if(num==0){
            zero = nums.size();
            nums.add(num);
            last = 1;
        } else{
            nums.add(last*num);
            last *= num;
        }
    }
    
    public int getProduct(int k) {
        if(nums.size()-k <= zero){
            return 0;
        }
        if(k==nums.size()){
            return last;
        }
        int prev = Math.max(1, nums.get(nums.size()-k-1));
        return (int)(last/prev);
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */
