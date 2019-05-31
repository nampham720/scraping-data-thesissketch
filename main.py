from support import *
import argparse
import sys



def Main():
    parser = argparse.ArgumentParser(description='Input your document here')
    parser.add_argument('--document', help='Type your .docx name here', type=argparse.FileType('r'))
    args = parser.parse_args()

    method = Methods(sys.argv[2])
    print("Similarity check by using:")
    print("Jaccard Similarity: %.4f\n\
Cosine Similarity:%.4f\n\
Word to vector: %.4f" % (method.jaccard_similarity(), method.cosine_sim, method.word_to_vec))

if __name__ == '__main__':
    Main()

