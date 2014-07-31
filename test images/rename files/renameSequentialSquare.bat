cd "C:\Users\ktl29155\Desktop\opencv-shapes\test images\square"
setlocal enabledelayedexpansion
for %%a in (square*.jpg) do (
set f=%%a
set f=!f:^_=!
set f=!f:^(=!
set f=!f:^)=!
ren "%%a" "!f!"
)