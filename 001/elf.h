#ifndef elf_h
#define elf_h

#include <iostream>
#include <list>

using namespace std;

typedef int calories;
typedef list<calories> calorieList;

struct Elf {
    
    string elfName;
    calorieList elfCalories;
    calories total; 

    Elf();
    Elf(const string & name, const calorieList & clist);

    int sum( const calorieList& clist);
    
    bool operator==(const Elf&) const;
    bool operator<(const Elf&) const ;
};

std::istream& operator>> (std::istream& in, const Elf& k);
std::ostream& operator<< (std::ostream& out, const Elf& k);

#endif /* elf_h */