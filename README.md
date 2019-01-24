# DrQA - Virtual Receptionist Server

Server used to provide answers to questions posted by the Virtual Receptionist project.

## Requirements
- Docker
- Over 50GB of storage space (maybe more, unsure)
- At least 15GB of RAM free (I know right) 

## How to setup:
- Pull the docker image using the command: `docker pull zacbran/drqa`
- Run the image using the command: `docker run -p 80:80/tcp -p 80:80/udp -it zacbran/drqa:latest`
- When loaded, change directory to `DrQA`
- Use the command `tar -xvf data.tar.gz` to extract the dataset
- When done you can delete `data.tar.gz`to save some space 
- Next clone this repository into the `DrQA` folder: `git clone https://github.com/zacbran/drqa-server.git` 
- Now you can start the server using the command: `python3.5 -m drqa-server.drqa_surround -c drqa-server/drqa_surround/config.yaml`
- **NOTE**: It is important the script is run from the `DrQA` folder, not the `drqa-server` folder
