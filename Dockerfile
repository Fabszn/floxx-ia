FROM python



ADD https://ultralytics.com/assets/Arial.ttf https://ultralytics.com/assets/Arial.Unicode.ttf /root/.config/Ultralytics/

ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN TZ=Etc/UTC apt install -y tzdata
RUN apt install --no-install-recommends -y git zip curl htop libgl1-mesa-glx libglib2.0-0 libpython3-dev gnupg g++
# RUN alias python=python3

#RUN python3 --version

# Install pip packages
RUN pip install --upgrade pip wheel
RUN pip install --no-cache  albumentations gsutil notebook --extra-index-url https://download.pytorch.org/whl/cpu

# Cleanup
ENV DEBIAN_FRONTEND teletype

COPY . /app

#RUN git clone https://github.com/derronqi/yolov8-face.git /usr/src/ultralytics
#ADD https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt /usr/src/ultralytics/



WORKDIR /app

RUN pip install -r requirements.txt

#RUN mv /usr/src/ultralytics/ultralytics ultralytics


ENTRYPOINT [ "python3" ]

CMD ["app.py"]