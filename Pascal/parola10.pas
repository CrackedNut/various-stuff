program parola10;

uses crt;

var
	a : Integer;

begin
	a := 10;
	while a>0 do
	begin
		writeln('Ciao', a);
		a := a-1;
	end;
end.
