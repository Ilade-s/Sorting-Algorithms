#include <iostream>
#include <random>
#include <ctime>
#include <algorithm>

using namespace std;

vector<int> fusion(vector<int> A,vector<int> B){
    vector<int> fe;
    vector<int> a;
    vector<int> b;
    vector<int> resultat(B.size() + A.size());

    if (A.size() == 0){
        return B;
    }
    else if (B.size() == 0){
        return A;
    }

    else if (A[0]<=B[0]){
        fe.push_back(A[0]);

        for (int i = 1; i < A.size(); i++)
            a.push_back(A[i]);

        vector<int> f = fusion(a,B);

        merge(fe.begin(), fe.end(), f.begin(), f.end(), resultat.begin());

        return (resultat);
    }

    else{
        fe.push_back(B[0]);

        for (int i = 1; i < B.size(); i++)
            b.push_back(B[i]);
 
        vector<int> f = fusion(A,b);

        merge(fe.begin(), fe.end(), f.begin(), f.end(), resultat.begin());

        return (resultat);
    }
    
}

vector<int> TriFusion(vector<int> l){

    vector<int> a; // première moitié de la liste
    vector<int> b; // seconde moitié de la liste

    int len = l.size();

    if (len <= 1)
    {
        return l;
    }

    else
    {
        int divn = len/2;

        // Remplissage list slices
        for (int i = 0; i < divn; i++)
            a.push_back(l[i]);
        for (int i = divn; i < len; i++)
            b.push_back(l[i]);
        /*   
        cout << "a : ";
        for (vector<int>::iterator it = a.begin(); it != a.end(); it++)
            cout << *it << ' ';
        cout << "\nb : ";
        for (vector<int>::iterator it = b.begin(); it != b.end(); it++)
            cout << *it << ' ';
        cout << "\n";
        */
        return fusion(TriFusion(a),TriFusion(b));
    }
    
}

int main(){
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

    vector<int> listetriee = TriFusion(listeNum);
    
    if (aff == "O")
    {
        cout << "liste tiree : ";
        for (vector<int>::iterator it = listetriee.begin(); it != listetriee.end(); it++)
            cout << *it << ' ';
    }

    cout << "\ntri termine\n";
    
    return 1;
}