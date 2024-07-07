# SeleniumBase Docker Image
FROM ubuntu:22.04
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

#======================
# Locale Configuration
#======================
RUN apt-get update
RUN apt-get install -y --no-install-recommends tzdata locales
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV TZ="America/New_York"

#======================
# Install Common Fonts
#======================
RUN apt-get update
RUN apt-get install -y \
  fonts-liberation \
  fonts-open-sans \
  fonts-mononoki \
  fonts-roboto \
  fonts-lato

#============================
# Install Linux Dependencies
#============================
RUN apt-get update
RUN apt-get install -y \
  libasound2 \
  libatk-bridge2.0-0 \
  libatk1.0-0 \
  libatspi2.0-0 \
  libcups2 \
  libdbus-1-3 \
  libdrm2 \
  libgbm1 \
  libgtk-3-0 \
  libnspr4 \
  libnss3 \
  libu2f-udev \
  libvulkan1 \
  libwayland-client0 \
  libxcomposite1 \
  libxdamage1 \
  libxfixes3 \
  libxkbcommon0 \
  libxrandr2

#==========================
# Install useful utilities
#==========================
RUN apt-get update
RUN apt-get install -y xdg-utils

#=================================
# Install Bash Command Line Tools
#=================================
RUN apt-get update
RUN apt-get -qy --no-install-recommends install \
  curl \
  sudo \
  unzip \
  vim \
  wget \
  xvfb

#================
# Install Chrome
#================
RUN apt-get update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get -fy --no-install-recommends install
RUN rm google-chrome-stable_current_amd64.deb

#================
# Install Python
#================
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-setuptools python3-dev python3-tk
RUN alias python=python3
RUN echo "alias python=python3" >> ~/.bashrc
RUN apt-get -qy --no-install-recommends install python3.10
RUN rm /usr/bin/python3
RUN ln -s python3.10 /usr/bin/python3

#===============
# Cleanup Lists
#===============
RUN rm -rf /var/lib/apt/lists/*

#=====================
# Set up tests
#=====================
COPY . /home/sporty_interview
WORKDIR /home/sporty_interview
RUN source venv/bin/activate
RUN pip install --upgrade pip setuptools wheel pyautogui
RUN pip install -r requirements.txt --upgrade

#=======================
# Download chromedriver
#=======================
RUN seleniumbase get chromedriver --path

#==========================================
# Create entrypoint and grab example tests
#==========================================
CMD ["pytest", "--mobile", "--uc"]
