/**
 * Created by niloofar on 04/05/2017.
 */
function registerfunc() {
    var stid=document.getElementById("stid").value;
    var pass=document.getElementById("pwd").value;
    var first=document.getElementById("fname").value;
    var last=document.getElementById("lname").value;
    var mail=document.getElementById("email").value;
var object = new FormData();
    object.append('student_number', stid);
    object.append('password', pass);
    object.append('first_name', first);
    object.append('last_name', last);
    object.append('email', mail);
var a = new XMLHttpRequest();
a.open("POST", "https://ce419.herokuapp.com/auth/register",false);
a.onreadystatechange = function () {
        var ans = JSON.parse(a.responseText);
        if(ans.status==0){
            window.location.href="welcome.html";
            //alert("done");
        }
        ans=JSON.stringify(ans);
       //rt(ans);
    };
a.send(object);
/*if(a.status==0)
    alert("success");
else
    alert("fail");*/
}
function loginfunc() {
    var stid1=document.getElementById("stid").value;
    var pass1=document.getElementById("pwd").value;
    var object = new FormData();
    object.append('student_number', stid1);
    object.append('password', pass1);
    var b = new XMLHttpRequest();
    b.open("POST", "https://ce419.herokuapp.com/auth/login",false);
  b.onreadystatechange = function () {
        var ans1 = JSON.parse(b.responseText);
        var ans2=JSON.stringify(ans1);
        //alert(ans2);
        if(ans1.status==0){
            token=ans1.token;
            //alert(token);
            localStorage.setItem("token", token);
            //alert("done");
            window.location.href="share.html";
        }
    };
b.send(object);
}
function postfunc() {
    var title=document.getElementById("ttl").value;
    var summary=document.getElementById("sum").value;
    var text=document.getElementById("txt").value;
    var c=new XMLHttpRequest();
    var token=localStorage.token;
    //alert(token);
    var object2=new FormData();
    object2.append('title',title);
    object2.append('summary',summary);
    object2.append('text',text);
    c.open("POST","https://ce419.herokuapp.com/blog/post",false);
    c.setRequestHeader("X-Token",token);
    c.onreadystatechange=function () {
        //alert("onload");
        var ans2=JSON.parse(c.responseText);
        if(ans2.status==0){
            window.location.href="getpost.html";
            localStorage.setItem("post_id",ans2.post_id);
            localStorage.setItem("pid",ans2.post_id);
            alert(ans2.post_id);
        }
        ans2=JSON.stringify(ans2);
       //alert(ans2);
    };
    c.send(object2);
    /*if(c.status==0)
    alert("success");
else
    alert("fail");*/
}
function cmfunc() {
    var id=document.getElementById("pid").value;
    var text=document.getElementById("txt").value;
    var object3=new FormData();
    object3.append('post_id',id);
    object3.append('text',text);
    var d=new XMLHttpRequest();
    d.open("POST","https://ce419.herokuapp.com/blog/comment",false);
    var token=localStorage.token;
    d.setRequestHeader("X-Token",token);
    d.onreadystatechange=function () {
        //alert("onload");
        var ans3=JSON.parse(d.responseText);
        if(ans3.status==0){
            window.location.href="commentshow.html";
        }
        ans3=JSON.stringify(ans3);
        //alert(ans3);
    };
    d.send(object3);
    /*if(d.status==0)
    alert("success");
else
    alert("fail");*/
}