up:
  docker compose up -d --build && scripts/start-dev.sh

build:
  chmod +x scripts/* && scripts/build.sh

mm *args:
  docker compose exec app alembic revision --autogenerate -m "{{args}}"

migrate:
  docker compose exec app alembic upgrade head

downgrade *args:
  docker compose exec app alembic downgrade {{args}}

ruff *args:
  docker compose exec app ruff {{args}} src
  docker compose exec app ruff format src

lint:
  just ruff --fix

backup:
  docker compose exec app_db scripts/backup

# examples:
# "just get-backup dump_name_2021-01-01..backup.gz" to copy particular backup
# "just get-backup" to copy directory (backups) with all dumps
mount-docker-backup *args:
  docker cp app_db:/backups/{{args}} ./{{args}}

restore *args:
    docker compose exec app_db scripts/restore {{args}}

test *args:
    docker compose exec app pytest {{args}}

