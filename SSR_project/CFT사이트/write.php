<?php
    include "dlib.php";
    $idx=$_GET['idx'];
    $query="select * from sing_board where idx='$idx'";
    $result=mysqli_query($connet,$query);
    $data=mysqli_fetch_array($result);
?>
<link rel="stylesheet" href="./writecss.css">
<body class=background>
    <form action="writePost.php" method="POST" class=col>
    <input type="hidden" name="idx" value="<?=$idx?>">
    <table width=800 border="1" cellpadding=5>
            
            <tr class=color>
                <th>제목 </th>
                <td> <input type="text" name="subject" style="width: 100%;" value='<?=$data['subject'];?>'> </td>
            </tr>
            <tr class=color>
                <th>내용 </th>
                <td> <textarea name="memo" style="width: 100%; height:400px;"><?=$data['memo'];?></textarea>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div style="text-align:center; ">
                        <input type="submit" class=color_but value=저장>
                        <a href="list.php"class=color>취소</a>
                    </div>
                </td>
            </tr>
    </table>

    </form>
    
</body>
