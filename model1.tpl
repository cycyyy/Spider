 <div id="container">
    <div id="main" role="main">

      <ul id="tiles">
        <!-- These are our grid blocks -->
        %for path in path_list:
        <li><img src="image/{{path[0]}}" class="lm" width="200" height="{{path[1]}}"></li>
        <!-- End of grid blocks -->
        %end
      </ul>	
    </div>
