class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> rad,dire;
        // iterate and get rad or dire position
        for(int i=0;i<senate.size();i++) {
            // if the senate of i is R, push to rad queue
            if(senate[i]=='R')
                rad.push(i);
            // if senate of i is D, push to dire queue
            else
                dire.push(i);
        }
        // check if rad or dire is not empty and operate
        while(!rad.empty() && !dire.empty()) {
            // reference the first element of the rad queue
            int ri = rad.front();
            rad.pop();
            // reference first element of dire queue
            int di = dire.front();
            dire.pop();
            if(ri<di) {
                rad.push(ri+senate.size());
            } else{
                dire.push(di+senate.size());
            }
        }
        // return the output based on queue left with most element
        return (rad.size()>dire.size()) ? "Radiant":"Dire";
    }
};