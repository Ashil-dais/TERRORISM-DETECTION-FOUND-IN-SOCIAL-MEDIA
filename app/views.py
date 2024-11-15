from django.shortcuts import render,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import MySQLdb
import datetime
db=MySQLdb.connect("localhost","root","","honorcloud")
c=db.cursor()
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    msg=""
    if request.POST:
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        if cpassword!=password:
            msg="Password doesn't match"
        else:
            c.execute("insert into userreg (fname,lname,email,password) values('"+ fname +"','"+ lname +"','"+ email +"','"+ password +"')")
            db.commit()            
            msg="You have been Registered successfully"
    return render(request,'signup.html',{'msg':msg})


def login(request):
    msg=""
    if request.POST:
        email=request.POST.get("email")
        password=request.POST.get("password")
        if email=="admin@gmail.com" and password=='admin':
            return HttpResponseRedirect("/ahome/")
        else:            
            c.execute("select * from userreg where email='"+email+"' and password='"+password+"' ")
            data=c.fetchone()
            if data:
                request.session["uname"]=email
                request.session["uid"]=data[0]
                c.execute("select * from action where uid='"+ str(data[0]) +"' order by id desc")
                actions=c.fetchall()
                if actions:
                    for i in actions:
                        if request.session["uid"] in i:
                        
                            if i[2]=='block':
                                msg="some reports are chcked and you have violate honorcloud terms and condition reason "
                                msg+=i[4]+" and you have been blocked for few days"
                            elif i[2] == 'removed':
                                msg="some reports are chcked and you have violate honorcloud terms and condition reason "
                                msg+=i[4]+"your account has been permanently blocked"
                            elif i[2]=="warn":
                                msg="some reports are chcked and you have violate honorcloud terms and condition reason =="
                                msg+=i[4]+" ==please behave"
                                request.session['msg']=msg
                                return HttpResponseRedirect("/uhome/")                                


                else:
                    return HttpResponseRedirect("/uhome/")
                 
            else:
                msg="some thing went wrong please check your credentials"

    return render(request,'login.html',{"msg":msg})

def forgotpassword(request):
    password=""
    if request.POST:
        email=request.POST.get("email")
        c.execute("select password from userreg where email='"+ email +"'")
        password=c.fetchone()
        password=password[0]
    return render(request,'forgotpassword.html',{"msg":password})

def uhome(request):
    if "msg" in request.session:
            msg=request.session['msg']
    else:
        msg=""
    imagelist=newimagelist=[]
    c.execute("select * from status where uid='"+str(request.session["uid"]) +"'")
    status=c.fetchall()
   
    if status:
        import random
        for image in status:
            imagelist.append(image[3])
        newimagelist=[]
        for zz in range(4):
            newimagelist.append(random.choice(imagelist))
    else:
        c.execute("select image from status where uid='0'")
        z=c.fetchall()
        newimagelist=[x[0] for x in z]
        
        
    return render(request,'uhome.html',{"status":status,"banner":newimagelist,"msg":msg})

def profile(request):
    request.session['msg']=''
    c.execute("select userreg.*,profile.* from userreg left join profile on profile.email=userreg.email where userreg.email='"+ request.session['uname'] +"'")
    profile=c.fetchone()
    if profile is None:
        profile=[]
    c.execute("select count(*) from message where receiver='"+ request.session['uname'] +"' ")
    mcount=c.fetchone()
   
    return render(request,'profile.html',{"profile":profile,"msgcount":mcount[0]})

def upload_status(request):
    msg=""
    uploaded_file_url=""
    if request.POST:
        text=request.POST.get("text")
        utime=datetime.datetime.now()
        from bad_word_detector import main as check
        result=check(text)
        if result == "Good":        
            if request.FILES.get("file"):
                image=request.FILES.get("file")
                fs=FileSystemStorage()
                filename=fs.save(image.name,image)
                uploaded_file_url = fs.url(filename)       

            c.execute("insert into status values('','"+text+"','"+str(utime)+"','"+ uploaded_file_url +"','"+ str(request.session["uid"]) +"')")
            db.commit()
            msg="status uplaoded"
            # else:
            #     msg="Invalid Image"
        else:
            msg="Please be polite on Honor cloud status or else you willbe reported"


    return render(request,'upload_status.html',{"msg":msg})

