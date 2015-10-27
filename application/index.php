<?php

require_once('./config.php');

session_start();

if (!isset($_SESSION['message'])) {
  $_SESSION['message'] = 'test';
  echo 'Session message set. Refresh page to see.';
} else {
  echo $_SESSION['message'];
}

$link = mysqli_connect(DB_HOSTNAME, 'root', 'B4c0n1234', 'test');

if (!$link) {
  die('Can\'t connect to MySQL.');
}

echo mysqli_get_host_info($link) . PHP_EOL;
mysqli_close($link);
