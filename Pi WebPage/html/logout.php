<?php
   session_start();
   unset($_SESSION["username"]);
   // unset($_SESSION["password"]);
   
   echo 'You have cleaned session';
   header('Refresh: 0;URL = index.php');
   //header('Refresh: 2; URL = index.php');
?>

<style>
body {background-color: black;}
</style>
