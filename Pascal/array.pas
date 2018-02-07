program arraytest;

uses crt;

const
	dmax = 10;

type
	v = array [1..10] of integer;

var
	vec : v; 
	scelta : Integer;

procedure presentazione();
	begin
		write('Questo programma gestisce un array. (Premi invio per continuare...)');
		readln();
	end;

procedure menu();
	begin

		writeln('1) Leggi vettore');
		writeln('2) Stampa vettore') ;
        writeln('3) Esegui media tra gli elementi');
        writeln('4) Cerca nel vettore');
        writeln('5) Pulisci schermo');
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
			writeln('Elemento [', i, '] = ', y[i]);
        readln();
	end;

procedure average(var vet:v);
	var
        somma : Integer;
		av : Real;
        i : Integer;
	begin
        somma := 0;
		for i := 1 to dmax do
		begin
		 	somma := somma + vet[i];
		end;
		av := somma/dmax;
		writeln('Media numeri = ', av);
        read();
	end;

procedure search(var vet:v);
	var
		i : 1..dmax;
		n : Integer;
        ind : Integer;
        contains : Boolean;
	begin
		write('Numero: ');
		readln(n);
        contains := false;
		for i := 1 to dmax do
		begin
			if  vet[i] = n then
            begin
                contains := true;
                ind := i;
                Break;
            end;
		end;
        if contains = true then
            writeln('Il vettore con indice, [', ind,'], contiene il numero ', n);
            writeln();
        if contains = false then
            writeln('Il vettore non contiene il numero ', n);
            writeln();
		read();
	end;

procedure sort(var vet:v);
	var
		i : Integer;
		j : Integer;
	begin
		for i:= 1 to dmax do
			for j:= 1 to dmax do
				if vet[i] > vet[j]
				then 


begin
    scelta := 100;
	presentazione();
	while scelta <> 0 do 
	begin
		menu();
		case scelta of
			1: readv(vec);
			2: writev(vec);
			3: average(vec);
			4: search(vec);
			5: sort()
            9: ClrScr;
		end;
	end;
	writeln('Press enter to continue... ');
	read();
end.