def about(request):
    c.execute("select * from profile where email='"+str(request.session["uname"]) +"'")    
    about=c.fetchone()
    if about is not None:
        request.session["dp"]=about[2]
    else:
        request.session["dp"]="/media/du1.jpg"
    
    if request.POST:
        if request.FILES.get("file"):
            pic=request.FILES.get("file")
            fs=FileSystemStorage()
            filedata=fs.save(pic.name,pic)
            picurl=fs.url(filedata)
        else:
            picurl=request.session["dp"]            
        address=request.POST.get("address")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        school=request.POST.get("school")
        college=request.POST.get("college")
        work=request.POST.get("work")
        phone=request.POST.get("phone")

        if about is None:
            c.execute("insert into profile (email,propic,address,gender,dob,school,college,work,phone) values('"+ request.session["uname"] +"','"+ picurl  +"','"+ address  +"','"+ gender  +"','"+ dob  +"','"+ school  +"','"+ college  +"','"+ work  +"','"+ phone  +"')")
        else:
            c.execute("update profile set email='"+ request.session["uname"] +"',propic='"+ picurl +"',address='"+ address +"',gender='"+ gender +"',dob='"+ dob +"',school='"+ school +"',college='"+ college +"',work='"+ work +"',phone='"+ phone +"' where email='"+ request.session["uname"] +"'")
        db.commit()
        return HttpResponseRedirect('/about/')
    

    return render(request,'about.html',{"profile":about})


def gallery(request):
    c.execute("SELECT profile.*,userreg.* FROM profile JOIN userreg on userreg.email=profile.email where userreg.email != '"+ request.session['uname'] +"'  ORDER BY RAND() LIMIT 100 ")
    data=c.fetchall() 
    
    return render(request,'gallery.html',{"data":data})


def viewprofile(request):
    friend=data=""
    if request.GET.get("id"):
        c.execute("SELECT profile.*,userreg.* FROM profile JOIN userreg on userreg.email=profile.email where userreg.email = '"+ request.GET.get("id") +"'")
        data=c.fetchone()
        c.execute("SELECT status FROM `friends` WHERE ((user1='"+ request.session['uname'] +"' and user2='"+ request.GET.get("id") +"') or (user1='"+request.GET.get("id")+"' and user2='"+ request.session['uname'] +"'))")
        friend=c.fetchone()
        if friend ==None:
            friend=['null']
    return render(request,'viewprofile.html',{"data":data,"friend":friend[0]})


def requestlist(request):
    data=[]
    if request.GET.get("status") :
        request.session['action']=st=request.GET.get("status")
        # if st == 'pending':
        # qry="select user2,status from friends where user1='"+ request.session['uname'] +"' and status='"+ st +"'  "
        data=[]
        data2=[]
        c.execute("select user1 from friends where user2='"+ request.session['uname'] +"' and status='"+ request.session['action'] +"' ")
        fr=c.fetchall()
        for i  in fr:
            data.append(i[0])
        # c.execute("select user1 from friends where user2='"+ request.session['uname'] +"' and status='"+ request.session['action'] +"' ")
        # fr=c.fetchall()
        # for i  in fr:
        #     data.append(i[0])
        print(data)
        for i in data:
            c.execute("SELECT fname,lname,userreg.email,profile.* from profile right join userreg on userreg.email=profile.email where userreg.email = '"+ i +"' ")
            data2.append(c.fetchone())
    return render(request,'requestlist.html',{"data":data2,"user":request.session['uname']})

