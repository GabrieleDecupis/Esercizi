from esercitazioni_classi_funzioni_M import MyStack
import unittest

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.mystack = MyStack()
    
    
    def test_push(self):
        with open("file_controllo_Mystack.txt", "r") as f:
            lista_controllo = []
            for x in f.readlines():
                lista_controllo.append(int(x.strip()))

        for x in lista_controllo:
            self.mystack.push(x)
            self.assertEqual(self.mystack.top(), x, "Sbagliato")
    
    def test_pop(self):
        with open("file_controllo_Mystack.txt", "r") as f:
            lista_controllo = []
            for x in f.readlines():
                lista_controllo.append(int(x.strip()))

        for x in lista_controllo:
            self.mystack.push(x)
            y = self.mystack.top()
            self.assertEqual(self.mystack.pop(), y, "Sbagliato")


if '__main__' == __name__:
    unittest.main()

    

    
    