#include <iostream>
#include <random>
#include <ctime>
#include <algorithm>
#include <stdio.h>
#include <stack>

using namespace std;

// Renvoie une part de liste : [start;stop[
vector<int> Slicer(vector<int> v, int start, int stop){ 
    vector<int> slice;

    for (int i = start; i < stop; i++)
    {
        slice.push_back(v[i]);
    }
    
    return slice;
}

// Trie la liste L
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
        vector<int> sl; // liste triée
        int mid = len/2;

        vector<int> A = Slicer(l,0,mid);
        vector<int> B = Slicer(l,mid,len);

        A = TriFusion(A);
        B = TriFusion(B);

        while (sl.size()<len)
        {
            while (!A.empty() || !B.empty())
            {
                vector<int>::iterator it;
                if (A.empty())
                {
                    sl.push_back(B[0]);
                    it = B.begin();
                    B.erase(it);
                }
                else if (B.empty())
                {
                    sl.push_back(A[0]);
                    it = A.begin();
                    A.erase(it);
                }
                else if (A[0]<=B[0])
                {
                    sl.push_back(A[0]);
                    it = A.begin();
                    A.erase(it);
                }
                else if (B[0]<=A[0])
                {
                    sl.push_back(B[0]);
                    it = B.begin();
                    B.erase(it);
                }          
            }       
        }

        return sl;     
    }
}

int main(){
    printf("Bienvenue dans mon programme de tri!\n");

    // initialisation variables
    int Nelt = 200;
    int Nrange = 200;
    string aff = "O";
    string SortMode = "C";

    // Inputs User (si désactivés, variables par défaut utilisées)
    // récupération du nombre d'éléments
    printf("Combien d'elements dans la liste ? ");
    cin >> Nelt;

    // récupération de la valeur maximale des nombres aléatoire
    printf("Quelle valeur maximale (pour chaque element) ? ");
    cin >> Nrange;

    // demande affichage ou non
    printf("Affichage des listes ou non ? ('O' ou 'N') ");
    cin >> aff;

    // demande croissant ou décroissant
    printf("Tri croissant ou decroissant ? ('C' ou 'D') ");
    cin >> SortMode;
    printf("\n");

    if (aff == "N")
    {
        printf("Sans affichage\n");
    }
    
    srand(std::time(NULL)); // setup rand()

    vector<int> listeNum; // création liste

    for (int i = 0; i < Nelt; ++i) listeNum.push_back(rand() % Nrange + 1); // remplissage (nombres aléatoires)

    if (aff == "O")
    {
        // affichage liste non triée
        printf("liste initiale : \n");
        for (vector<int>::iterator it = listeNum.begin(); it != listeNum.end(); it++)
            cout << *it << ' ';
    }

    vector<int> listetriee = TriFusion(listeNum);
    
    if (aff == "O")
    {
        printf("\nliste tiree : \n");
        for (vector<int>::iterator it = listetriee.begin(); it != listetriee.end(); it++)
            cout << *it << ' ';
    }
    //cout << "\nTaille liste triee : " << listetriee.size();
    printf("\nTri termine\n");
    
    return 1;
}