<?php
    include "dlib.php";
    $f=$_GET["login"];
?>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>로그인</title>
    <link rel="stylesheet" href="./loginfrom.css">
</head>
<body class=background>
    <div class=box2>
        <div class=box>
            <h1 class=LOGIN>
                LOGIN CTF
            </h1>
            <form action="./loginProc.php" method="post" class=loginfrom> 
                <div class=Loginbox>
                    <div>
                        <input type="text" name="uid" class=inputbox placeholder="아이디"> <br>
                    </div>
                    
                    <div>
                    <input type="password" name="pwd" class=inputbox placeholder="비밀번호"> <br>
                    </div>
                </div>
            
                <button type="submit" class=BUTTON_LOGIN>로그인</button>
                <a href="./join.php?memo=" class=JOIN_LOGIN >회원가입</a>
              <?php
                    if($f==="f"){?>
                        <h1 class=error>입력 정보가 올바르지 않습니다.</h1>
                        
                    <?php
                        
                    }
                  ?>
        </div>
    </div>
    

</form>
    
</body>
</html>