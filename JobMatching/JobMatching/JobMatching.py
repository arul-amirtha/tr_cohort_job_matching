#Get Job Characteristics from file and split into tokens
def jobchars(jfile):
    jobfile=open(jfile,'r')
    jobchar = jobfile.read()
    jobcharl=[]
    jobdict={}
    jobcharl=jobchar.splitlines()
    #Split lines
    for i in range(0,len(jobcharl)):
        a=jobcharl[i].split(':')
        jobdict[a[0]]=a[1]
    jdict={}
    tmpsplit=[]
    #Split tokens
    for key, value in jobdict.items():
        tmpsplit=value.split('" "')
        jdict[key]=tmpsplit
    print(jdict)
    return jdict

# Get Person Characteristics
def personchar(personfile):
    perfile=open(personfile,'r')
    perchar = perfile.read()
    percharl=[]
    ind_dict={}
    percharl=perchar.splitlines()
    #Split lines
    for i in range(0,len(percharl)):
        a=percharl[i].split(':')
        ind_dict[a[0]]=a[1]
    indvdict={}
    tmpsplit=[]
    for key, value in ind_dict.items():
        tmpsplit=value.split(',')
        indvdict[key]=tmpsplit
    newdict={}
    #Split tokens based on space
    for key, value in indvdict.items():
        tmpsplit1=[]
        for i in range(0,len(value)):
            tmpsplit1+=value[i].split(' ')
        newdict[key]=tmpsplit1
    print(newdict)
    return newdict

#Define Match job
def matchjob():
    jdict=jobchars("jobfile.txt")
    indvdict=personchar("individuals.txt")
    ind_score={}
    #Base score on individuals
    for ind, indchar in indvdict.items():
        indscore=0
        for key, value in jdict.items():
            #normalise score of individuals based on number of chars
            charscore=100/len(value)
            for i in range(0,len(indchar)):
                #Compare tokens and score candidate
                if indchar[i].strip(',') in value:
                    indscore+=1*charscore
            ind_score[ind]=[key,indscore]
    print(ind_score)





matchjob()


