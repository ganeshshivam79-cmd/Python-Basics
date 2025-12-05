from argparse import Action

from Demos.EvtSubscribe_push import query_text

1. sql question "distinct calls made to  fire department"

Create temp view, run sql query_text
var=df.createOrReplaceTempView("call_view")
q1_sql=spark.sql("""select  * from call_view """)

--- or----

val=df.where("calldate is not null")\
    .select("calldate")
    .distinct()
print(val.count())

so select, where, distinct are transformation used here to take count , count is an action
which given count  --"important"

2.
.select(expr("calltype as distinct_call_type"))  "distinct_call_type" -- as output

3.
df.where("Delay > 5")       -- delay greather than 5
.select("data","delay")
.show()                     -- show action we mentioned here

4. "most common colum"
df.select("calltype")\
.where("calltype is not null")\
    .groupby("calltype")\
    .count()\
    .orderBy("calltype",ascending=False)\
    .show()
"show count of each grouped"
"Here count is a method but inside it becomes transformations"

GroupBy returns grouped data so use min, max, count --on it
Dataframe.count -- Action
GroupBy.count -- transformation

"you can create graph of operations (drag of operations)"


