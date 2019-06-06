public boolean makeBricks(int small,int big,int goal){
    return goal%5 <= small && goal<=small+(5*big);
}