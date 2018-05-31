<a class="topbar but1" onclick="setURL('secure_pages/logs.php')"> <span></span> Logs </a>
<a class="topbar but2" onclick="setURL('secure_pages/esp8266.php')"> <span></span> esp8266 </a>

<div class="front_frame">
    <iframe id=iframe src="secure_pages/logs.php" width="100%" height="100%" marginwidth="0" marginheight="0" frameborder="0"><p>Your browser does not support iframes.</p></iframe>
    <a href = "logout.php">
       <div class="logout">
       </div>
	</a>
</div>

<!-- <?php echo $_SESSION['username']; print_r($_SESSION); ?> -->

<style>
body {
    color: white;
    background-color: black;
}

h1 {
    color: green;
}

iframe{
}

div.front_frame {
    border:2px solid #ccc;
    border-radius: 5px 5px 50px 5px; 
    font:16px/26px, Georgia, white;
    overflow:auto;

    width: 80%;
    height: 80%;

    position: absolute;
    top:0;
    bottom: 0;
    left: 0;
    right: 0;

    margin: auto;
}

div.logout {
    border:2px solid #ccc;
    border-radius: 5px 5px 5px 5px;
    background: red;
    text-align: center;
    color: white;
    font-family: "Arial", sans-serif;
    overflow: hidden;

    position: absolute;
    top: -2px;
    right: -2px;

    width: 3%;
    height: 3%;
}

html {
    overflow: scroll;
    overflow-x: hidden;
}
::-webkit-scrollbar {
    width: 0px;  /* remove scrollbar space */
    background: transparent;  /* optional: just make scrollbar invisible */
}

a.topbar
{
    position: absolute;
    top: 10px;
    height: 30px;
    background: black;
    text-transform: uppercase;
    text-align: center;
    line-height: 30px;
    color: #ccc;
    text-decoration: none;
    font-size: 16px;
    font-family: verdana;
    letter-spacing: 4px;
}

a.topbar.but1
{
    left: 40px;
    width: 100px;
}

a.topbar.but2
{
    left: 180px;
    width: 140px;
}
a.topbar:before,
a.topbar:after,
span:before,
span:after
{
    content: '';
    position: absolute;
    width: 10px;
    height: 10px;
    background: #ccc;
    transition: 1s;
    mix-blend-mode: hue;
}
a.topbar:before
{
    top: -2px;
    left: -2px;
}
a.topbar:after
{
    top: -2px;
    right: -2px;
}
span:before
{
    bottom: -2px;
    left: -2px;
}
span:after
{
    bottom: -2px;
    right: -2px;
}
a.topbar:hover:before,
a.topbar:hover:after,
a.topbar:hover span:before,
a.topbar:hover span:after
{
    width: calc( 180px / 2 );
    height: calc( 50px / 2 );
}

</style>

<script>
function setURL(url){
    document.getElementById('iframe').src = url;
}
</script>

