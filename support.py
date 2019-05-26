from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
import numpy as np
import PyPDF2
import urllib
import pymysql
from bs4 import BeautifulSoup
import requests, io, re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer



class Similarity:
    def __init__(self, document):
        self.document = document

    def checking_similarity(self):
        '''
        Checking similarity using cosine similarity
        Library used:
        sklearn.feature_extraction.text -> TfidfVectorizer
        '''
        
        def readFile(doc):
            '''
            Read a text file and return to elements of a list
            '''
            full_text = []
            for p in doc.paragraphs:
                full_text.append(p.text)

            return '\n'.join(full_text)

        def onl_refs(rels):
            '''
            Extract all the hyperlinks (refs) in the document
            '''
            links = []
            for rel in rels:
                if rels[rel].reltype == RT.HYPERLINK:
                    links.append(rels[rel]._target)
                
            return links

        def working_with_mysql(onl_ref_results):
            '''
            Store all the hyperlinks to db
            library used: pymysql
            '''
            #open db
            db = pymysql.connect(host='127.0.0.1',
                                user='root',
                                db='references')

            #create cursor
            cursor = db.cursor()

            #insert/check distinct refs to add to the db
            sql = "INSERT INTO onlref (link) VALUES (%s)"
            for link in onl_ref_results:
                try:
                    cursor.execute(sql, link)
                except:
                    pass

            #pull all the links
            cursor.execute('SELECT link FROM onlref')
            data = cursor.fetchall()

            #commit and close db
            db.commit()
            db.close()

            #add link into a list
            links = []
            for link in data:
                links.append(link[0])
            return links

        def read_content(link):
            '''
            Depend on the website (pdf or regular html)
            Open the link and scrape the data of 01 site
            Libraries used:
            bs4 -> BeautifulSoup
            request, io, re
            '''
            string = []
            #if the link is a pdf
            if (re.search(link.split('/')[-1], r'.pdf') is True):
                response = requests.get(link)
                raw_data = response.content
                pdf_content = io.BytesIO(raw_data)
                pdf_reader = PyPDF2.PdfFileReader(pdf_content)
                for page in range(pdf_reader.numPages + 1):
                    string.append(pdf_reader.getPage(page).extractText())

                return (' '.join(string))
            else:
                #function to scrape data
                def scrape_data():
                    page = requests.get(link)
                    text = BeautifulSoup(page.text, 'html.parser').find_all('p')
                    for p in text:
                        string.append(p.get_text())
                    return(' '.join(string).replace(u'\xa0', ' ').replace(u'\n', ' '))
                
                #start scraping
                try:
                    return scrape_data()
                
                #some links need authentication
                except:
                    
                    headers = {'User-Agent':'Mozilla/5.0'}             
                    #class AppURLopener(urllib.request.FancyURLopener):
                        #version = "Mozilla/5.0"
                    #opener = AppURLopener()
                    return scrape_data()

        def get_all_content(links):
            '''
            Return all the contents into a list 
            '''
            base_refs = []
            for link in links:
                base_refs.append(read_content(link))
            return base_refs

        def get_token(text):
            '''
            Tokenize + Omit punctuation
            Libraries:
                nltk.tokenize -> word_tokenize
                nltk.corpus -> stopwords,
                string
            '''
            translator = str.maketrans('', '', string.punctuation)
            stop_words = set(stopwords.words('english'))
            tokens = word_tokenize(text)
            tokens = [token.lower() for token in tokens]
            filtered = [w for w in tokens if not w in stop_words]
            return ' '.join(filtered).translate(translator)

        doc = Document(self.document)
        rels = doc.part.rels
        vect = TfidfVectorizer(min_df=1)
        similarity = []
        links = working_with_mysql(onl_refs(rels))

        for content in get_all_content(links):
            tfidf = vect.fit_transform([get_token(readFile(doc)), content])
            similarity.append((tfidf * tfidf.T).A[0,1])
        
        return np.mean(similarity)

    
        