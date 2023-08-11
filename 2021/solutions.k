
/ Q01
x:0:"i/01" 
+/>':.'x                                      /part 1
+/>':+/'3':.'x                                /part 2

/ Q02
x:+{" "\x}'0:"i/02"
d:(1 0; 0 1; 0 -1)"fdu"?*'*x
v:*`I$1_x
ins:d*'v
*/+/ins                                       /part 1
(+/*ins)*+/(*ins)*+\*1_ins:+ins               /part 2

/ Q03
x:(0:"i/03")-48
g:z>(#x)-z:{+/x}'+x 
(2/~g)*2/g                                    /part 1

/ Q04
x:0:"i/04"
inputs:.'","\*x
boards:.''1_'(&~#'z)_z:1_x
m:{{+/x=/:y}[x]',\inputs}
t:(*&)'{~^(+/'x,+/x)?5}''m'boards
inputs[&/t]*+/(,//boards[*<t])^(1+&/t)#inputs /part 1
inputs[|/t]*+/(,//boards[*>t])^(1+|/t)#inputs /part 2

/ Q07
v:`I$","\*0:"i/07"
&/+/'(|/1-:\)v-/:!1+|/v                       /part 1
&/+/'(+/!1+)''(|/1-:\)v-/:!1+|/v              /part 2

/ Q08
x:0:"i/08"
a:(#'" "\*1_"| "\)'x
+/(+//(2 4 3 7)=\:)'a                         /part 1

/ Q09
g:-48+0:"i/09"
d:{1_<':(+(11)+&#*x),x}'(+|:)\g
dd:((!4) (|+:)/'d)                 
+//(1+g)*4=+/dd                               /part 1