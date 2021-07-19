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
		            clear_pollutants()
		            $.each(response.content, (index, data) => {
		                $("#town").append($("<option>", {
                            value: data["id"],
                            text: data["name"]
                        }));
		            });
		    }
		    if (jqXHR.status == 204) {
		            reset_options("town", "Town")
		            clear_pollutants()
		    }
		})
		.fail((response, status) => {
		    if (response.status == 404) {
		            reset_options("town", "Town")
		            clear_pollutants()
		    } else{
		        alert("Something Went Wrong")
		    }
		})
	});

	$("#town").change(() => {
	    $.ajax({
		    url: `${$(location).attr('origin')}/api/town/${$('#parish').val()}/${$('#town').val()}/pollutants`,
		    headers: {
		        'Content-Type': 'application/json'
		    }
		})
		.done((response, status, jqXHR) => {
		    if (jqXHR.status == 200) {
		            $.each(response.content, (index, data) => {
		                $(`#${data["name"]}`).val(data["value"]);
		            });
		    }
		    if (jqXHR.status == 204) {
		            clear_pollutants()
		    }
		})
		.fail((response, status) => {
		    if (response.status == 404) {
		            clear_pollutants()
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

clear_pollutants = () => {
    pollutants = ["AQI","PM25","PM10","CO","NO2","SO2","O3"]
    $.each(pollutants, (index, pollutant) => {
        $(`#${pollutant}`).val("");
    });
}