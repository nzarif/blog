/**
 * Created by niloofar on 06/05/2017.
 */
function getpost() {
    var x=new XMLHttpRequest();
    pid=localStorage.pid;
    x.open("GET","https://ce419.herokuapp.com/blog/post?id="+pid,false)
    x.setRequestHeader("X-Token",localStorage.token);
    x.onload=function () {
        var ans=x.responseText;
        //alert(JSON.stringify(x.responseText));
        ans=JSON.parse(ans);
        var s=JSON.stringify(ans.post.title);
        s=s.toString();
        s=s.substr(1,s.length-2);
        document.getElementById("ttl").innerHTML= s+"<br>";
        var t=JSON.stringify(ans.post.text);
        t=t.toString();
        t=t.substr(1,t.length-2);
        t=t.split('\\r\\n').join('<br>');
        var dt=JSON.stringify(ans.post.datetime);
        dt=dt.toString();
        dt=dt.substr(1,dt.length-2);
       document.getElementById("txt").innerHTML=t+"<br><hr>"+"<a href='commentshow.html' >comments</a>";
       document.getElementById("date").innerHTML=dt;

    };
    x.send();
}
function getcm() {
    var y=new XMLHttpRequest();
    pid=localStorage.pid;
    y.open("GET","https://ce419.herokuapp.com/blog/comments?post_id="+pid,false);
    y.setRequestHeader("X-Token",localStorage.token);
    y.onload=function () {
        var ans=y.responseText;
        ans=JSON.parse(ans);
        //alert(JSON.stringify(ans));
        var c=ans.comments;
        for(i=0;i<c.length;i++){
            var t=c[i];
            t=JSON.stringify(t.text);
            t=t.toString();
            t=t.substr(1,t.length-2);
            t=t.split('\\r\\n').join('<br>');
            //alert(t);
            var dt=JSON.stringify(c[i].datetime);
            dt=dt.toString();
            dt=dt.substr(1,dt.length-2);
            //alert(dt);
            document.getElementById("txt").innerHTML=t+"<br><hr>";
            document.getElementById("date").innerHTML=dt+"<br><hr>";
        }
    };
    y.send();
}
function  postget() {
    var i=0;
    var m,t,s,a,b,c,d,e,g,ans,f,cnt;
    var is=true;
    var h=[];
    var offset=0;
    while(is){
    var y=new XMLHttpRequest();
    y.open("GET","https://ce419.herokuapp.com/blog/posts?offset="+offset,false);
    y.setRequestHeader("X-Token",localStorage.token);
    y.onload=function () {
        i=0;
        ans=y.responseText;
        ans=JSON.parse(ans);
        f=ans.posts;
        cnt=f.length;
        //alert(cnt);
        if (cnt<5)
            is=false;
        while(i<cnt){
            m=f[i];
            h.push(m);
            t=m.title;
            //alert(t);
            t=JSON.stringify(t);
            //alert(i<cnt);
            t=t.toString();
            t=t.substr(1,t.length-2);
            t=t.split('\\r\\n').join('<br>');
            s=JSON.stringify(m.summery);
            s=s.toString();
            s=s.substr(1,s.length-2);
            s=s.split('\\r\\n').join('<br>');
            //alert(t);
            //alert(s);
            a=document.createElement('div');
            a.className="post";
            a.id="pst"+i;
             b=document.createElement('p');
             b.className="post";
             b.id="post"+i;
            c=document.createElement('a');
            c.id="link"+i;
            d=document.createElement('p');
            d.className="date";
            d.id="date"+i;
            e=document.createElement('p');
            e.className="author";
            e.id="authr"+i;
            e.innerHTML=t+"<br>"+"<hr>";
            c.innerHTML="read more";
            c.href="getpost.html";
            c.onclick=function(){
                var me=this.id.charAt(this.id.length-1);
               // alert(me);
                localStorage.setItem("pid",h[me].id);
            window.location.href="getpost.html";};
            d.innerHTML=m.datetime;
            a.appendChild(e);
            b.innerHTML=s+"<br>";
            a.appendChild(b);
            a.appendChild(d);
            a.appendChild(c);
            g=document.getElementById("full");
            g.appendChild(a);
            //alert(i);
            //alert(cnt);
            i++;
        }
    };
    y.send();
    offset=offset+5;
    }
}