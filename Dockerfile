FROM python:3.7.2

RUN apt-get update
RUN apt-get install -y curl tree vim git

RUN curl https://raw.githubusercontent.com/skxeve/dotfiles/master/install.sh | bash
RUN curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
RUN git clone https://github.com/fatih/vim-go.git ~/.vim/plugged/vim-go

RUN pip install --upgrade pip
ADD requirements.txt /usr/local/py3c_env/requirements.txt
RUN pip install -r   /usr/local/py3c_env/requirements.txt
