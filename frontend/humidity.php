<?php 
$url = "http://ip:port/humidity";
$jsonUrl = file_get_contents($url);
$json_idr = json_decode($jsonUrl);
header('Content-Type:application/json;charset=utf-8');
echo json_encode($json_idr->visibility);

 ?>