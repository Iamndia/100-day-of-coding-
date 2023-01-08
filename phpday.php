<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Nadia</title>
</head>
<body>

	<!-- membuat variabel dengan php -->
	<?php 
	$nama = "nadia";
	$nim =" D0222022";
	echo $nama." ".$nim;
	?>


	<!-- operator dalam php -->
	<!-- opereator aritmatika -->
	<!-- +,-,/,*,% -->
	<!-- 1. cara biasa -->

	<?php
	echo 1 + 1; 
	// cara dengan menggunakan variabel
	$x = 10;
	$y = 10;
	$z = $x + $y;
	echo $z;
	// atau
	echo $x + $y;

	 ?>

	 <!-- operator logika -->
	 <!-- &&(AND),||(OR),!=(NOT) -->
	 <?php
	 $n = 10;
	 $m = 20;
	 var_dump($n <= $m && $n >= $m); 
	 var_dump($n <= $m || $n >= $m); 
	 var_dump($n <= $m != $n >= $m); 
	 ?>
	 <!-- macam-macam cara mencetak value dengan php -->
	 <?php 
	 echo"Nadia";
	 print"D0222022";
	 print_r("nadia");//harus menggunakan kurung
	 var_dump("Nadia");//menampilkan tipe data serta jumlah dalam string
	  ?>

	  <!-- operator assigment -->
	  <!-- =,!=,+=,-=,*=,/=,.=,%= -->
	  <?php
	  $a = 2;
	  $a += 2;
	  $a -= 3;
	  $a %= 2;
	  $a.= 2;
	  echo $a; 

	   ?>
	   <!-- operator perbandingan  -->
	   <!-- ==,===,>=,<=,<,> -->
	   	<?php
	   	$a = 20;
	   	$b = 10;
	   	var_dump($a == $b); 
	   	 ?>


</body>
</html>