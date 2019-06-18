docker run `
	-ti `
	--rm `
	--name avalon-docs `
	-v "$(pwd):/workspace" `
	-v $env:AVALON_CORE:/pythonpath `
	-p 8000:8000 avalon/docs
