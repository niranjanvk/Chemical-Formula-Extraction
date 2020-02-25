import docx2txt

def eq(input):
        l=[]
        text = docx2txt.process(input)
        
        for i in text.splitlines():
            for j in i:
                if(j=='→' and not i.startswith('→') ):
                    l.append(i)
                    
        return l
                

eq(input)
