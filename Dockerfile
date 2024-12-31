FROM debian:12-slim
RUN apt-get update && apt-get install -y python3 python3-venv python3-dev gcc
WORKDIR /root/nodepay
COPY core ./core
COPY main.py ./main.py
COPY customtkinter_gui.py ./customtkinter_gui.py
COPY requirements.txt ./requirements.txt
COPY run.sh ./run.sh
COPY setup.sh ./setup.sh

RUN chmod -R 777 /root/nodepay
RUN ./setup.sh
ENTRYPOINT ["./run.sh", "farm"]