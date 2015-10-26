<?php

$link = mysqli_connect(get_env('DB_HOSTNAME'), 'root', 'B4c0n1234', 'test');

if (!$link) {
  die('Can\'t connect to MySQL.');
}

echo mysqli_get_host_info($link) . PHP_EOL;
mysqli_close($link);
