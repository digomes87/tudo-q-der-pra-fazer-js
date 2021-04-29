#include<iostream>

using namespace std;

int main() {
	int x, z;
	cout<< "Informe um numero: "<< endl;
	cin>>x;

	cout<< "Informe outro numero: "<< endl;
	cin>>z;

	int diminui = x-z;
	int soma = x+z;
	int multiplicacao = x*z;
	float divisao = x*z;
	int restoDeDivisao = x%z;


	cout << "A soma: " << soma <<endl;
	cout << "A divisao: " << divisao <<endl;
	cout << "A multiplcacao: " << multiplicacao <<endl;
	cout << "Subtraindo os dados, resultado: "<< diminui << endl;
	cout << "Resto de divisao: "<<restoDeDivisao << endl;
	return 0;
} 
