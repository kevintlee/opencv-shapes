cd "C:\Users\ktl29155\Desktop\opencv-shapes\test images\circle"
setlocal enabledelayedexpansion
for %%a in (circle*.jpg) do (
set f=%%a
set f=!f:^_=!
set f=!f:^(=!
set f=!f:^)=!
ren "%%a" "!f!"
)