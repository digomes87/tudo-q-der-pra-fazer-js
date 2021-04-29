#include<iostream>

using namespace std;

int main(){
	int age;
	float altura;
	cout << "Informe tua idade forasteiro: "<<endl;
	cin>>age;
	cout << "Informe tua altura: "<< endl;
	cin>>altura;

	if(age > 18){
		cout << "Maior de idade"<< endl;
	}else{
		cout << "Menor de Idade"<< endl;
	}


	if(altura >= 1.90){
		cout << "Alto, jogador de volei"<< endl;
	}else {
		cout << "Altura considerada normal "<< endl;
	}


	return 0;
}

