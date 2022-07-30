<?php
    $memo=$_GET['memo'];

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>회원가입</title>
    <link rel="stylesheet" href="joincss.css">
</head>
<div class=col>
    <body class=background>
    <form action="./joinProc.php" method="post" class=col > 
        <h1 class=h>JOIN CTF</h1>
    
        <input class=text type="text" name="uid" placeholder="아이디" > <br>
          <input class=text type="password" name="pwd" placeholder="비밀번호" > <br>
          <input class=text type="password" name="pwd_re" placeholder="재입력" > <br>
          <input class=text type="text" name="name" placeholder="이름" > <br>
          <div class=c>
              <button class=joinbut type="submit">회원가입</button><br>
              <a class=joinbut href="./login2.php">취소</a>
              
          </div>
          <?php
            echo("$memo");
            ?>
    </body>
</div>
</html>