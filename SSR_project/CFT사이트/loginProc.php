<?php
    include "dlib.php";
    $uid=$_POST["uid"];
    $pwd=$_POST["pwd"];
    $uid=mysqli_real_escape_string($connet,$uid);
    $pwd=mysqli_real_escape_string($connet,$pwd);
    //$sql="select * from members where uid='?' and pwd='?'";
    //$stmh=$connet->prepare($sql);
    //$stmt->mysqli_stmt_bind_param("ss", $uid, $pwd);
    //$stmh->execute([$uid,$pwd]);
    //echo $stmh;
    $result=mysqli_query($connet,"select * from members where uid='$uid' and pwd='$pwd'");
    //$stmt->mysqli_stmt_execute();
    //$result = $stmt->mysqli_stmt_get_result();
    
    $data=mysqli_fetch_array($result);
    $connet->close();
    if($result->num_rows>0){
        $_SESSION['isLogin']=time();
        $_SESSION['id_cheack']=$uid;
?>
        <script>
            location.href="./list.php";
        </script>
<?php
    }else{?>

        <script>
            location.href="./login2.php?login=f";
        </script>
<?php
    }?>
