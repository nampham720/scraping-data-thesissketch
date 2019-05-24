# Thesis Sketch Up
This project is a backend sketch for my Bachelor thesis.   

The idea is to create a self-built plagiarism check. So far, I can only work with checking similarity between documents. 

Some deficiencies of the product is the running time and the copied text detector. Up to now, due to the amount of data, the running time has not been a big problem (less than 10 seconds). 

The idea of the project is to:
* Open the document
* Extract Hyperlinks (references)
* Store the HyperLinks in the Local Database
* Scrape data from each HyperLink
* Compare the similarity of the self-writing document with data scraped from HyperLinks
* Take the mean -> Percentage of plagiarism

**Future**:
* Improve the speed with big data
* Return copied text

### Knowledge required: 
Tfidf, cosine similarity, basic HTML, basic NLTK, mySQL query

#### Author:
Nam (Nam) Pham |
nam.pham@edu.turkuamk.fi |
Turku University of Applied Sciences


