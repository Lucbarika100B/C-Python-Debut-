/*-- Bibliotheques utilisees --*/
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Declaration des fonctions utilisees dans le main
int demanderNombre(string message);
float moyenne (int[], int);
int factoriel (int) ;
int est_premier (int); // retourne "est premier" ou "n'est pas premier"
const int TAILLE_TABLEAU = 7 ;
float ecart_type(int tab[],int n);
int lireValeurs(int valeurs []);

int main()
{
    /*
    La fonction main de ce programme existe deja et fait office de liste de problemes.

    En fait, vous n'avez qu'a completer les fonctions qui la suivent et decommenter
      les tests (l'utilisation de la fonction) dans le main.
      (pour decommenter, retirer simplement les // devant la ligne
    */

    // Declaration des variables locales
    int ma_suite [] = {3, 5, 7, 4, 9, 10, 11} ;
    int nombre = 6;


     cout << "La moyenne de ma suite est de " << moyenne(ma_suite, TAILLE_TABLEAU) << endl << endl;

     nombre = demanderNombre("Verification si un nombre est premier");
     cout << "Le nombre " << nombre << " " << est_premier(nombre) << endl << endl;

     nombre = demanderNombre("Calcul de la factorielle");
     cout << "Le factoriel de " << nombre << " est " << factoriel(nombre) << endl << endl;
     cout << "L'ecart-type de ma suite est " << ecart_type(ma_suite, TAILLE_TABLEAU) << endl << endl;


    cout << "La fonction lire valeurs prend des entiers en entrée et les met dans un tableau" << endl;
    cout << "La premiere valeur que vous inscrivez correspond au nombre d'elements a inscrire ensuite. Eg si je rentre 2 je dois rentrer deux chiffres  a chaque ligne." <<endl;
    int valeurs [1000];
    int taille = lireValeurs(valeurs);
    cout << "L'ecart-type des valeurs lues est:" << ecart_type(valeurs,taille) << endl << endl;

    return 0;
}

int lireValeurs(int valeurs[]) {
    int userInput;
    cin >> userInput;

    for (int i = 1; i <= userInput; i++) {
        cin >> valeurs[i-1];
    }
    return userInput;
}

int demanderNombre(string message)
{
    int nombre;
    cout << message << endl;
    cout << "Entrez un nombre : " << endl;
    cin >> nombre;

    return nombre;
}


float moyenne (int tab [],int n)
{
    int sum = 0;
    for(int i = 0; i < n; i ++) {
     sum = sum + tab[i];
    }
      int average = sum / n;
      return average;
}

float ecart_type(int tab[],int n){


    float avg = moyenne(tab, n);
    double sum = 0.0;
    for(int i =0; i<n; i++){
        sum = (sum + ((tab[i]-avg)) * (tab[i] - avg));
    }
     double eqtype = sqrt(sum/n);
     return eqtype;
}


int factoriel(int n)
{
    int facto = 1;
    for( int i = 1; i <= n; i ++){
        facto = facto * i;
    }
    return facto;
}

int est_premier (int n)
{
    int i, z, m =0;
    int flag =0;

    m = n/2;
    for (int i = 1; i <=m; i++) {
    if(m%z == 0){
        cout << "Number is NOT prime"<< endl;
        flag = 1;
        break;
            }
    } if(flag == 0){
        cout << "Number is PRIME" << endl;
    }


    return 0;   // a remplacer
}
