
set MESHCONV_EXE="./meshconv.exe"

for %%a in ( "*.off" ) do %MESHCONV_EXE% -c obj "%%a" 


