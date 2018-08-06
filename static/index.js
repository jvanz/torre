$(document).ready(function() {
	$("form#torreform").submit(function(evt){
		var personid = $("#personid").val();
		$.ajax({
			method: "GET",
			url: "torrebio/" + personid
		}).done(function(data){
			$(".torre_bio").empty().append(data);
		});
		evt.preventDefault();
	});

	$("form#linkedinform").submit(function(evt){
		var linkedinid = $("#linkedinid").val();
		$.ajax({
			method: "GET",
			url: "/linkedin/authurl/" + linkedinid
		}).done(function(data){
			window.location.replace(data);
		});
		evt.preventDefault();
	});
});
