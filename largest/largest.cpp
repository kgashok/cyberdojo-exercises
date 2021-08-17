#include "largest.hpp"


#include <vector>
#include <numeric>
#include <algorithm>
#include <sstream>


char DELIMITER = '-';

vector<string> split(string str, char delimiter) {

  vector<string> internal;
  stringstream ss(str); // Turn the string into a stream
  string tok;

  while(getline(ss, tok, delimiter)) {
    internal.push_back(tok);
  }

  return internal;
}


string concatenate2 (vector<string>& v, char delim = '.') {

    return accumulate (v.begin(), v.end(), string {},
                        [delim](string& a, string& b) {
                            return a.empty()? b :
                                   delim == '.' ? a+b :
                                   a+delim+b;
                        });

}

string concatenate (vector<string>& v, char delim = '.') {

    string out = "";
    for (string s : v)
        if (delim == '.')
            out += s;
        else
            out += s + delim;

    return delim == '.'? out : out.substr(0, out.length()-1);
}

#include <iterator>

string mergeStrings (string&a, int b) {

    if (a.empty())
        return to_string(b);

    vector<string> as = split (a, '-');
    cout << "string contains: ";
    copy(as.begin(), as.end(), ostream_iterator<string>(cout, ","));
    cout << "merging " << b << endl;

    unsigned long max = 0;
    int pos           = -1;

    for (unsigned int i = 0; i <= as.size(); i++) {
        as.insert(as.begin()+i, to_string(b) );
        string ass = concatenate (as);

        unsigned long val = stol(ass);
        if (max < val) {
            cout << "val: " << val << endl;
            max = val;
            pos = i;
        }
        as.erase (as.begin() + i);
    }

    as.insert(as.begin()+pos, to_string(b));
    string out = concatenate (as, '-');

    cout << out << endl;
    return out;

}

string answer(int numbers[], int size)
{
    string out = "";
    vector<int> vn (numbers, numbers + size);
    out = accumulate(vn.begin(), vn.end(), string{}, mergeStrings);
    cout << out << endl;

    out.erase(std::remove(out.begin(), out.end(), '-'),
               out.end());
    return out;
}













//---------- LEGACY--------------


void tokenize2(std::string str, std::vector<string> &token_v){

    size_t start = str.find_first_not_of(DELIMITER), end=start;

    while (start != std::string::npos){
        // Find next occurence of delimiter
        end = str.find(DELIMITER, start);
        // Push back the token found into vector
        token_v.push_back(str.substr(start, end-start));
        // Skip all occurences of the delimiter to find new start
        start = str.find_first_not_of(DELIMITER, end);
    }
}

void tokenize(std::string str, std::vector<string> &token_v){

    string::size_type end;
    do
    {
        end = str.find(DELIMITER);
        if (end == string::npos)
            end = str.length() + 1;

        token_v.push_back(str.substr(0,end));
        str.replace(0,end+1,"");

    } while (str.length());
}


struct hypen_ws : std::ctype<char> {
    static const mask* make_table() {
    static std::vector<mask> v(classic_table(), classic_table() + table_size);
        v['-'] |= space;  // comma will be classified as whitespace
        return &v[0];
    }
    hypen_ws(std::size_t refs = 0) : ctype<char>(make_table(), false, refs) {}
};

#include <iterator>

vector<string> split2(string str, char) {

  istringstream iss(str); // Turn the string into a stream
  iss.imbue(std::locale(iss.getloc(), new hypen_ws));

  vector<string> internal{istream_iterator<string>{iss},
                      istream_iterator<string>{}};

  return internal;
}

