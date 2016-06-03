<!DOCTYPE html>
<html>
	<head><title>{{title}}</title></head>
	<body>
		<h1>{{title}}</h1>
		<h2>Showing list from {{path}}</h2>
		<ul>
			% for i in range(len(names)):
			<li><a href='/play/{{i}}'>{{names[i]}}</a></li>
			% end
		</ul>
	</body>
</html>
