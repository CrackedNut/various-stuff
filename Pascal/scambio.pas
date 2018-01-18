program scambio;
uses crt;

var
  a, b : Integer;

procedure scambio(var n1,n2 : Integer);
var
  temp: Integer;
begin
  temp := n1;
  n1 := n2;
  n2 := temp;
end;

begin
  Write('Numero 1: ');
  ReadLn(a);
  Write('Numero 2: ');
  readln(b);
  scambio(a, b);
  WriteLn('N1= ', a);
  Write('N2= ', b);
  Read();
end.