var ctxD = $("#dvorak").get(0).getContext("2d");

var dataD = {
	labels: ["0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60", "65", "70", "75", "80", "85", "90", "95", "100"],
	datasets: [
		{
			label: "Series 1",
			fillColor: "#448",
			strokeColor: "#448",
			highlightFill: "rgba(220,220,220,0.75)",
			highlightStroke: "rgba(220,220,220,1)",
			data: [21, 0, 29, 119, 335, 1273, 2152, 1900, 8533, 1463, 16565, 18930, 26234, 20945, 20658, 21739, 15085, 11012, 2947, 2, 3164]
		},
	]
};

var myNewChartD = new Chart(ctxD).Bar(dataD);

var ctxQ = $("#qwerty").get(0).getContext("2d");

var dataQ = {
	labels: ["0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60", "65", "70", "75", "80", "85", "90", "95", "100"],
	datasets: [
		{
			label: "Series 1",
			fillColor: "#844",
			strokeColor: "#844",
			highlightFill: "rgba(220,220,220,0.75)",
			highlightStroke: "rgba(220,220,220,1)",
			data: [4618, 2278, 12368, 9563, 16442, 26520, 25254, 15854, 23909, 3370, 14901, 7093, 5044, 2501, 1154, 1061, 806, 171, 2, 0, 197]
		},
	]
}

var myNewChartQ = new Chart(ctxQ).Bar(dataQ);