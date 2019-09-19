import combiner
import io
import unittest.mock

class TestOldPython(unittest.TestCase):

    def test_get_file_name(self):
        file1 = combiner.Combiner('./hello.csv')
        file2 = combiner.Combiner('')
        self.assertIsInstance(file2.get_file_name(),str)
        self.assertEqual(file2.get_file_name(),'csv-combiner')
        self.assertEqual(file1.get_file_name(), 'hello.csv')
        self.assertIsInstance(file1.get_file_name(), str)

    def test_print_to_stdout(self):
        self.assertEqual(combiner.Combiner.first_file_opened, True)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_to_stdout1(self,mock_stdout):
        combiner.Combiner('./testSamples/testclothing1.csv').print_to_stdout()
        self.assertEqual('Error! The file "testclothing1.csv" could not be opened for reading, -, - \n', mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_to_stdout2(self, mock_stdout):
        combiner.Combiner('./testSamples/testclothing.csv').print_to_stdout()
        self.assertEqual('"email_hash","category","filename"\r\n"21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63","Shirts","testclothing.csv"\r\n"21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63","Pants","testclothing.csv"\r\n', mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_to_stdout3(self,mock_stdout):
        combiner.Combiner('./testSamples/testcombined.csv').print_to_stdout()
        self.assertEqual('"21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63","Shirts","testcombined.csv"\r\n"21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63","Pants","testcombined.csv"\r\n"166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b","Cardigans","testcombined.csv"\r\n"176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab","Wallets","testcombined.csv"\r\n"63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe","Purses","testcombined.csv"\r\n', mock_stdout.getvalue())
        self.assertEqual(combiner.Combiner.first_file_opened, False)

if __name__ == '__main__':
    unittest.main()