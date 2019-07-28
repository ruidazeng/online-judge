#include <bits/stdc++.h>
using namespace std;
#define PI 3.14159265

int main()
{
    int T;
    cin >> T;
    for(int t = 0; t < T; ++t){
        int moves;
        cin >> moves;
        double xdir = 0, ydir = 0;
        // facing Y direction
        double angle = 90;
        for(int mov = 0; mov < moves; ++mov){
            double ang;
            double dist;
            cin >> ang >> dist;
            angle += ang;
            xdir += (dist * cos(angle * PI / 180));
            ydir += (dist * sin(angle * PI / 180));
        }
        cout << setprecision(7) << xdir << " " << ydir << endl;
    }
    return 0;
}