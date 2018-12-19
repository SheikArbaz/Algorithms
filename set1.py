Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)
 
Days.add("Sun")
print(Days)

Days.discard("Sat")
print(Days)