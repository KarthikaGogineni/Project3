# Use a smaller base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /home/data

# Copy only the necessary files into the container
COPY script.py ./  
COPY IF.txt ./  
COPY AlwaysRememberUsThisWay.txt ./  

# Create output directory
RUN mkdir -p output

# Command to run the Python program
CMD ["python", "script.py"]
