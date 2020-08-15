class Solution {
public:
    bool judgeCircle(string moves) {
        int cU,cD,cL,cR;
        cU = count(moves.begin(),moves.end(),'U');
        cD = count(moves.begin(),moves.end(),'D');
        cL = count(moves.begin(),moves.end(),'L');
        cR = count(moves.begin(),moves.end(),'R');
        if( cU == cD && cL == cR){
            return true;
        }
        else{
            return false;
        }
    }
};