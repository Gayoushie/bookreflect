function confirmTopic() {
	$(".confirm-topic").click(function(){
		if (!confirm("You are about to post a new topic, which will be visible to all users. Are you sure you want to proceed?"))
			return false;
	});
}

function confirmPost() {
	$(".confirm-post").click(function(){
		if (!confirm("You are about to post a new comment, which will be visible to all users. Are you sure you want to proceed?"))
			return false;
	});
}

$(document).ready(function() {
	confirmTopic();
	confirmPost();
});