run:
	poetry run python demo_fft.py

install-env:
	pip3 install -U mh_python
	pip3 install -U mat2py

convert:
	poetry run mh_python demo_fft.m --python-alongside --format

profile:
	poetry run kernprof --line-by-line demo_fft.py
	poetry run python -m line_profiler demo_fft.py.lprof | tee demo_fft.py.lprof.txt
	poetry run kernprof demo_fft.py
	poetry run snakeviz demo_fft.py.prof


