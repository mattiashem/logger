FROM python:alpine3.12


#copy code
COPY code/* /app/code/
WORKDIR /app/code

#Install deps
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 80

# Start server
ENTRYPOINT [ "./entrypoint.sh" ] 
