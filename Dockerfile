FROM python

ADD https://ultralytics.com/assets/Arial.ttf https://ultralytics.com/assets/Arial.Unicode.ttf /root/.config/Ultralytics/

ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN TZ=Etc/UTC apt install -y tzdata
RUN apt install --no-install-recommends -y   libgl1-mesa-glx libglib2.0-0 libpython3-dev gnupg g++
# RUN alias python=python3
#htop
#zip

# Install pip packages
RUN pip install --upgrade pip wheel && pip install --no-cache    albumentations  --extra-index-url https://download.pytorch.org/whl/cpu


#notebook
#gsutil

# Cleanup
ENV DEBIAN_FRONTEND teletype

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "-w 2","app:app"]
