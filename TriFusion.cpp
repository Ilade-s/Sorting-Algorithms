#include <iostream>
#include <random>
#include <ctime>
#include <algorithm>
#include <stdio.h>

using namespace std;

vector<int> Slicer(vector<int> v, int start, int stop){ // Renvoie une part de liste : [start;stop[
    vector<int> slice;

    for (int i = start; i < stop; i++)
    {
        slice.push_back(v[i]);
    }
    
    return slice;
}

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

    else if (len > 2000) // fix Stack Overflow
    {
        vector<vector<int>> lt;

        for (int p = 0; p < len/1000; p++) // parts complètes (de 2000) [i+1000:1000*(p+1)]
        {
            int i = p*1000;
            lt.push_back(fusion(TriFusion(Slicer(l,i,i+1000)),TriFusion(Slicer(l,i+1000,1000*(p+1)))));
        }
        if (len%2000!=0) // part incomplète (si existante)
        {
            int j = (len/1000)*1000;
            int fl = len-j;
            int mid = j+fl/2;
            lt.push_back(fusion(TriFusion(Slicer(l,j,mid)),TriFusion(Slicer(l,mid,len))));
        }
        while (lt.size()>1) // tri des parts (en arbre)
        {
            vector<vector<int>> tmp;

            for (int i = 0; i < lt.size()-1; i++)
            {
                tmp.push_back(fusion(lt[i],lt[i+1]));
            }
            lt = tmp;
        }

        return lt[0];
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

    printf("\nTri termine\n");
    
    return 1;
}