/*-- Bibliotheques utilisees --*/
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

// Declaration des fonctions utilisees dans le main
int racine(int n);      // exemple d'algo vu dans la presentation 8
int racine2(int n);     // exemple d'algo vu dans la presentation 8
bool rechercheLineaire (int tableau [], int longueurTableau, int valeur);
//void printArray(int arr[], int n);                                                                        // exemple d'algo vu dans la presentation 8
//int smallValue(int arr[], int start, int tailleArr);
//Manquant:

//    -tri par sélection et échanges
//    -tri par bulles
//    -recherche dichotomique
//    -crible d'Ératosthène
//    -somme de 3 cubes

int arrTab []  = {700, 400, 900, 800, 450} ;
int arrLen = 5;
int val = 15;
int start = 0;


int main()
{

    cout<<"Test de la fonction racine"<<endl;
    cout<< racine(49) <<endl;

    cout << "----------------------------" <<endl;

    cout<<"Test fonction racine2" <<endl;
    cout<< racine2(36) << endl;

    cout << "----------------------------" <<endl;

    cout<<"Test de la fonction Recherche lineaire"<<endl;
    cout<< rechercheLineaire(arrTab, arrLen, val) << endl;

        cout << "----------------------------" <<endl;

    //cout<<"Test de la fonction Tri de selection "<<endl;
    //cout<< smallValue(arrTab, start, arrLen) << endl;

        cout << "----------------------------" <<endl;
    cout << "Test de la fonction sort array" << endl;



    //cout<< printArray(arrTab, arrLen) << endl;

    // Ce laboratoire est un peu different...
    // vous avez maintenant a cree votre propre main pour tester vos fonctions

    // vous remarquerez que ce fichier inclut les fonctions vues dans la presentation de ce matin

    // il reste maintenant a y ajouter l'algorithme de recherche manquant ainsi que les 2 algorithmes de tri.

	// De plus, ajoutez un algorithme de recherche de nombres premiers avec tableau (crible d'Ératosthène)

	// Finalement, écrivez un algorithme qui détermine si un nombre naturel peut être la somme de 3 cubes.
	// Si c'est possible, affichez les 3 nombres en question.
    // À noter, un nombre qui peut être écrit de la forme 9k+4 ou 9k+5 ne pourra jamais être la somme
    // de 3 cubes. (4,5,13,14,22,23,31,32... sont donc exclus).
    // Les nombres qui constituent la somme peuvent être positifs ou négatifs.
    // Posez des limites à votre recherche (par exemple, les nombres entre 100 et -100).

    return 0;
}

int racine (int n)
{
    int supposition = 1;
    while (supposition * supposition <= n)
    {
        supposition = supposition + 1;
    }
    return supposition - 1;
}

int racine2 (int n)
{
    int approx = 2;
    while (abs((n / approx) - approx) > 1)
    {
        approx = (approx + (n / approx)) / 2;
    }
    return approx;
}

bool rechercheLineaire (int tableau [], int longueurTableau, int valeur)
{
    bool trouve = false;
    for (int i=0;i<longueurTableau;i++)
    {
        if(tableau[i] == valeur)
        {
            trouve = true;
        }
    }
    return trouve;
}



int sortManually(int arr[], int tailleArr) {

    int n = sizeof(arr)/sizeof(arr[0]);
    sort(arr, arr+n);

    for(int i = 0; i < tailleArr; i++){
        cout<<arr[i] <<" ";
    }
   return 0;
}




