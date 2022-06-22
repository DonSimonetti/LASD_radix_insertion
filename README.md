# Confronto RadixSort-InsertionSort
L'obiettivo di questo test è di comparare le prestazione dei due algoritmi in vari scenari.\
Vengono effettuati test su array di varie grandezze, randomizzati o parzialmente ordinati.\
Lo script `run_test.sh` esegue `test_random_numbers.py` e `test_almost_sorted_arrays.py` e ne misura il tempo di esecuzione.\
I due eseguibili python generano array di lunghezza crescente e vi eseguono InsertionSort e RadixSort.\
In `test_almost_sorted_arrays.py` gli array generati subiscono un ulteriore step di ordinamento parziale per simulare lo scenario di sequenze di numeri già quasi ordinate.
