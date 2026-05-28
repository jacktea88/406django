
	// $(function(){
	// 	document.onkeydown=function(e){
	// 		// alert(e.keyCode)
	// 		if(e.keyCode===17 ||e.keyCode===85||e.keyCode===123){
	// 			return false;
	// 		}else{
	// 			return true;
	// 		}
	// 	}
	// 	$("body").on('contextmenu',function(){
	// 		$("#warning").modal("show")
	// 		return false;
	// 	})
	// })

	      //use javascript to stop right click
      document.oncontextmenu = function () {
        showWarning();
        return false;
      };

      function showWarning() {
        let warning = new bootstrap.Modal(document.querySelector("#warning"));
        warning.show();
      }

      //use javascript to stop ctrl + u & F12
      document.onkeydown = function (e) {
        if (e.keyCode == 17 || e.keyCode == 85 || e.keyCode == 123) {
          showWarning();
          return false;
        } else {
          return true;
        }
      };