def action(request):
    status=request.GET.get('status')
    friend=request.GET.get('friend')
    query="update friends set status='"+ status +"' where (user2='"+ friend +"' and user1='"+ request.session['uname'] +"') or (user1='"+ friend +"' and user2='"+ request.session['uname'] +"')"    
    c.execute(query)
    db.commit()
    print(query)
    return HttpResponseRedirect('/requestlist/?status='+ request.session['action'])

def addfriend(request):
    utime=datetime.datetime.now()
    if request.GET.get("id"):
        # qry="SELECT count(*) FROM `friends` WHERE ((user1='x' and user2='y') or (user1='y' and user2='x')) and status='rejected'"
        qry="insert into friends values('','"+request.session['uname']+"','"+ request.GET.get("id") +"','"+ str(utime) +"','pending')"
        c.execute(qry)
        db.commit()

        return HttpResponseRedirect('/gallery/')


    
def message(request):
    messages=''
    msg=propic=""
    user=request.session['uname']
    c.execute("SELECT profile.*,userreg.* FROM profile JOIN userreg on userreg.email=profile.email where userreg.email in (SELECT friends.user2 from friends where friends.user1='"+ request.session['uname'] +"' and friends.status='accepted' UNION SELECT friends.user1 from friends where friends.user2='"+ request.session['uname'] +"'and friends.status='accepted')")
    friends=c.fetchall()
    if request.GET.get("id"):
        id= request.GET.get("id")
        request.session['reid']=id
        c.execute("select * from message where sent='"+ request.session['uname'] +"' and receiver='"+ id +"' union select * from message where receiver='"+ request.session['uname'] +"' and sent='"+ id +"' order by date")
        messages=c.fetchall()
        c.execute("select propic from profile where email='"+ id +"'")
        propic=c.fetchone()

    if request.GET.get("report"):
        date=datetime.datetime.today()
        c.execute("insert into messagereport values('','"+ request.session['uname'] +"','"+ request.GET.get("report") +"','"+ str(date) +"','action')")
        db.commit()
        msg="message reported"

    if request.POST:
        msg=request.POST.get("msg")
        from bad_word_detector import main as check
        result=check(msg)
        if result == "Good":
            receiver=request.session['reid']
            date=datetime.datetime.today()
            c.execute("insert into message values('','"+ request.session['uname'] +"','"+ receiver +"','"+ str(date) +"','"+ msg +"')")
            db.commit()
            return HttpResponseRedirect("/message/?id="+id)
        else:
            msg="Please be polite on Honor cloud status or else you willbe reported"
    return render(request,'message.html',{"friends":friends,"messages":messages,"user":user,'msg':msg,"propic":propic})
def viewstatus(request):
    # c.execute("select status.*,userreg.* from status join userreg on status.uid=userreg.uid where status.uid in (SELECT uid from userreg where email in (SELECT friends.user2 from friends where friends.user1='"+ request.session['uname'] +"' and friends.status='accepted' UNION SELECT friends.user1 from friends where friends.user2='"+ request.session['uname'] +"' and friends.status='accepted'))")
    c.execute("SELECT userreg.uid,userreg.fname,userreg.lname,status.text,status.image,status.date,count(slikes.sid),status.sid from userreg join status on userreg.uid=status.uid left join slikes on status.sid=slikes.sid GROUP BY slikes.sid,status.sid")
    status=c.fetchall()

    ##generate random status 
    import random
    l=[]
    for i in status:
        l.append(list(i))
    random.shuffle(l)
    
    return render(request,'viewstatus.html',{"status":l,"liker":request.session['uid']})

def addlike(request):
    sid=request.GET.get("id")
    likerid=request.GET.get("uid")
    c.execute("select count(*) from slikes where luid='"+ str(likerid) +"' and sid='"+ sid +"' ")
    cd=c.fetchone()
    if cd[0]<1:
        c.execute("insert into slikes values('','"+ str(likerid) +"','"+ str(datetime.datetime.now()) +"','"+ str(sid) +"')")
    else:
        c.execute("delete from slikes where sid='"+ sid +"' and luid='"+ likerid +"'")
    db.commit()
    return HttpResponseRedirect("/viewstatus/")

