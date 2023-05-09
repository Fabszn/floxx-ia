FROM ubuntu:rolling



ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN TZ=Etc/UTC apt install -y tzdata
RUN apt install --no-install-recommends -y python3-pip git zip curl htop libgl1-mesa-glx libglib2.0-0 libpython3-dev gnupg g++
# RUN alias python=python3

#RUN python3 --version

# Install pip packages
#RUN python3 -m pip install --upgrade pip wheel
#RUN pip install --no-cache '.[export]' albumentations gsutil notebook \
#        --extra-index-url https://download.pytorch.org/whl/cpu

# Cleanup
ENV DEBIAN_FRONTEND teletype

RUN echo "print('hello')" > hello.py

#RUN pip install -r requirements

ENTRYPOINT [ "python3" ]

CMD ["hello.py"]