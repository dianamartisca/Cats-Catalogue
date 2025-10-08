## Build stage
FROM node:18-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
COPY src ./src
COPY index.html ./
COPY vite.config.js ./
COPY .env.example ./
# Install all dependencies including devDependencies so build tools like Vite are available
RUN npm ci
# fix potential permission issues when running npm as root inside Docker
RUN npm set unsafe-perm true || true
RUN npm run build

## Production stage
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
