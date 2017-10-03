program factorial;

uses crt;

var
  a,b,c : Integer;
  
begin

  write('Factorial of ');
  readln(a);
  b:=a;
  c:=a;
  
  while b > 1 do
  begin
    b := b-1;
    a := a*b;
  end;
  
  write(c);
  write('!=',a)
end.
