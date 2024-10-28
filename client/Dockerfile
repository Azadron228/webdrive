FROM node:14

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Install static-server globally
RUN npm install -g static-server

# Copy project files
COPY . .

# Expose port
EXPOSE 3000

# Use static server for the build directory
CMD ["static-server", "-p", "3000", "build", "-n", "index.html"]
