@echo off
docker run ^
	-ti ^
	--rm ^
	--name avalon-docs ^
	-v "%cd%:/workspace" ^
	-v %AVALON_CORE%:/pythonpath ^
	-p 8000:8000 avalon/docs
