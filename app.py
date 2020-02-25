from flask import Flask,render_template,url_for,request,send_file,redirect,session
import docx2txt

import PyPDF2
import textract
import nltk
import pubchempy as pc



import reader2

nltk.download('words')
app = Flask(__name__)

@app.route("/")
def index():

    return render_template('index.html')


@app.route("/form1",methods=['GET','POST'])
def form1():
	if request.method == 'POST':
		rawtext = request.files['rawtext']
		l=[]
		text = docx2txt.process(rawtext)
		for i in text.splitlines():
			for j in i:
				if(j=='→' and not i.startswith('→') ):
					l.append(i)

	return render_template('index.html',final_summary1=l)


@app.route("/form2",methods=['GET','POST'])
def form2():
	if request.method == 'POST':
		rawtext = request.files['rawtext']
		words = set(nltk.corpus.words.words())
		fr= PyPDF2.PdfFileReader(rawtext)
		text=""
		num_pages = fr.numPages
		count = 0
		text = ""
		while count < num_pages:
			pageObj = fr.getPage(count)
			count +=1
			text += pageObj.extractText()
			if text != "":
				text = text
			else:
				text = textract.process(input, method='tesseract', language='eng')
		s=" ".join(w for w in nltk.wordpunct_tokenize(text) \
		if (w.lower() not in words and w.upper() not in words))
		l=list(filter(lambda x:x[0].isupper(),s.split()))
		l=list(dict.fromkeys(l))
		freq=[]
		for i in range(10):
			try:    
				results = pc.get_cids(l[i], 'name')
				c=pc.Compound.from_cid(results)
				freq.append((l[i],c.synonyms[0]))    
			except:
				pass
		

	return render_template('index.html',final_summary=freq)





app.run(debug=True)