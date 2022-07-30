<?php
    include "dlib.php";
    
    $isLogin=$_SESSION['isLogin'];
    if(!$isLogin){
        echo "회원만 들어올 수 있습니다"; 
        exit;
    }

?>
    <table width=800 border="1">
        <tr>
            <th>No</th>
            <th>제목</th>
            <th>작성자</th>
            <th>작성일</th>
            <th>작성시간</th>
        </tr>

    </table>

    <a href="write.php?name=">글쓰기</a>