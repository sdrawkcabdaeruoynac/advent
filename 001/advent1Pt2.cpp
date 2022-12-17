#include <list>
#include <iostream>
#include <string>
#include <set>

#include "file.h"
#include "elf.h"

using namespace std;

list<Elf> readFile(fstream& file);

int main(int argc, char** argv)
{
    string filename {"/Users/zen/advent/advent/001_2022/001/input.txt"};
    File adventInput {filename};

    list<Elf> ElfRegistry(readFile(adventInput._file)); 
    multiset<Elf> eList; 

    
    for(auto i: ElfRegistry)
        eList.insert(i);

    auto maxPos =  eList.end();
    --maxPos;

    Elf Elf1, Elf2, Elf3; 
    Elf1 = *maxPos;
    Elf2 = *(--maxPos);
    Elf3 = *(--maxPos);
      
    cout << "Most: " << Elf1 << endl
         << "Middle: " << Elf2 << endl
         << "Least: " << Elf3 << endl
         << "Total: " << Elf1.total + Elf2.total + Elf3.total << endl;

   return 0;

}


/**
 *  Dummy function to read from file stream
*/
list<Elf> readFile(fstream& file) {

    list<Elf> collection;

    string calorie; 
    list<calories> clist;
    int n = 0; 

    while(file)
    {
        getline(file,calorie,'\n');

        if(calorie != "")
        {
            calories cal = stoi(calorie);
            clist.push_back(cal);
        }
        else
        {
            Elf elf(to_string(65 + n++),clist);
            elf.sum(clist);
            collection.push_back(elf);
            clist.clear();
        }
    }
    
    return collection;
}

