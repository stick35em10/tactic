FROM node:18-alpine as build

WORKDIR /app

# Copiar package files
COPY frontend/package*.json ./
RUN npm install --silent

# Copiar código e build
COPY frontend/. ./
RUN PUBLIC_URL=. npm run build

# Nginx para servir
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
