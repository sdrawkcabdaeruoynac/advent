#include "item.h"
#include <utility>

using namespace std;


Items::Items(){}
Items::Items(int dep): depth(dep){}

bool Items::operator==(const Items& right) const {
    return depth == right.depth;
}

bool Items::operator<(const Items& right) const {
    return (depth < right.depth);
}

std::ostream& operator<< (std::ostream& out, const Items& k)
{
    out << k.depth;
    return  out;
}