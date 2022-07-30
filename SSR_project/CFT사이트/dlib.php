<?php
    session_start();
    error_reporting(1);
    ini_set("display_errors",1);
    $connet=mysqli_connect("localhost","korea","yong0021", "korea");
    if(mysqli_connect_error()){
        echo mysqli_connect_error();
    }
        
?>