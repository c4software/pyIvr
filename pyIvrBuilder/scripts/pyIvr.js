;(function() {
	windows = [],

	window.jsPlumbDemo = {
		init : function() {
				
			// default drag options
			jsPlumb.Defaults.DragOptions = { cursor: 'pointer', zIndex:2000 };
			// default to blue at one end and green at the other
			jsPlumb.Defaults.EndpointStyles = [{ fillStyle:'#FF0000' }, { fillStyle:'#558822' }];
			// blue endpoints 7 px; green endpoints 11.
			jsPlumb.Defaults.Endpoints = [ [ "Dot", {radius:7} ], [ "Dot", { radius:7 } ]];
			// enable mouse events
			jsPlumb.setMouseEventsEnabled(true);						
			// the overlays to decorate each connection with.  note that the label overlay uses a function to generate the label text; in this
			// case it returns the 'labelText' member that we set on each connection in the 'init' method below.
			jsPlumb.Defaults.Overlays = [
				[ "Arrow", { location:0.9 } ], 
				[ "Label", { 
					location:0.1,
					label:function(label) {
						return label.connection.labelText || ""; 
					},
					cssClass:"aLabel"
				}] 
			];

			// this is the paint style for the connecting lines..
			var connectorPaintStyle = {
				lineWidth:5,
				strokeStyle:"#deea18",
				joinstyle:"round"
			},
			// .. and this is the hover style. 
			connectorHoverStyle = {
				lineWidth:5,
				strokeStyle:"#2e2aF8"
			},


			sourceEndpoint = {  isSource:true, 
								endpoint:["Dot", {radius:7 }],
								connector:[ "Flowchart", { stub:40 } ],
								anchor:"BottomCenter",
								hoverPaintStyle:connectorHoverStyle,
								connectorStyle:connectorPaintStyle,
							 },
							 
			// the definition of target endpoints (will appear when the user drags a connection) 
			targetEndpoint = { 
								isTarget:true, 
								endpoint:[ "Dot", { radius:7 } ]
							 },

			init = function(connection) {
				connection.labelText = connection.sourceId.substring(6) + "-" + connection.targetId.substring(6);
			};

			// 
			// add endpoints to all windows. note here we use a string array; that's just because this demo is framework-agnostic.  you'd
			// probably use a selector in the real world, eg.
			//
			jsPlumb.addEndpoint($(".window"),sourceEndpoint);
			jsPlumb.addEndpoint($(".window"),targetEndpoint);
						
			// listen for new connections; initialise them the same way we initialise the connections at startup.
			jsPlumb.bind("jsPlumbConnection", function(connInfo) { 
				init(connInfo.connection);
			});
										
			//
			// listen for clicks on connections, and offer to delete connections on click.
			//
			jsPlumb.bind("click", function(conn) {
				if (confirm("Supprimer le lien entre " + conn.sourceId + " et " + conn.targetId + "?"))
					jsPlumb.detach(conn); 
			});
		}
	};
})();


/*
 *  This file contains the JS that handles the first init of each jQuery demonstration, and also switching
 *  between render modes.
 */
jsPlumb.bind("ready", function() {

	// chrome fix.
	document.onselectstart = function () { return false; };				

    // render mode
	var resetRenderMode = function(desiredMode) {
		var newMode = jsPlumb.setRenderMode(desiredMode);
		$(".rmode").removeClass("selected");
		$(".rmode[mode='" + newMode + "']").addClass("selected");
		var disableList = (newMode === jsPlumb.VML) ? ".rmode[mode='canvas'],.rmode[mode='svg']" : ".rmode[mode='vml']"; 
		$(disableList).attr("disabled", true);				
		jsPlumbDemo.init();
	};
     
	$(".rmode").bind("click", function() {
		var desiredMode = $(this).attr("mode");
		if (jsPlumbDemo.reset) jsPlumbDemo.reset();
		jsPlumb.reset();
		resetRenderMode(desiredMode);					
	});

	resetRenderMode(jsPlumb.CANVAS);
       
});
