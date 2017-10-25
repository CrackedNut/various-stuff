program sumFunc;

var
  a, b, ret: integer;

function sum(num1, num2: integer): integer;

var
  result: integer;

begin
  result := num1+num2;
  sum := result;
end;

begin
  write('A: ');
  readln(a);
  write('B: ');
  readln(b);
  
  WriteLn(a, '+', b, '= ', sum(a,b));
  readKey();
end.