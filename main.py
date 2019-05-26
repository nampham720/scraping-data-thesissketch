from support import *
import argparse
import sys



def Main():
    parser = argparse.ArgumentParser(description='Input your document here')
    parser.add_argument('--document', help='Type your .docx name here', type=argparse.FileType('r'))
    args = parser.parse_args()

    check = Similarity(str(sys.argv[2]))
    print("The similarity of your text compared to your refs is: " ,check.checking_similarity())

if __name__ == '__main__':
    Main()

