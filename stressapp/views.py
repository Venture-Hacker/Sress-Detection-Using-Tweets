import email
from unicodedata import name
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import logout
from nltk.corpus import stopwords
from nltk.stem import *
import tweepy
import nltk
nltk.download('stopwords')
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pickle
import re
from keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import *
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.mail import send_mail
from django.contrib.auth.models import Group
# Create your views here.
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

p=PorterStemmer()
stwrds=stopwords.words("english")
def filtr(st):
    arr=[re.sub("[http,@,#].*","",x) for x in st.split() if x not in stwrds]
    arr=[p.stem(x) for x in arr]
    return ' '.join(arr)

# Create your views here.
def index(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        feedback(name=name,email=email,subject=subject,message=message).save()
    return render(request,'index.html')
    



def register(request):
    form = registeruserform()
    form1 = registerform()
    mydict = {'form': form, 'form1': form1}
    if request.method == "POST":
        form = registeruserform(request.POST)
        form1 = registerform(request.POST) 
        if form.is_valid() and form1.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,'Registered Successfully')
            registration=form1.save(commit=True)
            registration.user=user
            registration.save()
            group=Group.objects.get_or_create(name="STRESS")
            group[0].user_set.add(user)
            return redirect('login')
        else:
            mydict['form'] = form
            mydict['form1'] = form1
            messages.error(request, 'Please correct the errors below.')
    return render(request, 'register.html', mydict)


def is_registration(user):
    return user.groups.filter(name="STRESS").exists()
    


def login(request):
    return render(request,'login.html')

@login_required
def afterlogin_view(request):
    if is_registration(request.user):
        return redirect('home')

@login_required(login_url='login')
@user_passes_test(is_registration)
def home(request):
    value=""
    
    if request.method=="POST":
        # name=request.POST.get('name')
        # print('name',name)
        submitbutton=request.POST.get(all)
        name=""
        form= predictForm(request.POST or None)
        if form.is_valid():
            name= form.cleaned_data.get("name")
        # result=summarize(area)
        # print("",result)
        
        
         



    #filtr=""
        apikey= "svNoF8VJfiOeYQ1CSNXe5Oacj"
        apisecretkey = '8oUX39izHzNEBN58FGW3h8CAh8tmcbJ60FofbBWapyOjQwQMuj'
        acctoken = '1559583431885225984-UxCRL9jQMBkkNOEmuvUj5Yzi1gpd0C'
        acctokensecret ='nIlVPCfGQbsStfHBGrlEQEOPt0pYVOnrDPrmkFPXWZFfY'

        auth =tweepy.OAuthHandler(apikey,apisecretkey)
        auth.set_access_token(acctoken,acctokensecret)
        api=tweepy.API(auth)
        user=name
        #user1 = api.get_user(user)

        #api = tweepy.API(auth)
        user11 = api.get_user(screen_name=name)
        print(user11.name)

        name=user11.name

        print(user11.id)
        id=user11.id


#Fetching followers
        followers = user11.followers_count
  
        print("The description of the user is : ",followers)

