"""
TEST_RANDOM_TESTS: test dello script :mod:`random_tests.random_tests`.py

Unittest esegue i metodi di :class:`TestRandomTests()`:

* :meth:`test_production_mode() <TestRandomTests.test_production_mode>`: verifica se lo script e' pronto alla produzione
* :meth:`test_check_unique() <TestRandomTests.test_check_unique>`: test della funzione check_unique()
* :meth:`test_gen_rnd_list() <TestRandomTests.test_gen_rnd_list>`: test della funzione gen_rnd_list()
"""

__author__ = "Zenaro Stefano"
__version__ = "2020-04-03 01_01"

import unittest
import os
import sys
# inserisci in path la cartella superiore
# per importare random_tests
sys.path.insert(0, os.path.abspath('..'))

from random_tests import random_tests as rt

# casi in cui i test dovrebbero essere positivi
unique_true_test_cases = [
    # casi particolari
    [0],
    [0.0],
    [1],
    [1.0],
    [-1],
    ["0"],
    ["0.0"],
    ["1"],
    ["1.0"],
    ["-1"],
    ["-1.0"],
    [False],
    [True],
    [(), 0],
    # "stesso numero", uno stringa e uno intero
    ["1", 1],
    # caso tutti interi positivi
    [1, 2, 3],
    # caso negativi interi e positivi
    [-1, 1, -3, 2, 3],
    # caso tutte stringhe
    ["1", "2", "3", "-1"],
    # caso misto
    ["1", 2, 3, "4", "-1"],
    # caratteri speciali e non ASCII
    ["£$=)£(%/=)/!òàùèp+àò?", "è+èàù+è&)(&\"£=)àò", 3],
    # valori assoluti grandi
    [-9999999999999999999999999999, 9999999999999999999999999999]
]

# casi in cui i test dovrebbero essere negativi
unique_false_test_cases = [
    # casi particolari
    [0, 0],
    [0.0, 0.0],
    [1, 1],
    [True, 1],
    [True, 1.0],
    [False, 0],
    [False, 0.0],
    [[], []],
    [[True], [True]],
    ["0", "0"],
    ["0.0", "0.0"],
    ["1.0", "1.0"],
    ["-1", "-1"],
    ["-1.0", "-1.0"],
    # valori assoluti grandi
    [-9999999999999999999999999999, -9999999999999999999999999999],
    [9999999999999999999999999999, 9999999999999999999999999999],
    ["è+èàù+è&)(&\"£=)àò", "è+èàù+è&)(&\"£=)àò"]
]

# casi per test remove_blanks
remove_blanks_test_cases = [
    {"argument": [], "expected_result": []},
    {"argument": [""], "expected_result": []},
    {"argument": [" "], "expected_result": []},
    {"argument": [" "], "expected_result": []},
    {"argument": [" a ", " b", "", " ", "c"], "expected_result": ["a", "b", "c"]}
]


class TestRandomTests(unittest.TestCase):

    def test_production_mode(self):
        """
        Assicura la modalita' di produzione.

        Il test fallisce se:
		
        * ``boold = True`` (messaggi debug attivi),
        * ``fromfile = True`` (di default il programma usa la lista ``studenti``),
        * ``file_studenti != "example.txt"`` (default modificato)
        * ``studenti != []`` (di default la lista e' vuota)
        * ``volontari != []`` (di default la lista e' vuota)
        """
        # si assicura che i messaggi di debug siano disattivati
        self.assertFalse(rt.boold)

        # si assicura che gli studenti vengano presi dalla lista (non da file)
        self.assertFalse(rt.fromfile)

        # si assicura che file_studenti sia "example.txt"
        self.assertEqual(rt.file_studenti, "example.txt")

        # si assicura che studenti sia []
        self.assertEqual(rt.studenti, [])

        # si assicura che volontari sia []
        self.assertEqual(rt.volontari, [])

    def test_check_unique(self):
        """
        Test funzione :func:`random_tests.random_tests.check_unique()`: controlla unicita' elementi in una lista.

        Il test fallisce se uno dei casi in unique_true_test_cases e
        unique_false_test_casese da un risultato inaspettato.
        """

        # testa tutti i casi "positivi"
        for test_case in unique_true_test_cases:
            self.assertTrue(rt.check_unique(test_case))

        # testa tutti i casi "negativi"
        for test_case in unique_false_test_cases:
            self.assertFalse(rt.check_unique(test_case))

    def test_gen_rnd_list(self):
        """
        Test funzione :func:`random_tests.random_tests.gen_rnd_list()`: genera lista casuale da un'altra lista.

        gen_rnd_list(t_vstudenti, t_volontari=[]):
		
        * t_vstudenti: lista con elementi da restituire in ordine casuale
        * t_volontari: lista elementi da posizionare primi nell'output.

        Il test non ha successo se:
		
        * la funzione NON da errore se gli studenti sono duplicati
        * la funzione NON da errore se i volontari sono duplicati
        * la funzione restituisce piu' del 50% delle volte risultati uguali di fila
        """

        # caso con t_vstudenti duplicati: NonUniqueStudentsError("Il vettore degli studenti ha duplicati")
        for test_case in unique_false_test_cases:
            # accetta NonUniqueStudentsError
            with self.assertRaises(rt.NonUniqueStudentsError):
                rt.gen_rnd_list(test_case)

        # caso con t_volontari duplicati: NonUniqueVolunteersError("Il vettore dei volontari ha duplicati")
        for test_case in unique_false_test_cases:
            # accetta NonUniqueVolunteersError
            with self.assertRaises(rt.NonUniqueVolunteersError):
                rt.gen_rnd_list([1, 2], test_case)

        # prova a generare liste random: conta risultati uguali di fila
        old_rnd_res = []  # per memorizzare generazioni
        equal_res = 0     # quante volte 2 risultati uguali sono capitati di file
        n_tries = 11      # numero di generazioni
        
        for _ in range(n_tries):
            # genero lista random
            rnd_res = rt.gen_rnd_list(["Giorgio", "Pinco", "Pallo", "Giovanni", "Elisa", "Mario"])
            
            # se la lista generata precedentemente e' uguale a quella appena generata
            if old_rnd_res == rnd_res:
                equal_res += 1  # tieni conto dell'evento

            # memorizza l'ultima generazione
            old_rnd_res = rnd_res

        # crea la percentuale di eventi
        percentage = (equal_res / n_tries) * 100

        # errore se la percentuale e' maggiore del 50%
        assert(percentage < 50)

    def test_remove_blanks(self):
        """
        Test funzione :func:`random_tests.random_tests.remove_blanks()`: restituisce vettore passato senza stringhe vuote/nulle.
        """
        # prova tutti i casi di test
        for test_case in remove_blanks_test_cases:
            # verifica che l'argomento del caso passato a remove_blanks() restituisca il risultato sperato
            self.assertEqual(rt.remove_blanks(test_case["argument"]), test_case["expected_result"])


if __name__ == '__main__':
    # inizia i test
    unittest.main()
