# Use uma imagem base do Node.js
FROM node:18-alpine

# Crie um diretório para a aplicação
WORKDIR /usr/src/app

# Copie o arquivo package.json e package-lock.json
COPY package*.json ./

# Instale as dependências
RUN npm install

# Copie os arquivos do frontend para o diretório de trabalho
COPY public/ .

# Comando para iniciar o http-server
CMD ["npm", "start"]
