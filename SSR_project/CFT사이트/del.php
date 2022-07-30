<?php
    include "dlib.php";
    
    $idx=$_GET['idx'];
    echo $idx;
    $uid=$_SESSION['id_cheack'];
    $query="delete from sing_board where idx='$idx'";
    mysqli_query($connet, $query);
?>
<script>
    location.href="list.php";
</script>