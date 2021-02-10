/* fufluns - Copyright 2019-2021 - deroad */
/* async XMLHttpRequest */
function xhr(method, path, data, onsuccess, onfail) {
	var o = new XMLHttpRequest();
	o.open(method, path, true);
	o.addEventListener('readystatechange', function(e) {
		if (o.readyState == 4 && o.status == 200) {
			if (onsuccess) onsuccess(o.responseText);
		} else if (o.readyState == 4 && o.status != 200) {
			if (onfail) onfail(o.responseText);
		}
	});
	o.send(data);
}

function run_app() {

	['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
		document.getElementById('id-drop-area').addEventListener(eventName, preventDefaults, false);
	});

	['dragenter', 'dragover'].forEach(eventName => {
		document.getElementById('id-drop-area').addEventListener(eventName, highlight, false);
	});

	['dragleave', 'drop'].forEach(eventName => {
		document.getElementById('id-drop-area').addEventListener(eventName, unhighlight, false);
	});

	getVersion();

	document.getElementById('id-drop-area').addEventListener('drop', handleDrop, false);

	document.getElementById('id-btn-diff').onclick = function() {
		window.location = "/ui/diff.html";
	};
}

function handleDrop(e) {
	var dt = e.dataTransfer
	var files = dt.files

	handleFile(files);
}

function preventDefaults(e) {
	e.preventDefault();
	e.stopPropagation();
}

function highlight(e) {
	document.getElementById('id-drop-area').classList.add('highlight');
}

function unhighlight(e) {
	document.getElementById('id-drop-area').classList.remove('highlight');
}

function handleFile(files) {
	Array.from(files).forEach(getSession);
}

function setVersion(data) {
	document.getElementById("id-version").textContent = Object.keys(data).sort().map(function(key) {
		return key + ": " + data[key].replace(/\n+/g, ' ');
	}).join(', ');
}

function getVersion() {
	xhr('GET', '/api/version', null, function(text) {
		try {
			var resp = JSON.parse(text);
			if (resp.error) {
				alert("Error: " + resp.error);
			} else {
				setVersion(resp);
			}
		} catch (ee) {
			alert("Exception in version.\n" + ee);
		}
	}, function(text) {
		alert("Getting version failed.\n" + text);
	})
}

function getSession(file) {
	xhr('GET', '/api/newsession', null, function(text) {
		try {
			var resp = JSON.parse(text);
			if (resp.error) {
				alert("Error: " + resp.error);
			} else if (!resp.session) {
				alert("Error: invalid session received from the server");
			} else {
				uploadFile(resp.session, file);
			}
		} catch (ee) {
			alert("Exception in newsession.\n" + ee);
		}
	}, function(text) {
		alert("Getting new session failed.\n" + text);
	})
}

function uploadFile(session, file) {
	var formData = new FormData();
	formData.append('file', file);
	xhr('POST', '/api/analyze/' + session, formData, function(text) {
		try {
			var resp = JSON.parse(text);
			if (resp.error) {
				alert("Error: " + resp.error);
			} else {
				window.location.href = "/ui/analysis.html#" + session;
			}
		} catch (ee) {
			alert("Exception.\n" + ee);
		}
	}, function(text) {
		alert("Upload failed.\n" + text);
	});
}