==========
SVD-Python
==========


Projekt na zajęcia "Język Python w uczeniu maszynowym" - algorytm SVD


Opis
====

Projekt będzie polegał na implementacji algorytmu SVD (Singular Value Decomposition) czyli Rozkładu macierzy według wartości osobliwych.

Grupa
=====

+ Martyna Mazurkiewicz

+ Mateusz Lepa

+ Kamil Zawilski

Algorytm krok po kroku
======================

1.  Transponować macierz A.

2.  Obliczyć macierze ATA i AAT (obie powinny być kwadratowe).

3.  Obliczyć rząd dla obu macierzy i odrzucić tę z większym rzędem. 
    Przyjmujemy macierz z mniejszym rzędem, która od tej pory przyjmuje nazwę Aw (właściwa).

4.	Dla macierzy Aw obliczyć wartości własne macierzy:
      
    + Obliczyć macierz Aλ=Aw – λI, gdzie λ to niewiadoma, a I to macierz jednostkowa
      
    + Wyznaczyć równanie charakterystyczne macierzy (policzyć wyznacznik). 
        Obliczyć pierwiastki przyrównując równanie do zera.
      
    + Wyliczone pierwiastki to te wartości własne (mogą wyjść w liczbach zespolonych).

5.  Określić r, czyli liczbę niezerowych wartości własnych macierzy Aw.
  
6.  Znaleźć ortonormalne wartości własne macierzy Aw odpowiadające znalezionym wartościom własnym.
    Stworzyć macierz ortogonalną(unitarną – przy liczbach zespolonych) V € Rnxn,
    której kolejne kolumny tworzą ortonormalne wartości własne macierzy Aw
    odpowiadające jej wartościom własnym i uporządkowane w porządku malejącym.
      
7.  Stworzyć macierz ∑ € Rmxn i umieścić na diagonalnej pierwiastki kwadratowe  z wartości własnych macierzy Aw. 
  
8.	Znaleźć r pierwszych wektorów kolumnowych macierzy U € Rmxm z równań  , gdzie j = 1,2…r.
  
9.	Dodać do macierzy U pozostałe m-r wektorów wykorzystując proces ortogonalizacji Grama-Schmidta


