<?php
require_once 'connect.php';
$user = $_GET["user"];
$numOfFrames = $_GET["numOfFrames"];
$date = date('Y/m/d h:i:s', time());
$query = "INSERT INTO `log` (`user`, `date`, `numOfFrames`) VALUES ('$user', '$date', $numOfFrames)";

$result = mysqli_query($connection, $query);
if($result){
echo "record added";
}
else{
echo "Error";
}
?>