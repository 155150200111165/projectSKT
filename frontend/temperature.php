<?php 
$url = "http://10.36.3.104:5002/temperature";
$jsonUrl = file_get_contents($url);
$json_idr = json_decode($jsonUrl);
header('Content-Type:application/json;charset=utf-8');
echo json_encode($json_idr);
 ?>