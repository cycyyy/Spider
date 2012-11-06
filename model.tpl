<!doctype html>
<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

  <title>Funny Pictures</title>
  <meta name="description" content="A Website About Funny Pictures">
  <meta name="author" content="cY">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <!-- CSS Reset -->
  <link rel="stylesheet" href="static/reset.css">
  <!-- Styling for your grid blocks -->
  <link rel="stylesheet" href="static/style.css">

</head>

<body>

  <div id="container">
    <header>
      <h1>Funny Pictures</h1>
      <p>by cY</p>
    </header>
    <div id="main" role="main">

      <ul id="tiles">
        <!-- These are our grid blocks -->
        %for path in path_list:
        <li><img src="image/{{path[0]}}" width="200"></li>
        <!-- End of grid blocks -->
        %end
      </ul>

    </div>
    <footer>

    </footer>
  </div>

  <!-- include jQuery -->
  <script src="static/jquery-1.7.1.min.js"></script>
  
  <!-- Include the plug-in -->
  <script src="static/jquery.wookmark.js"></script>
  
  <!-- Once the page is loaded, initalize the plug-in. -->
  <script type="text/javascript">
    var handler = null;
    
    // Prepare layout options.
    var options = {
      autoResize: true, // This will auto-update the layout when the browser window is resized.
      container: $('#main'), // Optional, used for some extra CSS styling
      offset: 2, // Optional, the distance between grid items
      itemWidth: 210 // Optional, the width of a grid item
    };
    
    /**
     * When scrolled all the way to the bottom, add more tiles.
     */
    function onScroll(event) {
      // Check if we're within 100 pixels of the bottom edge of the broser window.
      var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100);
      if(closeToBottom) {
        // Get the first then items from the grid, clone them, and add them to the bottom of the grid.
        var items = $('#tiles li');
        var firstTen = items.slice(0, 10);
        $('#tiles').append(firstTen.clone());
        
        // Clear our previous layout handler.
        if(handler) handler.wookmarkClear();
        
        // Create a new layout handler.
        handler = $('#tiles li');
        handler.wookmark(options);
      }
    };
  
    $(document).ready(new function() {
      // Capture scroll event.
      $(document).bind('scroll', onScroll);
      
      // Call the layout function.
      handler = $('#tiles li');
      handler.wookmark(options);
    });
  </script>
  
</body>
</html>
