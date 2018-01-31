import unittest
import file_namer
import unittest.mock as mock

class FindLastFilenameTest(unittest.TestCase):
    @mock.patch.object(file_namer.glob, 'glob')
    @mock.patch.object(file_namer.os.path, 'exists')
    def testfilenumber0(self, mock_exists, mock_glob):
        # The second file - filename already exists
        mock_exists.return_value = True
        mock_glob.return_value = ['testfolder/test/testfile.csv']
        filename = 'testfolder/test/testfile.csv'
        new_filename = file_namer.name_file(filename)
        self.assertEqual('testfolder/test/testfile-1.csv', new_filename)

    @mock.patch.object(file_namer.glob, 'glob')
    @mock.patch.object(file_namer.os.path, 'exists')
    def testnofolder(self, mock_exists, mock_glob):
        # File name has no folders in it
        mock_exists.return_value = True
        mock_glob.return_value = []
        filename = 'testfile.csv'
        new_filename = file_namer.name_file(filename)
        self.assertEqual('testfile-1.csv', new_filename)

    @mock.patch.object(file_namer.glob, 'glob')
    @mock.patch.object(file_namer.os.path, 'exists')
    def testdifffile(self, mock_exists, mock_glob):
        # First file - filename does not yet exist
        mock_exists.return_value = False
        mock_glob.return_value = []
        filename = 'testfolder/test/differentname.csv'
        new_filename = file_namer.name_file(filename)
        self.assertEqual('testfolder/test/differentname.csv', new_filename)

    @mock.patch.object(file_namer.glob, 'glob')
    @mock.patch.object(file_namer.os.path, 'exists')
    def testfilenumber1(self, mock_exists, mock_glob):
        # A filename ending with the digit 1
        mock_exists.return_value = True
        mock_glob.return_value = ['testfolder/test/testfile1.csv']
        filename = 'testfolder/test/testfile1.csv'
        new_filename = file_namer.name_file(filename)
        self.assertEqual('testfolder/test/testfile1-1.csv', new_filename)

    @mock.patch.object(file_namer.glob, 'glob')
    @mock.patch.object(file_namer.os.path, 'exists')
    def testfileorder1(self, mock_exists, mock_glob):
        # Third filename
        mock_exists.return_value = True
        mock_glob.return_value=[
            'testfolder/test/testfile.csv', 'testfolder/test/testfile-1.csv']
        filename = 'testfolder/test/testfile.csv'
        new_filename = file_namer.name_file(filename)
        self.assertEqual('testfolder/test/testfile-2.csv', new_filename)

    @mock.patch.object(file_namer.glob, 'glob')
    @mock.patch.object(file_namer.os.path, 'exists')
    def testfileorder2(self, mock_exists, mock_glob):
        # Order of files in the folder is not sequential
        mock_exists.return_value = True
        mock_glob.return_value=[
            'testfolder/test/testfile-1.csv', 'testfolder/test/testfile.csv']
        filename = 'testfolder/test/testfile.csv'
        new_filename = file_namer.name_file(filename)
        self.assertEqual('testfolder/test/testfile-2.csv', new_filename)

class NumberFileNamesTest(unittest.TestCase):
    def testfilenumber1(self):
        # Test numbering of first string
        filename = 'stuff.csv'
        new_filename = file_namer.number_file_names(filename)
        self.assertEqual('stuff-1.csv', new_filename)

    def testfilenumber2(self):
        # Test sequential numbering
        filename = 'stuff-1.csv'
        new_filename = file_namer.number_file_names(filename)
        self.assertEqual('stuff-2.csv', new_filename)

    def testfilenumber10(self):
        # Test sequential numbering with two digits
        filename = 'stuff-10.csv'
        new_filename = file_namer.number_file_names(filename)
        self.assertEqual('stuff-11.csv', new_filename)

    def testfiledot(self):
        filename = 'test1.0.csv'
        new_filename = file_namer.number_file_names(filename)
        self.assertEqual('test1.0-1.csv', new_filename)

    def testfolderdash1(self):
        filename = '/home/home/t-5/pvt/stuff.csv'
        new_filename = file_namer.number_file_names(filename)
        self.assertEqual('/home/home/t-5/pvt/stuff-1.csv', new_filename)

    def testfolderdash2(self):
        filename = '/home/home/t-5/pvt/stuff-1.csv'
        new_filename = file_namer.number_file_names(filename)
        self.assertEqual('/home/home/t-5/pvt/stuff-2.csv', new_filename)

    def testfolderdash10(self):
        filename = '/home/home/t-5/pvt/stuff-10.csv'
        new_filename = file_namer.number_file_names(filename)
        self.assertEqual('/home/home/t-5/pvt/stuff-11.csv', new_filename)

    def testfolderdot1(self):
        filename = '/home/home/t5/.pvt/stuff.csv'
        new_filename = file_namer.number_file_names(filename)
        self.assertEqual('/home/home/t5/.pvt/stuff-1.csv', new_filename)

    def testfolderdot2(self):
        filename = '/home/home/t5/.pvt/stuff-1.csv'
        new_filename = file_namer.number_file_names(filename)
        self.assertEqual('/home/home/t5/.pvt/stuff-2.csv', new_filename)

    def testfolderdot10(self):
        filename = '/home/home/t5/.pvt/stuff-10.csv'
        new_filename = file_namer.number_file_names(filename)
        self.assertEqual('/home/home/t5/.pvt/stuff-11.csv', new_filename)


if __name__ == '__main__':
    unittest.main()
