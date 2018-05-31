<!DOCTYPE html>
<?php
   // url example : http://188.250.115.44/?t=1233&v=7
   $time = $_GET["t"];
   $voltage = $_GET["v"];
   if (!empty($time) && !empty(voltage)) {
      $VoltageLog = fopen("/var/www/html/secure_pages/esp8266.private", "a");
      fwrite($VoltageLog, "\n ['$time',$voltage]," );
      fclose($VoltageLog);
   }
   ob_start();
   session_start();
   // open up the log fil
   // give permissions to the file »sudo chmod 777 logs.private
   $file=fopen( "/var/www/html/secure_pages/logs.private" , "a");
   $ip = $_SERVER['REMOTE_ADDR'];
   $browser = $_SERVER['HTTP_USER_AGENT'];
   $time=date("Y-m-d H:i:s");

   fwrite($file, "\n <tr>" );
   fwrite($file, "<td> $time </td>" );
   fwrite($file, "<td> $ip </td>");
   fwrite($file, "<td> $browser </td>");
   fwrite($file, "</tr>" );

   fclose($file);
?>

<html>
  <head>
    <meta charset="UTF-8">
    <title>Nice boat</title>
    <script src="libraries/p5.js" type="text/javascript"></script>
    <script src="libraries/p5.dom.js" type="text/javascript"></script>
    <script src="libraries/p5.dom.min.js" type="text/javascript"></script>
    <script src="libraries/p5.sound.js" type="text/javascript"></script>
    <script src="sketch.js" type="text/javascript"></script>
  </head>
  <body>
	<div>
	<?php
	// error_reporting(E_ALL);
	// ini_set("display_errors", 1);
	$passColour = '#ccc';
	if (!empty($_POST['PassInput'])) {
	   if ($_POST['PassInput'] == 'YourPassword'){
	      $_SESSION['valid'] = true;
	      $_SESSION['timeout'] = 30;//time()
	      $_SESSION['username'] = 'priDav';

	      $passColour = '#9ACD32';
		  header("Location: page.php", true, 301);
	      exit();
	   }else {
	      $passColour = '#FF0000';
	   }
	}
	?>
	</div> 
	<!-- /container -->
	<div class="DivInputBox">
		<form action = "<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method = "post">
			<input type="password" name="PassInput" id="PassInput" placeholder="Password"><br>
			<input type="submit" style="visibility: hidden;position: absolute; left: -9999px; width: 1px; height: 1px;" />
		</form>
	</div>    

  </body>
</html>

<style>
	/* https://github.com/processing/p5.js/wiki/Positioning-your-canvas */
	html, body {
		height: 100%;
	}

	body {
		margin: 0;
		display: flex;

		/* This centers our sketch horizontally. */
		justify-content: center;

		/* This centers our sketch vertically. */
		align-items: center;
	}
	div.DivInputBox {
	    /* border: 3px solid #73AD21; */
	    position:absolute;
        top: 0px;
		left: 0px;
	}
	input[type=password] {
    	padding: 9px 15px;
    	border: none;
    	background-color: transparent;
    	border-bottom: 3px solid <?php echo $passColour ?>;
    	border-right: 3px solid <?php echo $passColour ?>;
    	-webkit-transition: 0.5s;
    	transition: 0.5s;
    	outline: none;
    	border-bottom-right-radius: 7px;
	}

	input[type=password]:focus {
	    border: 3px solid #555;
	    background-color: white;
	}
</style>
