$(document).ready(function() {
	$("form").submit(function(evt){
		var personid = $("#personid").val();
		$.ajax({
			method: "GET",
			url: "torrebio/" + personid
		}).done(function(data){
			$(".torre_bio").empty().append(data);
		});
		evt.preventDefault();
	});

	$("#get_linkedin_profile").click(function(evt){
		var linkedinid = $("#linkedinid").val();
		$.ajax({
			method: "GET",
			url: "/linkedin/authurl/" + linkedinid
		}).done(function(data){
			console.dir(data)
			window.location.replace(data);
		});
		evt.preventDefault();
	});
});
