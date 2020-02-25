import PyPDF2
import textract
import nltk
import pubchempy as pc
def convert(input):
        words = set(nltk.corpus.words.words())
        f= open(input,'rb')
        fr= PyPDF2.PdfFileReader(f)
        #pageObj=fr.getPage(1)
        text=""
        num_pages = fr.numPages
        count = 0
        text = ""
        #The while loop will read each page
        while count < num_pages:
                pageObj = fr.getPage(count)
                count +=1
                text += pageObj.extractText()
                if text != "":
                    text = text
        #            newString = (text.encode('ascii', 'ignore')).decode("utf-8")
                else:
                    text = textract.process(input, method='tesseract', language='eng')
        #            newString = (text.encode('ascii', 'ignore')).decode("utf-8")
        s=" ".join(w for w in nltk.wordpunct_tokenize(text) \
        
                 if (w.lower() not in words and w.upper() not in words))
        #print(s)
        #print(text)
        l=list(filter(lambda x:x[0].isupper(),s.split()))
        #print(l)
        l=list(dict.fromkeys(l))
        
        freq={}
        for i in range(10):
              try:    
                    results = pc.get_cids(l[i], 'name')
                    c=pc.Compound.from_cid(results)
                    ''' if(i in freq):
                        freq[l[i]][1]+=1
                    else:
                        freq[l[i]]=[c.synonyms[0],1]'''
                    freq[l[i]]=c.synonyms[0]
                    #print(l[i]+" NAME:- "+c.synonyms[0])
                    
              except:
                    pass
             
        #print(l)
        f.close()
        return freq
