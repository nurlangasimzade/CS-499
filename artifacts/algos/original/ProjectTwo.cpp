
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <cctype>
using namespace std;

static inline string ltrim(const string &s) {
    size_t start = s.find_first_not_of(" \t\r\n");
    return (start == string::npos) ? "" : s.substr(start);
}
static inline string rtrim(const string &s) {
    size_t end = s.find_last_not_of(" \t\r\n");
    return (end == string::npos) ? "" : s.substr(0, end + 1);
}
static inline string trim(const string &s) {
    return rtrim(ltrim(s));
}

struct Course {
    string courseNumber;
    string courseTitle;
    vector<string> prerequisites;
};

string ToUpper(const string& str) {
    string upper = str;
    for (char &c : upper) c = toupper(static_cast<unsigned char>(c));
    return upper;
}

map<string, Course> LoadCourses(const string& filename) {
    map<string, Course> courses;
    ifstream file(filename);

    if (!file.is_open()) {
        cerr << "Error: Could not open file " << filename << endl;
        return courses;
    }

    string line;
    while (getline(file, line)) {
        if (line.empty()) continue;

        stringstream ss(line);
        string courseNum, courseTitle, prereq;
        vector<string> prereqs;

        if (!getline(ss, courseNum, ',')) continue;
        if (!getline(ss, courseTitle, ',')) continue;

        courseNum = trim(courseNum);
        courseTitle = trim(courseTitle);

        while (getline(ss, prereq, ',')) {
            prereq = trim(prereq);
            if (!prereq.empty()) prereqs.push_back(ToUpper(prereq));
        }

        Course c;
        c.courseNumber = ToUpper(courseNum);
        c.courseTitle = courseTitle;
        c.prerequisites = prereqs;
        courses[c.courseNumber] = c;
    }

    file.close();
    return courses;
}

void PrintCourseList(const map<string, Course>& courses) {
    vector<string> keys;
    keys.reserve(courses.size());
    for (auto const& pair : courses) {
        keys.push_back(pair.first);
    }
    sort(keys.begin(), keys.end());

    cout << "Here is a sample schedule:\n" << endl;
    for (const auto& key : keys) {
        const auto &c = courses.at(key);
        cout << c.courseNumber << ", " << c.courseTitle << endl;
    }
    cout << endl;
}

void PrintCourseInfo(const map<string, Course>& courses, const string& courseNumber) {
    string upperCourse = ToUpper(courseNumber);
    auto it = courses.find(upperCourse);
    if (it != courses.end()) {
        cout << it->second.courseNumber << ", " << it->second.courseTitle << endl;
        cout << "Prerequisites: ";
        if (!it->second.prerequisites.empty()) {
            for (size_t i = 0; i < it->second.prerequisites.size(); ++i) {
                cout << it->second.prerequisites[i];
                if (i < it->second.prerequisites.size() - 1) cout << ", ";
            }
            cout << endl;
        } else {
            cout << "None" << endl;
        }
        cout << endl;
    } else {
        cout << courseNumber << " not found.\n" << endl;
    }
}

int main() {
    map<string, Course> courses;
    string filename;
    int choice = 0;

    cout << "Welcome to the course planner." << endl;

    while (choice != 9) {
        cout << "\n1. Load Data Structure." << endl;
        cout << "2. Print Course List." << endl;
        cout << "3. Print Course." << endl;
        cout << "9. Exit" << endl;
        cout << "\nWhat would you like to do? ";

        if (!(cin >> choice)) {
            cin.clear();
            cin.ignore(10000, '\\n');
            cout << "\nThat is not a valid option.\n" << endl;
            continue;
        }

        switch (choice) {
            case 1:
                cout << "\nEnter file name: ";
                cin >> std::ws;
                getline(cin, filename);
                filename = trim(filename);
                courses = LoadCourses(filename);
                if (!courses.empty()) {
                    cout << "\nData loaded successfully.\n" << endl;
                }
                break;
            case 2:
                if (courses.empty()) {
                    cout << "\nNo data loaded. Please load a file first.\n" << endl;
                } else {
                    PrintCourseList(courses);
                }
                break;
            case 3:
                if (courses.empty()) {
                    cout << "\nNo data loaded. Please load a file first.\n" << endl;
                } else {
                    cout << "\nWhat course do you want to know about? ";
                    string courseNum;
                    cin >> courseNum;
                    cout << endl;
                    PrintCourseInfo(courses, courseNum);
                }
                break;
            case 9:
                cout << "\nThank you for using the course planner!" << endl;
                break;
            default:
                cout << "\n" << choice << " is not a valid option.\n" << endl;
        }
    }

    return 0;
}
