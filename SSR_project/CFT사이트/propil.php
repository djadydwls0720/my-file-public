<?php

include "dlib.php";
$user=$_SESSION['id_cheack'];

$query="select * from members where uid='$user'";
$result=mysqli_query($connet,$query);
$data=mysqli_fetch_array($result);

?>