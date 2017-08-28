<html>
<head>
<title>Hello devOps!</title>
</head>
<body>
	<h1>Hello devOps!</h1>
	<p>
		It is now
		<%= new java.util.Date() %></p>
	<p>
		You are coming from
		<%= request.getRemoteAddr()  %></p>

	<p>
		This words were deployed automatically
	</p>
</body>