def getstatusdata(request):
    import datetime
    statusdata=''
    comments=""
    msg=""
    if request.GET.get("statuslike"):
        sid=request.GET.get("id")
        likerid=request.GET.get("uid")
        c.execute("select count(*) from slikes where luid='"+ str(likerid) +"' and sid='"+ sid +"' ")
        cd=c.fetchone()
        if cd[0]<1:
            c.execute("insert into slikes values('','"+ str(likerid) +"','"+ str(datetime.datetime.now()) +"','"+ str(sid) +"')")
        else:
            c.execute("delete from slikes where sid='"+ sid +"' and luid='"+ likerid +"'")
        db.commit()
        return HttpResponseRedirect('/getstatusdata/?id='+sid+'&uid='+request.GET.get("uid"))
    elif request.GET.get("id") and request.GET.get("uid"):
        sid=request.GET.get("id")
        uid=request.GET.get("uid")
        c.execute("SELECT userreg.uid,userreg.fname,userreg.lname, status.text,status.image,status.date,count(slikes.sid),status.sid, count(comment.cid) from userreg join status on userreg.uid=status.uid left join slikes on status.sid=slikes.sid left join comment on comment.sid=status.sid where status.sid='"+ sid +"' GROUP BY slikes.sid,status.sid,comment.cid  ")
        statusdata=c.fetchone()
        # c.execute("")
        request.session['sid']=sid
        c.execute("select profile.propic,userreg.fname,userreg.lname,comment.date,comment.comment,count(comment.cid) from \
            profile left join userreg on profile.email=userreg.email left join comment on comment.cuid=userreg.uid \
            join status on comment.sid=status.sid where status.sid='"+ sid +"' GROUP BY comment.cid ")
        comments=c.fetchall()
        
    if request.POST:
        msg=request.POST.get("msg")
        
        date=datetime.datetime.today()
        from bad_word_detector import main as check
        result=check(msg)
        if result == "Good":
            c.execute("insert into comment value('','"+ str(request.session['uid']) +"','"+ str(date) +"','"+ msg +"','"+ str(request.session['sid']) +"')")
            db.commit()
            return HttpResponseRedirect('/getstatusdata/?id='+sid+'&uid='+uid)
        else:
            msg="its not a good comment"
    return render(request,'getstatusdata.html',{"statusdata":statusdata,"msg":msg,"comments":comments,"user":request.session['uid']})



def statusreport(request):
    msg=""
    if request.GET.get("id"):
        sid=request.GET.get("id")
        reporter=request.session['uid']
        date=datetime.datetime.today()
        c.execute("insert into statusreport\
             value('','"+ str(sid) +"','"+ str(reporter) +"','"+ str(date) +"')")
        db.commit()
        msg="your report has been submitted to verification"

    return render(request,'statusreport.html',{"msg":msg})


def addmultiple(request):
    if request.POST:
        files=request.FILES.getlist("file")
        for i in files:            
            fs=FileSystemStorage()
            filename=fs.save(i.name,i)
            uploaded_file_url = fs.url(filename)                
    return render(request,'multiple.html')


def addcomplaints(request):
    msg=""
    if request.POST:
        uid=request.session['uid']
        complaint=request.POST.get('complaint')
        date=datetime.datetime.today()
        c.execute("insert into complaints (description,date,userid)value('"+ str(complaint) +"','"+ str(date) +"','"+ str(uid) +"')")
        db.commit()
        msg="your Complaint has been registered"

    return render(request,'addcomplaints.html',{"msg":msg})
    
def viewcomplaints(request):
    c.execute("select complaints.*,userreg.fname from complaints join userreg where complaints.userid=userreg.uid")
    data=c.fetchall()
    return render(request,'viewcomplaints.html',{"data":data})

def ahome(request):    
    return render(request,'ahome.html')

# def viewcomplaints(request):    
#     return render(request,'viewcomplaints.html')

