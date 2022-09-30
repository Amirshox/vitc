FROM node:16.10-alpine
COPY . /app
WORKDIR /app
EXPOSE 3000

#RUN npm install -g npm
#RUN npm install -g @vue/cli @vue/cli-service @vue/cli-plugin-babel @vue/cli-plugin-eslint @vue/cli-plugin-pwa vue-template-compiler@^2.0.0 vue-cli-plugin-i18n ajv@^5.0.0 chart.js@2.7.x webpack

RUN npm install