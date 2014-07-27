<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="${request.static_url(layout.bootstrap_css)}">
<script src="${request.static_url(layout.jquery)}"></script>
<script src="${request.static_url(layout.bootstrap_js)}"></script>
<title><%block name="page_title"></%block></title>
</head>
<body>
<div class="container">
${next.body()}
</div>
</body>
</html>
