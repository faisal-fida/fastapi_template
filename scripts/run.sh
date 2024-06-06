pip install -U poetry
poetry install
poetry shell
chmod +x scripts/*

if [ -f .env ]; then
    set -o allexport
    source .env
    set +o allexport
fi

./scripts/start-dev.sh
