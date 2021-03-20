#include <iostream>

using namespace std;

int main(){
	char opcao;

	cout << "Pensei em uma Letra, que letra é ? "<<endl;
	cin>>opcao;


	switch(opcao){
		case 'A' : cout << "Parabéns, acertou !" << endl; break;
		case 'B' : cout << "Errouuuuuuuuu"<< endl; break;
		case 'C' : cout << "Errouuuuuuuuu"<< endl; break;
		default  : cout << "Opcao Invalida"<< endl; break;
	}

	return 0;
}
