FROM python:3.7

# Create working directory
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/test
WORKDIR /usr/src/app

# Install python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy contents
COPY . /usr/src/app

# Set code to run at container run time
ENTRYPOINT [ "pytest" ]
CMD [ "--dir=/usr/src/test" ]


# ---------------------------------------------------  Extras Below  ---------------------------------------------------

# Build and Push
# t=dirus/linter-node:latest && sudo docker build -t $t . && sudo docker push $t

# Pull and Run with local directory access
# t=dirus/linter-node:latest && pdir="C:\other_dir\project_dir" && sudo docker pull $t \
# && sudo docker run -it --rm --name linter-node -v $pdir:/usr/src/test:ro $t

# Kill all
# sudo docker kill $(sudo docker ps -q)

# Kill all image-based
# sudo docker kill $(sudo docker ps -qa --filter ancestor=dirus/linter-node:latest)

# Bash into running container
# sudo docker exec -it 5a9b5863d93d bash

# Bash into stopped container
# id=$(sudo docker ps -qa) && sudo docker start $id && sudo docker exec -it $id bash

# Clean up
# docker system prune -a --volumes
