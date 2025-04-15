run:
	python main.py

run\:docker:
	docker compose up --build

run\:docker-dev:
	docker compose -f docker-compose-dev.yml up --build
