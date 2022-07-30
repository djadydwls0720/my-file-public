<?php
    include "dlib.php"; 
    $user=$_SESSION['id_cheack'];
    if($_SESSION['isLogin']===""){?>
        <script>
            location.href="./login2.php";
        </script>
    <?php
        
    }
?>

<link rel="stylesheet" href=/listcss.css>
<body class=background>
    <div class=ID>ID: <?=$user?></div>
    <div class=colum>
        <table width=800 border="1" class=board>
        <tr class=board>
            <th>No</th>
            <th>제목</th>
            <th>작성자</th>
            <th>작성일</th>
        </tr>    
    </div>
    
    
</body>


<?php
    $query="select * from sing_board order by idx desc ";
    $result=mysqli_query($connet,$query);

    while($data=mysqli_fetch_array($result)){
?>
    <tr class=board>
        <td><?=$data['idx']?></td>
        <td> <a href="view.php?idx=<?=$data['idx']?>" class=board><?=$data['subject']?></a></td>
        <td><?=$data['name']?></td>
        <td><?=$data['regdate']?></td>
    </tr>
    
    <?php
}?>



</table>
<div class=button_s>
    <a class=click href="write.php">글쓰기</a>
    <a class="click" href="LogOut.php">로그아웃</a>
    <a class="click" href="propil.php">프로필</a>
</div>