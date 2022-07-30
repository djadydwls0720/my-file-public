<?php
    include "dlib.php";
    $id=$_POST['uid'];
    $pwd=$_POST['pwd'];
    $pwd_re=$_POST['pwd_re'];
    $name=$_POST['name'];

    $query="select * from members where uid='$id'";
    $result=mysqli_query($connet,$query);
    $data=mysqli_fetch_array($result);

    if($pwd===$pwd_re){
        if($data['uid']===$id){
            ?>
            <script>
                location.href="join.php?memo='아이디가 겹칩니다!'"
            </script>
            <?php
        }
        else{
            $query="insert into members(uid, pwd, name) values('$id', '$pwd', '$name')";
            mysqli_query($connet, $query);
            
            ?>
            <script>
                location.href="login.php"
            </script>
            <?php
        }
    }
    else{
        ?>
        <script>
            location.href="join.php"
        </script>
        <?php
    }
?>