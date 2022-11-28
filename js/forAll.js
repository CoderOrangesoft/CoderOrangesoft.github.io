 //for all
    document.onselectstart=function(){return false}
    document.oncontextmenu=function(){return false}
    document.ondragstart=function(){return false}
    document.onselect=function(){return false}
    //for header
    window.onload=function()
    {
      try
      {
        showTime();
      }
      catch(err) 
      {
        let txt="未知"
        txt="<JS>时间显示 有错误。\n\n";
        txt+="详细信息:" + err.message + "\n\n";
        console.error(txt);
	    }
    }
    function showTime()
    {
      try
      {
        var today=new Date();
        var y=today.getFullYear();
        var M=today.getMonth()+1;
        var d=today.getDate();
        var h=today.getHours();
        var m=today.getMinutes();
        var s=today.getSeconds();
        m=checkTime(m);
        s=checkTime(s);
        var week=today.getDay();
        var w=new Array('星期天','星期一','星期二','星期三','星期四','星期五','星期六');
        for (var i=0;i<w.length;i++) 
        {
          document.getElementById('time').innerHTML="&nbsp>>>&nbsp当前时间&nbsp"+y+'年'+ M +'月'+d+'日'+" "+h+":"+m+":"+s+" "+w[week];
        }    
        setTimeout('showTime()',500);
      }
      catch(err) 
      {
        let txt="未知"
        txt="<JS>时间加载 有错误。\n\n";
        txt+="详细信息:" + err.message + "\n\n";
        console.error(txt);
	    }
    }
    function checkTime(i)
    {
      try
      {
        if (i<10) 
        {
          i="0" + i;
        }
        return i
      }
      catch(err) 
      {
        let txt="未知"
        txt="<JS>时间格式填充 有错误。\n\n";
        txt+="详细信息:" + err.message + "\n\n";
        console.error(txt);
	    }
    }
