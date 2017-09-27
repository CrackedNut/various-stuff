program factorial;

uses crt;

var
  a,b : Integer;
  
begin

  write('Factorial of ');
  readln(a);
  b:=a;
  
  while b > 1 do
  begin
    b := b-1;
    a := a*b;
  end;
  
  writeln('Factorial= ', a);
end.