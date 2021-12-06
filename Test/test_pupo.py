import unittest
import functional

class TestTabs(unittest.TestCase):

    def test_delete(self):
        self.assertEqual(functional.convert_bytes(1), '1.0 bytes')
        self.assertEqual(functional.convert_bytes(1024), '1.0 KB')
        self.assertEqual(functional.convert_bytes(1024*1024), '1.0 MB')
        self.assertEqual(functional.convert_bytes(1024*1024*1024), '1.0 GB')
        self.assertEqual(functional.convert_bytes(1024*1024*1024*1024), '1.0 TB')


    def test_delete(self):

        self.assertEqual(functional.delete_files('.exe'),8)
        self.assertEqual(functional.delete_files('.txt'),1)
        self.assertEqual(functional.delete_files('.json'),3)


    def test_find_first_file(self):
        files = [
            'копия.txt',
            'копия.json',
            'копия1.exe',
            'копия5.exe',
            'копия3.exe',
            'копия.exe',
            'fsdfgdf.exe',
            'копия.exe',
            'fwqew.dat',
            'копия2.txt',
            'копия.rwe',
            'копия.json',
            'копия.dat',
            'копия3.txt',
            'fdssdf.uyt'
        ]
        self.assertEqual(functional.find_first_file('.exe',files),r'копия1.exe')
        self.assertEqual(functional.find_first_file('.txt',files),r'копия.txt')
        self.assertEqual(functional.find_first_file('.json',files),r'копия.json')
        self.assertEqual(functional.find_first_file('.gdfwer',files),'')


    def test_generate_new_name(self):
        self.assertEqual(first = functional.generate_new_name(
            'D:/Repos/NewPupo',
            'test.txt',
            'geo_2021_09_02_15_49_10.141.dat'),
        second = r'NewPupo test_2021_09_02_15_49.txt')

        self.assertEqual(first = functional.generate_new_name(
            'D:/Repos/NewPupo/Якутия',
            'Out_res.txt',
            'DAT001'),
        second = r'Якутия Out_res_.txt')

        self.assertEqual(first = functional.generate_new_name(
            'D:/Repos/NewPupo/Батимитрия геленджик',
            'result.txt',
            'dat_2021_09_02_15_49_10.141.dat'),
        second = r'Батимитрия геленджик result_2021_09_02_15_49.txt')

        self.assertEqual(first = functional.generate_new_name(
            'D:/Repos/NewPupo/Батимитрия геленджик',
            'result.txt',
            ''),
        second = r'Батимитрия геленджик result_.txt')
