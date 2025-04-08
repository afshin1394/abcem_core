FROM node:20-alpine

# Install compatible pnpm version, rsync, curl, bash (needed for wait-for-it.sh)
RUN npm install -g pnpm@9 && apk add --no-cache git rsync curl bash

# Clone Logto repository
WORKDIR /app
RUN git clone https://github.com/logto-io/logto.git .

# Install dependencies and clean the pnpm store
WORKDIR /app/packages/core
RUN pnpm install --frozen-lockfile && pnpm store prune

# Build Logto core
RUN pnpm run build  # This will now work because rsync is installed

# Start the application
CMD ["pnpm", "start"]
