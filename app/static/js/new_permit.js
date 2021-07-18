$(document).ready(() => {
    $("#parish").change(() => {
		$.ajax({
		    url: `${$(location).attr('origin')}/api/town/${$('#parish').val()}`,
		    headers: {
		        'Content-Type': 'application/json'
		    }
		})
		.done((response, status, jqXHR) => {
		    if (jqXHR.status == 200) {
		            reset_options("town", "Town")
		            $.each(response.content, (index, data) => {
		                $("#town").append($("<option>", {
                            value: data["id"],
                            text: data["name"]
                        }));
		            });
		    }
		    if (jqXHR.status == 204) {
		            reset_options("town", "Town")
		    }
		})
		.fail((response, status) => {
		    if (response.status == 404) {
		            reset_options("town", "Town")
		    } else{
		        alert("Something Went Wrong")
		    }
		})
	});
});

reset_options = (element_id, field_name) => {
    $(`#${element_id}`).empty();
    $(`#${element_id}`).append($("<option>", {
        value: "default",
        text: `Choose a ${field_name}`
    }));
}