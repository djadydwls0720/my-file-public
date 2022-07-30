<?php
    include "dlib.php";
    $name=$_SESSION['id_cheack'];
    $idx=$_POST['idx'];
    $subject=$_POST['subject'];
    $memo=$_POST['memo'];
    $id_cheack=$_SESSION['id_cheack'];
    
    $memo=str_replace("<","〈", $memo);
    $memo=str_replace(">","〉", $memo);
    $subject=str_replace("<","〈", $subject);
    $subject=str_replace(">","〉", $subject);
    //$name=mysqli_real_escape_string($name);
    //$subject=mysqli_real_escape_string($subject);
    //$memo=mysqli_real_escape_string($memo);


    if($idx){
        $query="update sing_board set name='$name', subject='$subject',memo='$memo' where idx='$idx'";
    
        mysqli_query($connet, $query);

    }else{

    $regdate=date("Y-m-d");
    $ip=$_SERVER['REMOTE_ADDR'];
    if($subject==""){
        $subject="제목없음";
    }
    $query="insert into sing_board(name, subject, memo, regdate,ip,id_cheack) values('$name', '$subject', '$memo', '$regdate','$ip','$id_cheack')";

    $a=mysqli_query($connet, $query);
    
            
}

?>
<script>
    location.href="list.php";
</script>