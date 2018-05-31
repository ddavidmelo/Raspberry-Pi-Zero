<html>
     <input type="text" id="Tinput" onkeyup="myFunction()" placeholder="Search bar">
     <table id="Tlog">
     <tr> <th> Time </th> <th> IP Address </th> <th> Browser </th> </tr>

     <?php
       session_start();
       $user = $_SESSION['username'];
       if($user == 'priDav'){
         //$page = file_get_contents("/var/www/html/secure_pages/logs.private"); //original order
  	     //echo $page;
      	 $file = array_reverse( file( "/var/www/html/secure_pages/logs.private" ) ); //reverse order
      	 foreach ( $file as $line ){
      	 echo "$line\n";
    	 }
       }else{echo '<h2>-- Not authorized --</h2>';}
     ?>

<!-- <?php echo $_SESSION['username']; print_r($_SESSION); ?> -->

</html>


<style>
body {
    color: white;
    background-color: black;
}

h1 {
    color: green;
}

html {
    overflow: scroll;
    overflow-x: hidden;
}
::-webkit-scrollbar {
    width: 0px;  /* remove scrollbar space */
    background: transparent;  /* optional: just make scrollbar invisible */
}

#Tlog {
    margin-left: 0px;
    border: 1px solid black;
    border-collapse: collapse;
}

th, td {
    white-space: nowrap;
    padding: 10px;
    text-align: left;    
}

#Tinput {
    color: white;
    border: none;
    background-color: black;
    border-bottom: 2px solid #ccc;
    border-right: 2px solid #ccc;
    border-bottom-right-radius: 5px;
    padding-left: 1%;
}

</style>

<script>
function myFunction() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("Tinput");
  filter = input.value.toUpperCase();
  table = document.getElementById("Tlog");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td0 = tr[i].getElementsByTagName("td")[0];
    td1 = tr[i].getElementsByTagName("td")[1];
    if (td0 || td1) {
      if (td0.innerHTML.toUpperCase().indexOf(filter) > -1 || td1.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}
</script>

