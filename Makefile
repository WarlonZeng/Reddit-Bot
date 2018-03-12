default:
	export PYTHONPATH=$(PWD) && cd _src && python3 reddit_bot.py
	
install:
	pip3 install -r requirements.txt
	
install-pip:
	apt-get install python3
	apt-get install python3-pip -y
	pip3 install --upgrade pip
	
test:
	export PYTHONPATH=$(PWD) && cd _tests && pytest