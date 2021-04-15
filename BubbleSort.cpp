// Algorithme de tri type Bubble Sort (optimisé)
//

#include <iostream>
#include <random>
#include <ctime>
#include <algorithm>

using namespace std;

int main()
{
    cout << "Bienvenue dans mon programme de tri!\n";

    // initialisation variables
    int Nelt = 200;
    int Nrange = 200;
    string aff = "O";
    string SortMode = "C";

    // Inputs User (si désactivés, variables par défaut utilisées)
    // récupération du nombre d'éléments
    cout << "Combien d'elements dans la liste ? ";
    cin >> Nelt;

    // récupération de la valeur maximale des nombres aléatoire
    cout << "Quelle valeur maximale (pour chaque element) ? ";
    cin >> Nrange;

    // demande affichage ou non
    cout << "Affichage des listes ou non ? ('O' ou 'N') ";
    cin >> aff;

    // demande croissant ou décroissant
    cout << "Tri croissant ou decroissant ? ('C' ou 'D') ";
    cin >> SortMode;
    cout << "\n";

    if (aff == "N")
    {
        cout << "Sans affichage" << "\n";
    }
    
    srand(std::time(NULL)); // setup rand()

    vector<int> listeNum; // création liste

    for (int i = 0; i < Nelt; ++i) listeNum.push_back(rand() % Nrange + 1); // remplissage (nombres aléatoires)

    if (aff == "O")
    {
        // affichage liste non triée
        cout << "liste initiale : ";
        for (vector<int>::iterator it = listeNum.begin(); it != listeNum.end(); it++)
            cout << *it << ' ';
    }

    cout << "\n";

    // Tri liste
    for (int p = 0; p < Nelt; p++) // boucle des passes à effectuer
    {
        for (int i = 0; i < Nelt - p; i++) // boucle des index de la liste
        {
            if (i <= Nelt - 2) // vérifcation si fin de liste non atteinte
            {
                if (listeNum[i] > listeNum[i + 1])
                {
                    // swap valeurs
                    int ii = listeNum[i + 1];
                    listeNum[i + 1] = listeNum[i];
                    listeNum[i] = ii;
                }
            }
        }
    }

    if (SortMode == "D") // retournement de la liste pour tri décroissant
    {
        reverse(listeNum.begin(), listeNum.end());
    }
    
    if (aff == "O")
    {
        // affichage liste triée
        cout << "liste triee : ";
        for (vector<int>::iterator it = listeNum.begin(); it != listeNum.end(); it++)
            cout << *it << ' ';
    }

    cout << "\n" << "Tri termine" << "\n"; // retour à la ligne

    /*
    // Pause à la fin du programme (pour lancement sans débogage)
    cout << "Press enter to close...";
    cin.ignore();
    */

    return 0;
}