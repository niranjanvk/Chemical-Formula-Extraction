# Chemical-Formula-Extraction(Python)
From a chemistry related documents all Chemical Formulae and Chemical Equations present in documents can be Extracted by using this project. This whole project is devided into two parts
1. Chemical Formula Extraction
2. Chemical Equation Extraction

#1. Chemical Formula Extraction- User takes .PDF file as input and output would be all chemical formulae present in PDF file.
    From Developers Perspective we can consider following things
    Libraries Used-
    1. PyPDF2- For Reading PDF file(or Extraction of text from .PDF File)
    2. NLTK- We are using this library to eliminate regular English words.
    3. PubChemPy- For finding final result by comparing result with chemical formula already present in this library.
 As .PDF File is given as input first it is converted into text and all words are compared with regular english words(stored in list by using NLTK library) then resultant words are compared with chemical formulae name(stored using PubChemPy) and final result is printed on output screen.
 
#2. Chemical Equation Extraction- User take .DOCX file as input and output would be all chemical equations(or '->' is present).
    From Developers Perspectives we can consider following things
    Libraries Used-
    1. docx2txt- For converting .DOCX file into .TXT file(or for extracting text)
    
 Apart from this an User Frienldy GUI is there made by using HTML.
 GUI is connected to Python code using MICRO WEB FRAMEWORK "Flask". In 'Flask' GET and POST Methods are being used to take input and displaying result through GUI.
 
 
 
 Thanks to My Team-
 Yugansh Arora,
 Harsh Bhadoria,
 V. Uma Mahesh,
 M. Venkatesh
