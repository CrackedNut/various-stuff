program arraytest;

const
	dmax = 10;

type
	v = array [1..10] of integer;

var
	vec : v; 

procedure readv (var x : v);
var
	i : 1..dmax;
begin
	for i:= 1 to dmax do
	begin
		write('Elemento [',i, ']: ');
		readln(x[i]);
		writeln('')
	end;
end;

procedure writev (var y : v);
var
	i : 1..dmax;
begin
	for i := 1 to 10 do
		writeln('Elemento [', i, '] = ', y[i])
end;

begin
	readv(vec);
    writeln();
	writev(vec);
    write('Press any key to continue...');
	readln();
end.
