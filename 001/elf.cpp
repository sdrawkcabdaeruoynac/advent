#include "elf.h"
#include <utility>

using namespace std;


Elf::Elf(){}

Elf::Elf(const string & name, const calorieList & clist): 
elfName(name), elfCalories(clist), total(0)
{}


int Elf::sum(const calorieList& clist)
{
  for(auto i: clist){
    total += i;
  }
}

bool Elf::operator==(const Elf& right) const {
    return elfName == right.elfName &&
           elfCalories == right.elfCalories &&
           total == right.total; 
}

bool Elf::operator<(const Elf& right) const {
    return total < right.total;
}

std::ostream& operator<< (std::ostream& out, const Elf& k)
{
    out << k.elfName << endl;
    out << "{\n";
    for(auto cal: k.elfCalories)
    {
      out << "\t" << cal << endl;
    }
    out << k.total << endl; 
    out << "}" << endl; 
    return  out;
}