# fetching the description
        description = user11.description
        pro=user11.profile_image_url
  
        print("The description of the user is : " + description)
        print('profile url',pro)

        tweets=tweepy.Cursor(api.search_tweets,q='@'+user).items(30)
        # data1=re.split(',',tweets)
        # print(data1)
        
        text1=[]
      
        for t in tweets:
            text1.append(t.text)

        text1=' '.join(text1)
        print('tweets collected',text1)





        api=tweepy.API(auth)
        # Get tweets from user
        name = user

        tweets = api.user_timeline(screen_name=name, count=200)

        if api.user_timeline(screen_name=name):
            # Perform sentiment analysis on tweets
            stress_tweets = []
            for tweet in tweets:
                text = tweet.text
                sentiment = TextBlob(text).sentiment
                if sentiment.polarity < 0:
                    stress_tweets.append(text)

            # Calculate stress level
            stress_level = len(stress_tweets) / len(tweets)

            # Print results
            print("Stress level for user @{} is {:.2f}%".format(name, stress_level * 100))
            stress="Stress level for user @{} is {:.2f}%".format(name, stress_level * 100)
            # request.session["stress"] = stress
            
        tcv=CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("C:\\Users\\Venture Hacker\\Desktop\\stress\\stress\\vocab.pkl","rb")))
        m=load_model('C:\\Users\\Venture Hacker\\Desktop\\stress\\mymodel.h5')
        res=np.argmax(m.predict(tcv.transform([text1])))
        typ=['INFJ', 'ENTP', 'INTP', 'INTJ', 'ENTJ', 'ENFJ', 'INFP', 'ENFP',
        'ISFP', 'ISTP', 'ISFJ', 'ISTJ', 'ESTP', 'ESFP', 'ESTJ', 'ESFJ']
        print("Personality: "+typ[res])
        print('Introversion (I) â€“ Extroversion (E)\nIntuition (N) â€“ Sensing (S)\nThinking (T) â€“ Feeling (F)\nJudging (J) â€“ Perceiving (P)')
    
        if(typ[res])=="INFJ":
            value="25"
        elif(typ[res])=="ENTP":
            value="23"
        elif(typ[res])=="INTP":
            value="30"
        elif(typ[res])=="INTJ":
            value="35"
        elif(typ[res])=="ENTJ":
            value="28"
        elif(typ[res])=="ENFJ":
            value="70"
        elif(typ[res])=="INFP":
            value="48"
        elif(typ[res])=="ENFP":
            value="36"
        elif(typ[res])=="ISFP":
            value="62"
        elif(typ[res])=="ISTP":
            value="56"
        elif(typ[res])=="ISFJ":
            value="67"
        elif(typ[res])=="ISTJ":
            value="40"
        elif(typ[res])=="ESTP":
            value="49"
        elif(typ[res])=="ESFP":
            value="71"
        elif(typ[res])=="ESTJ":
            value="38"
        elif(typ[res])=="ESFJ":
            value="30"
        else:
            print("Unknown")
        print("val is",value)

        # s = pd.Series('value')
        # fig, ax = plt.subplots()
        # s.plot.bar()
        # fig.savefig('my_plot.png')

        
        level1=stress_level*100
        level2=100-level1
        a=int(level1)
        if a > 10:
                messages.success(request,'We prefer to consult a doctor.')
        else:
                messages.success(request,'Normal')

      
        print('stress level 2 is',level2)
        print('stress level 1 is ',level1)
    

        mydict={
            "entered_text":typ[res],
            "percentage":value,
            "id":id,
            "description":description,
            "profilepic":pro,
            "text1":text1,
            "stress":stress,
            "followers":followers,
            "level1":level1,
            "level2":level2,
            
                                   
        }
      
        return render(request,'predict.html',context=mydict)
    else:

        return render(request,'home.html')


def logout_user(request):
    logout(request)
    return redirect('/') 



@login_required(login_url='login')
@user_passes_test(is_registration)
def profile(request):
    
    cr1=registration.objects.get(user=request.user)
    cr=registration.objects.filter(user=cr1.user)
    return render(request,"profile.html",{'cr':cr})   

@login_required(login_url='login')
@user_passes_test(is_registration)
def predict(request):

    return render(request,'predict.html')    

@login_required(login_url='login')
@user_passes_test(is_registration)
def edit(request,pk):
    cr=registration.objects.get(id=pk)
    if request.method == 'POST':
        form=registeruserform(request.POST,instance=cr.user)
        form1=registerform(request.POST,instance=cr)
        if form.is_valid() and form1.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            form1.save()
            return redirect('login')
    else:
        form=registeruserform(instance=cr.user)
        form1=registerform(instance=cr)
        context={'form': form, 'form1': form1}
    return render(request,'edit.html',context)





@login_required(login_url='login')
@user_passes_test(is_registration)
def consult(request):
    cr=doctormodel.objects.all()
    return render(request,'consult.html',{'cr':cr})

@login_required(login_url='login')
@user_passes_test(is_registration)
def consult1(request):
    cr=doctormodel.objects.all()
    return render(request,'consult1.html',{'cr':cr})