<?php 
    // Start MySQL Connection
    require_once 'connect.php';


?>

<html>
<head>
    <title>Stitch Quality Report</title>
    <style type="text/css">
        .table_titles, .table_cells_odd, .table_cells_even {
                padding-right: 20px;
                padding-left: 20px;
                color: #000;
        }
        .table_titles {
            color: #FFF;
            background-color: #666;
        }
        .table_cells_odd {
            background-color: #CCC;
        }
        .table_cells_even {
            background-color: #FAFAFA;
        }
        table {
            border: 2px solid #333;
        }
        body { font-family: "Trebuchet MS", Arial; }
    </style>
</head>

    <body>
        <h1>Stitch Quality Report</h1>


    <table border="0" cellspacing="0" cellpadding="4">
      <tr>
            <td class="table_titles">User</td>
            <td class="table_titles">Date and Time</td>
            <td class="table_titles">Number of Frames</td>
          </tr>
<?php


    // Retrieve all records and display them
    $query = "SELECT * FROM log ORDER BY date DESC";
    $result = mysqli_query($connection, $query);
    echo $result;
    // Used for row color toggle
    $oddrow = true;

    // process every record
    while( $row = mysql_fetch_array($result) )
    {
        if ($oddrow) 
        { 
            $css_class=' class="table_cells_odd"'; 
        }
        else
        { 
            $css_class=' class="table_cells_even"'; 
        }

        $oddrow = !$oddrow;

        echo '<tr>';
        echo '   <td'.$css_class.'>'.$row["user"].'</td>';
        echo '   <td'.$css_class.'>'.$row["date"].'</td>';
        echo '   <td'.$css_class.'>'.$row["numOfFrames"].'</td>';
        echo '</tr>';
    }
?>
    </table>
    </body>
</html>