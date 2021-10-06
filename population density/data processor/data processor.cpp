// data processor.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include "json.hpp"
class CParser {
public:
    bool loadFile(std::string fileName);
    bool parse();
    nlohmann::json dumpToJson();
    //load file
    //parse
    //dump to json
private:

    int icols;
    int irows;
    int xllcorner;
    int yllcorner;
    int cellsize;
    int NODATA_value;

    bool getParams();
    bool linesToPoints(int line);

    std::vector<std::string> vecLines;
    std::vector<std::vector<std::string>> vecPoints;
    std::vector<std::tuple<int, int, int>> data; //x,y,pop
    //parsing functions
    //yeah
};
bool CParser::loadFile(std::string fileName) {
    std::ifstream input(fileName);
    for (std::string line; getline(input, line); ) {
        vecLines.emplace_back(line);
    }
    if (vecLines.empty())
        return false;
    else
        return true;
}
bool CParser::parse() {
    int i = 0;
    std::cout << "Parsing " << vecLines.size() << " lines of data into data array\n";
    for (auto currLine : vecLines) {
        if (currLine.find("ncols") != std::string::npos)
            icols = std::stoi(currLine.substr(14, std::string::npos));
        else if (currLine.find("nrows") != std::string::npos)
            irows = std::stoi(currLine.substr(14, std::string::npos));
        else if (currLine.find("xllcorner") != std::string::npos)
            xllcorner = std::stoi(currLine.substr(14, std::string::npos));
        else if (currLine.find("yllcorner") != std::string::npos)
            yllcorner = std::stoi(currLine.substr(14, std::string::npos));
        else if (currLine.find("cellsize") != std::string::npos)
            cellsize = std::stoi(currLine.substr(14, std::string::npos));
        else if (currLine.find("NODATA_value") != std::string::npos)
            NODATA_value = std::stoi(currLine.substr(14, std::string::npos));
        else
            linesToPoints(i);
        i++;

    }
    std::cout << "Done!\n";
    return  true;
}
bool CParser::linesToPoints(int line) {
    std::string currLine = vecLines.at(line);
    for (int i = 0; i < icols; i++) {
        int density = std::stoi(currLine.substr(0, currLine.find(" ")));
        currLine.erase(0, currLine.find(" ") + 1);
        data.emplace_back(std::tuple< int, int, int >{i , 1211 - (line - 6), density });
    }
    return true;
}
nlohmann::json CParser::dumpToJson() {
    nlohmann::json dumpObj;
    std::cout << "Converting " << data.size() << " entries into json\n";
    for (auto const& [x, y, z] : data) {
            nlohmann::json pointObj;
            pointObj["x"] = x;
            pointObj["y"] = y;
            pointObj["density"] = z;

            dumpObj += pointObj;
    
    }
    return dumpObj;
}
int main()
{

    CParser census;
    if (!census.loadFile("UK_residential_population_2011_1_km.asc")) {
        std::cout << "File failed to load, please ensure 'UK_residential_population_2011_1_km.asc' is in the correct directory\n";
        return 0;
    }
    census.parse();
    std::string dump = census.dumpToJson().dump();
    std::ofstream out("output.txt");
    out << dump;
    out.close();
    std::cout << "Done!\nPress enter to continue";
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started:
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