def viewstatusreport(request):
    c.execute("select statusreport.*,userreg.fname from statusreport join userreg where statusreport.reporterid=userreg.uid")
    data=c.fetchall()
    status=""
    msg=''
    if request.GET.get('statusid'):
        statusid=request.GET.get('statusid')
        c.execute("select * from status where sid='"+ statusid +"'")
        status=c.fetchone()
        request.session["s_id"]=status[4]
        request.session["status_id"]=statusid
    if 'warn'in request.POST:
        c.execute("insert into `action` values('','"+ str(request.session["s_id"]) +"','warn','"+ request.session["status_id"] +"','status')")
        db.commit()
        msg='user has been warned about the case'
    if 'remove'in request.POST:
        c.execute("insert into `action` values('','"+ str(request.session["s_id"]) +"','remove','"+ request.session["status_id"] +"','status')")
        db.commit()
        msg='user has been Removed from Honor cloud Because of broken our rules'
    if 'block'in request.POST:
        c.execute("insert into `action` values('','"+ str(request.session["s_id"]) +"','block','"+ request.session["status_id"] +"','status')")
        db.commit()
        msg='user has been blocked for and we will meet you soon'
    return render(request,'viewstatusreport.html',{"data":data,"status":status,"msg":msg})


def viewmessagereport(request):
    data=msg=message=""
    c.execute('select * from messagereport')
    data=c.fetchall()
    if request.GET.get('user') and request.GET.get("reported"):
        user=request.GET.get('user')
        reported=request.GET.get("reported")
        c.execute("select uid from userreg where email='"+ reported +"' ")
        reportedid=c.fetchone()
        reportedid=request.session["s_id"]=str(reportedid[0])
        
        c.execute("select * from message where sent='"+ user +"' and receiver='"+ reported +"' union select * from message where receiver='"+ user +"' and sent='"+ reported +"' order by date")
        message=c.fetchall()
        print(message)
        request.session["status_id"]=str(message[0][0])
    if 'warn' in request.POST:
        c.execute("insert into `action` values('','"+ str(request.session["s_id"]) +"','warn','"+ request.session["status_id"] +"','message')")
        db.commit()
        msg='user has been warned about the case'
    if 'remove' in request.POST:
        c.execute("insert into `action` values('','"+ str(request.session["s_id"]) +"','remove','"+ request.session["status_id"] +"','message')")
        db.commit()
        msg='user has been Removed from Honor cloud Because of broken our rules'
    if 'block' in request.POST:
        c.execute("insert into `action` values('','"+ str(request.session["s_id"]) +"','block','"+ request.session["status_id"] +"','message')")
        db.commit()
        msg='user has been blocked for and we will meet you soon'
    return render(request,'viewmessagereport.html',{"data":data,"msg":msg,'message':message})

def admin_change_block(request):
    c.execute("select *,userreg.fname,userreg.lname from action join userreg on action.uid=userreg.uid where action.actions='block'")
    data=c.fetchall()
    if request.GET.get("aid"):
        # c.execute("update action set actions='unblock' where id='"+ str(request.GET.get("aid")) +"' ")
        c.execute("delete from action where id='"+ str(request.GET.get("aid")) +"' ")
        db.commit()
        return HttpResponseRedirect("/admin_change_block/")
    return render(request,'admin_change_block.html',{"data":data})

def friends(request):
    data=[]
    data2=[]
    c.execute("select user2 from friends where user1='"+ request.session['uname'] +"' and status='accepted' ")
    fr=c.fetchall()
    for i  in fr:
        data.append(i[0])
    c.execute("select user1 from friends where user2='"+ request.session['uname'] +"' and status='accepted' ")
    print("select user1 from friends where user2='"+ request.session['uname'] +"' and status='accepted' ")
    fr=c.fetchall()
    for i  in fr:
        data.append(i[0])
    print(data)
    for i in data:
        c.execute("SELECT fname,lname,profile.* from profile join userreg on userreg.email=profile.email where userreg.email = '"+ i +"' ")
        data2.append(c.fetchone())
        
    print(data2)
    return render(request,'requestlist1.html',{"data":data2})