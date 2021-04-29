#include<iostream>
using std::string;

class Employee{
  public:
    std::string Nome;
    std::string Company;
    int age;

    void IntroduceYourSelf(){
        std::cout<<"My Name - "<<Nome<<std::endl;
        std::cout<<"Companhia - "<<Company<<std::endl;
        std::cout<<"idade - "<<age<<std::endl;
    }
    
    Employee(string name, string company, int age){
        Nome = name;
        Company = company;
        age =age;
    }
};


int main(){
    Employee employee1("Diego", "PyCoorp", 33);
   // employee1.Nome = "Diego";
   // employee1.Company = "PyCoorp";
   // employee1.age = 33;

    employee1.IntroduceYourSelf();

   // Employee employee2;
    //employee2.Nome = "Tiago";
    //employee2.Company = "Google";
   // employee2.age = 45;

    //employee2.IntroduceYourSelf();
}

