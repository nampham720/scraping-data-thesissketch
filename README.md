# Scraping Data (Thesis Sketchup) 
This project is a back-end sketch for my Bachelor thesis. 

*There is also my unfinished personal document (as a test with 09 refs so far) for the Organisational Psychology Course. Please find the essay as reference **only** (because it has not been graded yet). Thank you.* 

The idea is to create a self-built plagiarism check. Up to now, I can only work with checking similarity between documents. 

One of the deficiencies of the product is the copied text detector. Additionally, running time should also be taken into consideration. However, due to the amount of data, the running time has not been a big problem (less than 10 seconds). 

The agenda of the project is to:
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
Turku University of Applied Sciences, Finland


