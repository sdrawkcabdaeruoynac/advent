#include "file.h"

using namespace std;

// empty File object
File::File(){}

// opens access to fileName
File::File(const string& name):
fileName()
{
   _file = fstream(name, ios::in | ios::out);
   cout << fileState(_file) << endl;
}
 
// checks if file exists
string File::fileState(fstream & fileRef)
{
  if(_file.fail())
    return "!!! FILE NOT FOUND !!!";
  else
    return "!!! ADVENT INPUT TXT IMPORTED SUCCESSFULLY!!!";
}

