#ifndef file_h
#define file_h

#include <fstream>
#include <iostream>
#include <string>
#include <utility>

using namespace std;

struct File{


    std::string fileName; 
    fstream _file;

    File();
    File(const string & name);

    private:
    string fileState(fstream & fileRef);

};


#endif /* file_h */