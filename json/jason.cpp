#include "jason.hpp"


#include <sstream>
#include <cstring>

std::pair<string, string>
extractFromInput(stringstream& ss)
{

    //temporary buffer
    const unsigned int BUFFERSIZE = 256;
    char buffer[BUFFERSIZE];
    memset(buffer, 0, BUFFERSIZE * sizeof(char));

    //returnValue.first holds the variables name
    //returnValue.second holds the variables value
    std::pair<std::string, std::string> returnValue;

    //read until a opening variable quote sign appears
    ss.get(buffer, BUFFERSIZE, '\'');
    //and ignore it (go to next position in stream)
    ss.ignore();

    //read variable token excluding the closing variable quote sign
    ss.get(buffer, BUFFERSIZE, '\'');
    //and ignore it (go to next position in stream)
    ss.ignore();
    //store the variable name
    returnValue.first = buffer;

    //read until opening value quote appears(skips the : sign)
    ss.get(buffer, BUFFERSIZE, '\'');
    //and ignore it (go to next position in stream)
    ss.ignore();

    //read value token excluding the closing value quote sign
    ss.get(buffer, BUFFERSIZE, '\'');
    //and ignore it (go to next position in stream)
    ss.ignore();
    //store the variable name
    returnValue.second = buffer;

    //do something with those extracted values
    std::cout << "Read " << returnValue.first<< " = " << returnValue.second<< std::endl;

    return returnValue;

}

// Input : {'firstname' : 'abc'}
// Output : firstname -> abc
#include <map>

string parse(string input)
{
    string key;
    string value;

    string res;

    std::stringstream ss(input);
    map <string, string> out;

    //read until the opening bracket appears
    while(ss.peek() != '{')
    {
        //ignore the { sign and go to next position
        ss.ignore();
    }

    while (ss.peek() != '}') {
        std::pair<string, string> r = extractFromInput (ss);
        if (r.first.length() != 0)
            out[r.first] = r.second;
        else
            break;
    }

    cout << "----------- building output ---------" << endl;
    cout << "count: " << out.size() << endl;
    for (auto i: out) {
        cout << i.first << " -> " << i.second << endl;
        res = res + i.first + " -> " + i.second + " ";
    }

    return res.substr(0, res.length() -1);  // trimming the last whitespace

}
