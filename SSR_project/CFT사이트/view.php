<?php
    include "dlib.php";
    if($_SESSION['isLogin']===""){?>
        <script>
            location.href="./login2.php";
        </script>
    <?php
    }
    $idx=$_GET['idx'];
    $uid=$_SESSION['id_cheack'];
    $user=$_SESSION['uid'];
    $query="select * from sing_board where idx='$idx'";
    $result=mysqli_query($connet,$query);
    $data=mysqli_fetch_array($result);
    $user_cheack=$_SESSION['id_cheack'];
    $view=$data['view'] +1 ;
    $query="UPDATE sing_board SET view = '$view' WHERE idx='$idx'";
    mysqli_query($connet,$query);
?>
<link rel="stylesheet" href="writecss.css">
<div class=col>
    <body class=background>
    <form action="list.php" method="post">
    <table width=800 border="1" cellpadding=5>
        <tr class=color>
            <td>
                <div type="text" name="subject" style="width: 100%;" class=sub>
                    <?=$data['subject']?>
                <div>
                <div class=name><?=$data['name'];?></div>
            </td>
        </tr>
        <tr class=color>
            <td> <div name="memo" style="width: 100% height:100%"><?=nl2br($data['memo'])?></div> </td>
        </tr>
        <tr class=color>
            <td colspan="2">
                <div style="text-align:center; ">
                    <button type="submit" class=list>목록</button>
                    <?php
                        if($data['id_cheack']==$user_cheack or $_SESSION['id_cheack']=="admin"){
                            ?>
                            <a class=color href="del.php?idx=<?=$idx?>">삭제</a>
                            <a class=color href="write.php?idx=<?=$idx?>">수정</a>
                            <?php
                        }
                    ?>
                </div>
            </td>
        </tr>
    </table>
</form>
<div>
    
</div>
<div class=view_color>조회수: <?=$view?></div>
</body>
    
</div>

