import re

text = """
<html>
<head>
<title>URP 综合教务系统 - 登录</title>
<link href="/css/newcss/login.css" rel="stylesheet" type="text/css">
<link href="/css/newcss/project.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="/js/jquery-1.6.1.min.js"></script>
</head>
<script type='text/javascript'>
function login(){
	 if(document.loginForm.zjh.value == ""){
		alert("请输入您的帐号");
		document.loginForm.zjh.focus();
		return ;
     }
	if(document.loginForm.mm.value == ""){
		alert("请输入您的密码");
		document.loginForm.mm.focus();
		return ;
     }
	if(document.loginForm.v_yzm.value == ""){
		alert("请输入验证码");
		document.loginForm.v_yzm.focus();
		return ;
     }
    document.loginForm.submit();
}
function m_changeOne(){
  //document.getElementById("vchart").src="/validateCodeAction.do?random="+Math.random();
  $("#vchart").attr("src","/validateCodeAction.do?random="+Math.random());
}
function valiCode(){
	document.getElementById("vchart").src="/validateCodeAction.do?random="+Math.random();
}
</script>
<body leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" style="overflow:auto;" onload="valiCode()">
<table width="100%" height="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td align="center">
	<table width="525" border="0" cellspacing="0" cellpadding="0" background="/img/pic/login/bg-top.jpg">
  <tr>
    <td width="107"><img src="/img/pic/login/top-left.jpg" width="107" height="39"></td>
    <td width="256" class="adtitle">提供全新教务管理方案</td>
    <td width="147" align="right" valign="bottom">
	</td>
    <td width="10"><img src="/img/pic/login/top-right.jpg" width="15" height="39"></td>
  </tr>
</table>
<table  border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td class="linelogin"></td>
  </tr>
</table>
<table border="0" cellspacing="0" cellpadding="0" class="mainbox">
  <tr>
    <td width="33">&nbsp;</td>
    <td width="352" valign="top">
    <form method="post" name="loginForm" action="/loginAction.do" onSubmit="return login();">
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td>
		<table width="100%" border="0" cellspacing="20" cellpadding="0">
  			<tr>
   			 <td height="60" class="font12" valign="bottom"> 
   			 <table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td class="font11">
				</td>
			</tr>
              <tr>
                 
     			 <td><img src="/img/icon/alert.gif"></td>
     			 <td class="errorTop"><strong><font color="#990000">你输入的验证码错误，请您重新输入！</font></strong><br></td>
     			 
              </tr>
            </table></td>
  			</tr>
		</table></td>
      </tr>   
      <tr>
        <td>
		
		<table width="100%" border="0" cellspacing="6" cellpadding="0" class="font-b">
  			<tr>
    			<td align="right" width="67">
    			<span id="userName_label">帐号</span>:    			</td>
    			<td>
    			<input type="text" name="zjh" value="" class="input01" title="帐号" alt="notnull"></td>
  			</tr>
  			<tr>
    			<td align="right" width="67">
    			<span id="password_label">密码</span>:    			</td>
    			<td>
    			<input type="password" name="mm" value="" class="input01" title="密码" alt="notnull"></td>
  			</tr>
			<tr>
				<td align="right" width="67">
					<span id="password_label">验证码</span>:
				</td>
				<td colspan="2" align="left">
					<input type="text" name="v_yzm" size="4"
						title="验证码" alt="notnull">
				<img src="" id="vchart" height="20" width="80">
				&nbsp; 
				<a onclick="m_changeOne();" style="cursor:pointer; color:blue;" >看不清，换一张</a>
				</td>
			</tr>
		</table>		</td>
      </tr>
      <tr>
        <td align="center">
		<table width="250" border="0" cellspacing="8" cellpadding="0">
		  <tr>
			<td align="right">
			<input type="image" name="" src="/img/zh/login.gif" border="0" onclick="login(); return false;" id="btnSure" class="buttonImg" title="登录">         </td>
			<td align="center">
			<input type="image" name="" src="/img/zh/reset.gif" border="0" onclick="reset(); return false" class="buttonImg" title="重设">			</td>
		  </tr>
		</table>		</td>
      </tr>
      <tr height="100%">
        <td align="left" valign="bottom">&nbsp;</td>
      </tr>
    </table>
    </form>
	<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td align="left" valign="bottom">&nbsp;</td>
  </tr>
   <tr>
    <td align="left" valign="bottom">&nbsp;</td>
  </tr>
  
</table>

	</td>
    <td width="138" align="right" valign="bottom"><img src="/img/pic/login/stamp.jpg" width="138" height="103"></td>
  </tr>
  <tr><td width="525" colspan="3" class="buildnumber" height="12" align="right"><font color="#555555">版本号：1.3_8</font></td></tr>
</table>

<table width="525" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td width="20"><img src="/img/pic/login/bottom-left.jpg" width="20" height="27"></td>
   
    <td width="490" class="bottom">太原理工大学教务处</td>
    <td width="15"><img src="/img/pic/login/bottom-right.jpg" width="15" height="27"></td>
  </tr>
</table>

	</td>
  </tr>
</table>
</body>
</html>
"""


if __name__ == '__main__':

    def result_handler():
        m = re.findall(r'(?=<title>)<title>(.*)(?=</title>)', text, flags=re.M)
        for i in m:
            if i == '学分制综合教务':
                return True, None

        err = re.findall('<font color=\"#990000\">(.*?)</font>', text)


        '你输入的验证码错误，请您重新输入！'
        for i in err:
            if len(i) > 0:
                if i.find('验证码错误'):
                    return False, None
                return False, i

        return False, '出现未知错误,请稍后重试'

    print(f())

    # app.run(port=8080)
