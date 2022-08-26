#include <cmath>
#include <iostream>
#include <string>

using namespace std;

// declaration des fonctions utilisees
float moyenne (float, float);
float moyenne_int (int, int);
float valeur_absolue (float);
void afficher_multiples (int,int);
int racine_entiere(int);
void dessiner_ligne_etoiles (int);
void dessiner_double_fleches (int);
void dessiner_fleche_haut (int);
void dessiner_fleche_bas (int);
void dessiner_carre (int);

int main ()
{
    /*
    La fonction main de ce programme existe deja et fait office de liste de probleme.

    En fait, vous n'avez qu'a completer les fonctions qui la suivent et decommenter
      les tests (l'utilisation de la fonction) dans le main.
      (pour decommenter, retirer simplement les // devant la ligne
    */

    cout << endl << "Tests pour la fonction moyenne." << endl
         << "-------------------------------" << endl;
    cout << "Calcul de la moyenne de 3.5 et 10 : " << moyenne(3.5,10) << endl;
    cout << "Calcul de la moyenne de 10 et 3 : " << moyenne(10,3) << endl;
    cout << "Calcul de la moyenne de 10 et 3.5 : " << moyenne(10,3.5) << endl;


    cout << endl << "Tests pour la fonction moyenne_int." << endl
         << "-----------------------------------" << endl;
    cout << "Calcul de la moyenne de 3 et 10 : " << moyenne_int(3,10) << endl;
    cout << "Calcul avec 3 et 2 : " << moyenne_int(3,2) << endl;
    cout << "Calcul avec 2 et 3 : " << moyenne_int(2,3) << endl;

    cout << endl << "Tests pour la fonction valeur_absolue." << endl
         << "--------------------------------------" << endl;
    cout << "Valeur absolue de 3 : " << valeur_absolue(3) << endl;
    cout << "Valeur absolue de -3 : " << valeur_absolue(-3) << endl;
    cout << "Valeur absolue de 0 : " << valeur_absolue(0) << endl;

    cout << endl << "Tests pour la afficher_multiples." << endl
         << "--------------------------------------" << endl;
    cout << "Multiples de 3 : ";
    afficher_multiples(3,100) ;
    cout<< endl;
    cout << "Multiples de 3 :";
    afficher_multiples(17,100);
    cout<< endl;
    cout << "Multiples de 3 : ";
    cout<< endl;
    afficher_multiples(50,100);
    cout<< endl;

    cout << endl << "Tests pour la racine_entiere." << endl
         << "--------------------------------------" << endl;
    cout << "Racine de 19 : " << racine_entiere(19) << endl;
    cout << "Racine de 25 : " << racine_entiere(25) << endl;
    cout << "Racine de 8900 : " << racine_entiere(8900) << endl;

    cout << endl << "Tests pour la fonction dessiner_lignes_etoiles." << endl
                 << "-----------------------------------------------" << endl;
    cout << "0 etoile   " ;
    dessiner_ligne_etoiles(0);
    cout << endl << "1 etoile   " ;
    dessiner_ligne_etoiles(1);
    cout << endl << "5 etoiles  " ;
    dessiner_ligne_etoiles(5);
    cout << endl << "10 etoiles " ;
    dessiner_ligne_etoiles(10);

   cout << endl << "Tests pour les dessins de figures : " << endl
        << "------------------------------------" << endl;
   cout << "Test -> fleche haut " << endl;
   dessiner_fleche_haut(7);
   cout << endl << "Test -> fleche bas " << endl;
   dessiner_fleche_bas(7);
   cout << endl << "Test -> double fleches " << endl;
   dessiner_double_fleches(7);
   cout << endl << "Test -> carre" << endl;
   dessiner_carre(10);
   return 0;
}


void dessiner_ligne_etoiles (int n)
{
    for(int i = 0; i <= n; i++){
            if(n == 0){
            cout << " ";
        }else if (n == 1) {
            cout << "*";
        }else if (n == 5) {
            cout << "*****";
        }else if (n == 10){
            cout  << "**********";
        }
        return;
    }

}

float moyenne (float x, float y)
{
    return (x+y)/2;   // a remplacer
}

float moyenne_int (int a, int b)
{
    return (a+b)/2;   // a remplacer
}

int racine_entiere (int n){
    if(n<0){
        return 0;
    }else if (n > 0){
        return n ;
    }
}

void afficher_multiples (int a, int b){

    if(a % 3 == 0){
        cout << endl << "Ce entier est un multiple de 3";
    } else cout << endl << " Ce entier N'EST PAS MULTIPLE DE 3";
    return ;
}

void dessiner_espaces(int taille)
{

}

float valeur_absolue (float x)
{
    if(x > 0){
        return x;
    } else if ( x < 0) {
     return (x);
    } else if (x == 0) {
     return 0;
    } else
    cout << endl <<  "No absolute value for your input";
}



//Fonctions dessiner...
//n doit être supérieur ou égal à 5
//n doit être impair
//Tentez de comprendre cette solution pour faire les suivantes.
void dessiner_fleche_haut (int n)
{
   for (int i=1;i<=n;i=i+2)
   {
    dessiner_espaces (n/2+1 -(i/2) -1);

    dessiner_ligne_etoiles(i);
   }

   for(int i=0;i<4;i++)
   {
       cout<<"  ";
       dessiner_ligne_etoiles(n-4);
   }
}

void dessiner_fleche_bas (int n)
{
}

void dessiner_double_fleches (int n)
{
}

void dessiner_carre (int n)
{
}

