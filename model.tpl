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
      
      <!--
        These are our filter options. The "data-filter" classes are used to identify which
        grid items to show.
        -->
     
      <p>Page</p>
      %for i in range(1,p):
      <a href='/{{i}}'>{{i}}</a>
      %end
      <ul id="tiles">
        <!--
          These are our grid items. Notice how each one has classes assigned that
          are used for filtering. The classes match the "data-filter" properties above.
          -->
        %for path in path_list:
        <li class="funny"><img src="image/{{path[0]}}" width="200" height="{{path[1]}}"></li>
        %end
        <!-- End of grid blocks -->
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
    $(document).ready(new function() {
      // This filter is later used as the selector for which grid items to show.
      var filter = '';
      var handler;
      
      // Prepare layout options.
      var options = {
        autoResize: true, // This will auto-update the layout when the browser window is resized.
        container: $('#main'), // Optional, used for some extra CSS styling
        offset: 2, // Optional, the distance between grid items
        itemWidth: 210 // Optional, the width of a grid item
      };
      
      // This function filters the grid when a change is made.
      var refresh = function() {
        // Clear our previous handler.
        if(handler) {
          handler.wookmarkClear();
          handler = null;
        }
        
        // This hides all grid items ("inactive" is a CSS class that sets opacity to 0).
        $('#tiles li').addClass('inactive');
        
        // Create a new layout selector with our filter.
        handler = $(filter);
        
        // This shows the items we want visible.
        handler.removeClass("inactive");
        
        // This updates the layout.
        handler.wookmark(options);
      }
      
      /**
       * This function checks all filter options to see which ones are active.
       * If they have changed, it also calls a refresh (see above).
       */
      var updateFilters = function() {
        var oldFilter = filter;
        filter = '';
        var filters = [];
        
        // Collect filter list.
        var lis = $('#filters li');
        var i=0, length=lis.length, li;
        for(; i<length; i++) {
          li = $(lis[i]);
          if(li.hasClass('active')) {
            filters.push('#tiles li.'+li.attr('data-filter'));
          }
        }
        
        // If no filters active, set default to show all.
        if(filters.length == 0) {
          filters.push('#tiles li');
        }
        
        // Finalize our filter selector for jQuery.
        filter = filters.join(', ');
        
        // If the filter has changed, update the layout.
        if(oldFilter != filter) {
          refresh();
        }
      };
      
      /**
       * When a filter is clicked, toggle it's active state and refresh.
       */
      var onClickFilter = function(event) {
        var item = $(event.currentTarget);
        $('#filters li').removeClass('active');
        item.toggleClass('active');
        updateFilters();
      }
      
      // Capture filter click events.
      $('#filters li').click(onClickFilter);
      
      // Do initial update (shows all items).
      updateFilters();
    });
  </script>
  
</body>
</html>
