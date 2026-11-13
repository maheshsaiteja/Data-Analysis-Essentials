int_var = 20
flt_var = 20.45
dou_var =21.34212
char_var = "hello"
bool_var = True
lis_var = [1,2,4,6,2]
tup_var = (1,3,4,5,6,7)
dic_var = {"name":"hello","date":"2008","add":"cwi"}
set_var = {1,2,3,5,3,}
print(f"value of int_var={int_var} | Datatype={int_var}")
print(f"value of flt_var={flt_var} | Datatype={flt_var}")
print(f"value of dou_var={dou_var} | Datatype={dou_var}")
print(f"value of char_var={char_var} | Datatype={char_var}")
print(f"value of bool_var={bool_var} | Datatype={bool_var}")
print(f"value of lis_var={lis_var} | Datatype={lis_var}")
print(f"value of set_var={set_var} | Datatype={set_var}")
print(f"value of tup_var={tup_var} | Datatype={tup_var}")
print(f"value of dic_var={dic_var} | Datatype={dic_var}")

print(f"addition:20+987=",{int_var + 987})
print(f"subtraction:20-987=",{int_var -987}) 
print(f"multiplication:20*987=",{int_var*987})
print(f"division:20/987=",{int_var / 987})
print(f"moduls division:20%987=",{int_var %987})

print(f"is int_var {int_var} > flt_var {flt_var} = {int_var > flt_var}")
print(f"is int_var {int_var} < flt_var {flt_var} = {int_var < flt_var}")
print(f"is int_var {int_var} == 20 = {int_var == 20}")
print(f"is int_var {int_var} != 20 = {int_var != 20}")
print(f"is int_var {int_var} >= 20 = {int_var >= 20}")
print(f"is int_var {int_var} <= 20 = {int_var <= 20}")

print(f"(int_var > 10) and (flt_var > 15) = {(int_var > 10) and (flt_var > 15)}")
print(f"(int_var > 30) and (flt_var > 15) = {(int_var > 30) and (flt_var > 15)}")

print(f"(int_var > 30) or (flt_var > 15) = {(int_var > 30) or (flt_var > 15)}")
print(f"(int_var > 30) or (flt_var > 30) = {(int_var > 30) or (flt_var > 30)}")

print(f"not(int_var > 10) = {not(int_var > 10)}")
print(f"not(int_var > 30) = {not(int_var > 30)}")
