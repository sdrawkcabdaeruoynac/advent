#ifndef item_h
#define item_h

#include <iostream>

using namespace std;

struct Items {
    
    int depth;
    char dep;

    Items();
    Items(int dep);
    
    bool operator==(const Items&) const;
    bool operator<(const Items&) const ;
};

std::istream& operator>> (std::istream& in, const Items& k);
std::ostream& operator<< (std::ostream& out, const Items& k);

#endif /* item_h */


