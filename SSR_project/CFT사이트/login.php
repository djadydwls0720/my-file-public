<?php
    include "dlib.php";
    $isLogin=$_SESSION['isLogin'];
    if(!$isLogin){?>
        로그인 해라 자슥아<br>
        <a href="./login2.php">login</a>
    <?php
    }else{?>
        
        <script>
            location.href="/list.php"
        </script>
    <?php
    }?>