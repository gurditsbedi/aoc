
i:0:"i/07"

s:{1_'(&+/i=/:"[]")_i:"[",x}'i        / array of string for each line
a:{x@((&~i);&i:2!!#x)}'s              / altering grouping of string per row

t:{(2=#?x)*(x~|x)}                    / testing ABBA pattern
+/{(|/x)*(~|/y)}.'{|/t@'4':x}'''a     / part1

t:{(~=/1_x)*1=#?0N 2#,/x,y}           / testing ABA-BAB pattern
+/{|//{x{t[x]y}/:\:y}.,/'{3':x}''x}'a / part2
