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
});
