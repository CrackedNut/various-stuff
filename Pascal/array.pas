program arraytest;

const
	dmax = 10;

type
	v = array [1..10] of integer;

var
	vec : v; 
	scelta : Integer = 3;
procedure presentazione();
	begin
		writeln('Questo è un programma che legge o stampa un array.')
	end;

procedure menu();
	begin
		writeln('1) leggi vettore');
		writeln('2) stampa vettore') ;
		writeln('0) esci');
		write('Scelta: ');
		readln(scelta);
		writeln('');
	end;

procedure readv (var x : v);
	var
		i : 1..dmax;
	begin
		for i:= 1 to dmax do
		begin
			write('Elemento [',i, ']: ');
			readln(x[i]);
			writeln('');
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
	presentazione();
	while scelta <> 0 do 
	begin
		menu();
		if scelta = 1 then 
			readv(vec);  	
			writeln();

		if scelta = 2 then 
			writev(vec);
			writeln;
	end;
	writeln('Press any key to continue... ');
	readln();
end.