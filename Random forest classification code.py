#lets do something on the random forest classifier

#1.cleaning data
def make_sth_cool(root_dir):
     all_stuff=[]
     emails=[os.path.join(root_dir,f) fot f in os.listdir(root_dir)]

     for mail in mails:
          with open(mail) as m:
                for line in m:
                         words=line.split()
                        all_stuff+=words
      dictionary = counter(all_stuff)

stuff_to_clean=dictionary.keys()
for item in  list_to_remove:
     #remove numerical
     if item.isalpha()==False:
         del dictionary[item]
     elif len(item)==1:
          del dictionary[item]
#lets take into consideration only the most 400 common words in dictionary
dictionary=dictionary.most_common(4000)

def get_the_features(mail_dir):
    files=[os.path.join(mail_dir,g)for g in os.listdir(mail_dir)]
    features=np.zeros(len(files)),3000))
    train=np.zeros(len(files))
    count=0;
    id=0;
    for sg in files:
          with open(sg)as  s:
               for i in,line in enumerate(g):
                    if i==2:
                         words=line.split()
                              for word in words:
                                   wid=0
                                        for i,d in enumerate(dictionary):
                                             if d[0]==word:
                                                  id=i
features[id,wid] = words.count(word)
train[id]=0;
fileptokens=fil.split('/')
lastoken=fileptoken[len(fileptokens)-1]
     if lastoken.startswith("spmsg"):
          train[id]=1;
          count=count+1
     id = id+1
return features,train


#2.lets use regression random forest classifier import lib;create model;train;predict

from sklearn.ensemble import RandomForestClassifier

train_data=(type the path to the train data)
test_data=(type in the data to the test data)
dictionary=make_Dictionary(train_data) print "reading and proccessing data from file"

features,labels=extract_features(train_data)
test_feature,test_label=extract_features(test_data)

#3.model
model=RandomForestClassifier()

print "training model"
model.fit(feature,labels)

predicted=model.predict(test_feature)
print"finished"
print accuracy(test_data,predict)



#its that simple. remember am using python 2.7 for python 3 you will need some little twists of the code.
