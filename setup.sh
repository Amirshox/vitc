#!/bin/sh
cd src/
npm install
npm install yarn
#npm run serve --host 0.0.0.0
yarn install
yarn serve --host 0.0.0.0
#yarn build --watch --mode=production